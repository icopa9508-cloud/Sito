const { spawn } = require('child_process');

const edgePath = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
const port = 9225;

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

    const ws = new global.WebSocket(wsUrl);

    ws.onopen = () => {
      ws.send(JSON.stringify({ id: 1, method: 'Runtime.enable' }));
      ws.send(JSON.stringify({ id: 2, method: 'Log.enable' }));
      ws.send(JSON.stringify({ id: 3, method: 'Page.enable' }));
      ws.send(JSON.stringify({ id: 4, method: 'Page.navigate', params: { url: 'file:///c:/Users/Enrico/Desktop/Giada/the_irish_year.html' } }));
    };

    ws.onmessage = (event) => {
      const msg = JSON.parse(event.data);
      if (msg.id === 20) {
        console.log("EVAL RESULT:", JSON.stringify(msg.result, null, 2));
        ws.close();
        browser.kill();
        process.exit(0);
      } else if (msg.method === 'Runtime.consoleAPICalled') {
        console.log('BROWSER CONSOLE:', msg.params.type, msg.params.args.map(a => a.value || a.description || JSON.stringify(a)));
      } else if (msg.method === 'Runtime.exceptionThrown') {
        console.error('BROWSER UNCAUGHT EXCEPTION:', JSON.stringify(msg.params.exceptionDetails, null, 2));
      } else if (msg.method === 'Log.entryAdded') {
        console.log('BROWSER LOG:', msg.params.entry.level, msg.params.entry.text);
      }
    };

    setTimeout(() => {
      ws.send(JSON.stringify({
        id: 20,
        method: 'Runtime.evaluate',
        params: {
          expression: `({
            bodyHtml: document.body ? document.body.innerHTML.substring(0, 500) : 'NO_BODY',
            rootExists: !!document.getElementById('root'),
            reactLoaded: typeof React !== 'undefined',
            babelLoaded: typeof Babel !== 'undefined',
            title: document.title
          })`,
          returnByValue: true
        }
      }));
    }, 4000);

  } catch (err) {
    console.error("Error:", err);
    browser.kill();
  }
}, 1500);
