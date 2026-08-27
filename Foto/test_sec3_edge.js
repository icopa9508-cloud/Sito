const http = require('http');
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');

const server = http.createServer((req, res) => {
  const filePath = path.join('c:/Users/Enrico/Desktop/Giada', req.url === '/' ? 'the_irish_year.html' : req.url);
  
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

server.listen(8086, () => {
  const edgePath = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
  const port = 9227;
  
  const browser = spawn(edgePath, [
    `--remote-debugging-port=${port}`,
    '--headless=new',
    '--disable-gpu',
    'http://127.0.0.1:8086/the_irish_year.html'
  ]);
  
  setTimeout(async () => {
    try {
      const listRes = await fetch(`http://127.0.0.1:${port}/json/list`);
      const pages = await listRes.json();
      const page = pages.find(p => p.url.includes('8086')) || pages[0];
      const wsUrl = page.webSocketDebuggerUrl;
      
      const ws = new global.WebSocket(wsUrl);
      
      ws.onopen = () => {
        ws.send(JSON.stringify({ id: 1, method: 'Runtime.enable' }));
        ws.send(JSON.stringify({ id: 2, method: 'Log.enable' }));
        ws.send(JSON.stringify({ id: 3, method: 'Page.enable' }));
      };
      
      ws.onmessage = (event) => {
        const msg = JSON.parse(event.data);
        if (msg.id === 30) {
          console.log("FINAL PAGE STATE:", JSON.stringify(msg.result, null, 2));
          ws.close();
          browser.kill();
          server.close();
          process.exit(0);
        } else if (msg.method === 'Runtime.consoleAPICalled') {
          console.log('BROWSER CONSOLE [' + msg.params.type + ']:', msg.params.args.map(a => a.value || a.description));
        } else if (msg.method === 'Runtime.exceptionThrown') {
          console.error('BROWSER UNCAUGHT EXCEPTION:', JSON.stringify(msg.params.exceptionDetails, null, 2));
        }
      };
      
      setTimeout(() => {
        ws.send(JSON.stringify({
          id: 30,
          method: 'Runtime.evaluate',
          params: {
            expression: `({
              title: document.title,
              rootExists: !!document.getElementById('root'),
              sectionsFound: document.querySelectorAll('section').length,
              section03ImgSrc: document.querySelector('img[alt="Arrival in Ireland"]') ? document.querySelector('img[alt="Arrival in Ireland"]').src : 'NOT_FOUND'
            })`,
            returnByValue: true
          }
        }));
      }, 5500);
      
    } catch (err) {
      console.error("Error:", err);
      browser.kill();
      server.close();
    }
  }, 2000);
});
