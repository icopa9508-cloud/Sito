const { spawn } = require('child_process');

const edgePath = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
const port = 9223;

const browser = spawn(edgePath, [
  `--remote-debugging-port=${port}`,
  '--headless=new',
  '--disable-gpu',
  'file:///c:/Users/Enrico/Desktop/Giada/the_irish_year.html'
]);

console.log("Spawned browser, waiting for CDP on port " + port + "...");

setTimeout(async () => {
  try {
    const listRes = await fetch(`http://127.0.0.1:${port}/json/list`);
    const pages = await listRes.json();
    console.log("Pages found:", pages.length);
    const wsUrl = pages[0].webSocketDebuggerUrl;
    console.log("WebSocket URL:", wsUrl);

    const ws = new global.WebSocket(wsUrl);

    ws.onopen = () => {
      console.log("CDP WebSocket opened. Enabling Runtime and Log...");
      ws.send(JSON.stringify({ id: 1, method: 'Runtime.enable' }));
      ws.send(JSON.stringify({ id: 2, method: 'Log.enable' }));
      ws.send(JSON.stringify({ id: 3, method: 'Console.enable' }));
      ws.send(JSON.stringify({ id: 4, method: 'Runtime.runIfWaitingForDebugger' }));
    };

    ws.onmessage = (event) => {
      const msg = JSON.parse(event.data);
      if (msg.method === 'Runtime.consoleAPICalled') {
        console.log('CONSOLE:', msg.params.type, msg.params.args.map(a => a.value || a.description));
      } else if (msg.method === 'Runtime.exceptionThrown') {
        console.error('UNCAUGHT EXCEPTION:', JSON.stringify(msg.params, null, 2));
      } else if (msg.method === 'Log.entryAdded') {
        console.log('LOG ENTRY:', msg.params.entry);
      }
    };

    // Wait 5 seconds to observe loading and post-loading
    setTimeout(() => {
      console.log("Finished observing browser. Killing browser...");
      ws.close();
      browser.kill();
      process.exit(0);
    }, 5000);

  } catch (err) {
    console.error("CDP Error:", err);
    browser.kill();
  }
}, 1500);
