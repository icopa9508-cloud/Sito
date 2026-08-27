const http = require('http');
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');

// 1. Create a local static file server
const server = http.createServer((req, res) => {
  const filePath = path.join('c:/Users/Enrico/Desktop/Giada', req.url === '/' ? 'the_irish_year.html' : req.url);
  console.log("Serving request:", req.url, "->", filePath);
  
  if (fs.existsSync(filePath) && fs.statSync(filePath).isFile()) {
    const ext = path.extname(filePath);
    let contentType = 'text/html';
    if (ext === '.js') contentType = 'application/javascript';
    if (ext === '.css') contentType = 'text/css';
    if (ext === '.jpg' || ext === '.jpeg') contentType = 'image/jpeg';
    if (ext === '.png') contentType = 'image/png';
    
    res.writeHead(200, { 'Content-Type': contentType });
    fs.createReadStream(filePath).pipe(res);
  } else {
    res.writeHead(404);
    res.end('Not Found');
  }
});

server.listen(8085, () => {
  console.log("Server listening on http://127.0.0.1:8085");
  
  // 2. Launch headless edge
  const edgePath = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
  const port = 9226;
  
  const browser = spawn(edgePath, [
    `--remote-debugging-port=${port}`,
    '--headless=new',
    '--disable-gpu',
    'http://127.0.0.1:8085/the_irish_year.html'
  ]);
  
  setTimeout(async () => {
    try {
      const listRes = await fetch(`http://127.0.0.1:${port}/json/list`);
      const pages = await listRes.json();
      console.log("Found pages:", pages.length);
      const page = pages.find(p => p.url.includes('8085')) || pages[0];
      const wsUrl = page.webSocketDebuggerUrl;
      console.log("Connecting to page:", page.url);
      
      const ws = new global.WebSocket(wsUrl);
      
      ws.onopen = () => {
        ws.send(JSON.stringify({ id: 1, method: 'Runtime.enable' }));
        ws.send(JSON.stringify({ id: 2, method: 'Log.enable' }));
        ws.send(JSON.stringify({ id: 3, method: 'Page.enable' }));
      };
      
      ws.onmessage = (event) => {
        const msg = JSON.parse(event.data);
        if (msg.id === 30) {
          console.log("PAGE STATE RESULT:", JSON.stringify(msg.result, null, 2));
          ws.close();
          browser.kill();
          server.close();
          process.exit(0);
        } else if (msg.method === 'Runtime.consoleAPICalled') {
          console.log('BROWSER CONSOLE [' + msg.params.type + ']:', msg.params.args.map(a => a.value || a.description || JSON.stringify(a)));
        } else if (msg.method === 'Runtime.exceptionThrown') {
          console.error('BROWSER UNCAUGHT EXCEPTION:', JSON.stringify(msg.params.exceptionDetails, null, 2));
        } else if (msg.method === 'Log.entryAdded') {
          console.log('BROWSER LOG:', msg.params.entry.level, msg.params.entry.text);
        }
      };
      
      setTimeout(() => {
        console.log("Evaluating page state after 4.5s (loading should have finished at 1.8s)...");
        ws.send(JSON.stringify({
          id: 30,
          method: 'Runtime.evaluate',
          params: {
            expression: `({
              title: document.title,
              rootExists: !!document.getElementById('root'),
              rootChildrenCount: document.getElementById('root') ? document.getElementById('root').children.length : 0,
              rootHtmlSnippet: document.getElementById('root') ? document.getElementById('root').innerHTML.substring(0, 300) : 'NO_ROOT',
              hasCustomCursor: !!document.querySelector('.custom-cursor'),
              sectionsFound: document.querySelectorAll('section').length
            })`,
            returnByValue: true
          }
        }));
      }, 4500);
      
    } catch (err) {
      console.error("Error:", err);
      browser.kill();
      server.close();
    }
  }, 2000);
});
