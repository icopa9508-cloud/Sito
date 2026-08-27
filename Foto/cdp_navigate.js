const { spawn } = require('child_process');

const edgePath = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
const port = 9224;

const browser = spawn(edgePath, [
  `--remote-debugging-port=${port}`,
  '--headless=new',
  '--disable-gpu',
  'about:blank'
]);

setTimeout(async () => {
  try {
    const listRes = await fetch(`http://127.0.0.1:${port}/json/list`);
    const pages = await listRes.json();
    const wsUrl = pages[0].webSocketDebuggerUrl;
    console.log("Connected to page WebSocket...");

    const ws = new global.WebSocket(wsUrl);

    ws.onopen = () => {
      ws.send(JSON.stringify({ id: 1, method: 'Runtime.enable' }));
      ws.send(JSON.stringify({ id: 2, method: 'Log.enable' }));
      ws.send(JSON.stringify({ id: 3, method: 'Page.enable' }));
      ws.send(JSON.stringify({ id: 4, method: 'Page.navigate', params: { url: 'file:///c:/Users/Enrico/Desktop/Giada/the_irish_year.html' } }));
    };

    ws.onmessage = (event) => {
      const msg = JSON.parse(event.data);
      if (msg.method === 'Runtime.consoleAPICalled') {
        console.log('BROWSER CONSOLE:', msg.params.type, msg.params.args.map(a => a.value || a.description || JSON.stringify(a)));
      } else if (msg.method === 'Runtime.exceptionThrown') {
        console.error('BROWSER UNCAUGHT EXCEPTION:', msg.params.exceptionDetails.text, msg.params.exceptionDetails.exception ? (msg.params.exceptionDetails.exception.description || msg.params.exceptionDetails.exception.value) : '');
      } else if (msg.method === 'Log.entryAdded') {
        console.log('BROWSER LOG:', msg.params.entry.level, msg.params.entry.text);
      }
    };

    setTimeout(() => {
      // Evaluate document.body.innerHTML or #root.innerHTML after 4 seconds
      ws.send(JSON.stringify({
        id: 10,
        method: 'Runtime.evaluate',
        params: { expression: 'document.getElementById("root").innerHTML' }
      }));
    }, 3500);

    ws.onmessage = (event) => {
      const msg = JSON.parse(event.data);
      if (msg.id === 10) {
        console.log("ROOT INNER HTML (length):", msg.result.result.value ? msg.result.result.value.length : 'NULL');
        console.log("ROOT INNER HTML (first 300 chars):", (msg.result.result.value || '').substring(0, 300));
        ws.close();
        browser.kill();
        process.exit(0);
      } else if (msg.method === 'Runtime.consoleAPICalled') {
        console.log('BROWSER CONSOLE:', msg.params.type, msg.params.args.map(a => a.value || a.description));
      } else if (msg.method === 'Runtime.exceptionThrown') {
        console.error('BROWSER UNCAUGHT EXCEPTION:', msg.params.exceptionDetails.text, msg.params.exceptionDetails.exception ? (msg.params.exceptionDetails.exception.description || msg.params.exceptionDetails.exception.value) : '');
      } else if (msg.method === 'Log.entryAdded') {
        console.log('BROWSER LOG:', msg.params.entry.level, msg.params.entry.text);
      }
    };

  } catch (err) {
    console.error("Error:", err);
    browser.kill();
  }
}, 1500);
