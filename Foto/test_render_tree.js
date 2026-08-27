// Test full React rendering of IrishYearExperience with window.location
const fs = require('fs');

async function testFullRender() {
  const html = fs.readFileSync('c:/Users/Enrico/Desktop/Giada/the_irish_year.html', 'utf8');
  const scriptContent = html.split('<script type="text/babel">')[1].split('</script>')[0];
  
  console.log("Fetching Babel standalone & React...");
  const [babelRes, reactRes, reactDomRes, reactDomServerRes] = await Promise.all([
    fetch("https://unpkg.com/@babel/standalone@7.24.0/babel.min.js").then(r => r.text()),
    fetch("https://unpkg.com/react@18/umd/react.development.js").then(r => r.text()),
    fetch("https://unpkg.com/react-dom@18/umd/react-dom.development.js").then(r => r.text()),
    fetch("https://unpkg.com/react-dom@18/umd/react-dom-server.browser.development.js").then(r => r.text())
  ]);
  
  function createFakeNode(tagName = 'div') {
    const attrs = {};
    return {
      nodeType: 1,
      tagName: tagName.toUpperCase(),
      nodeName: tagName.toUpperCase(),
      innerHTML: '',
      style: {},
      attributes: attrs,
      setAttribute: (k, v) => { attrs[k] = v; },
      getAttribute: (k) => attrs[k] || null,
      removeAttribute: (k) => { delete attrs[k]; },
      addEventListener: () => {},
      removeEventListener: () => {},
      appendChild: (c) => c,
      removeChild: (c) => c,
      ownerDocument: null,
      childNodes: []
    };
  }

  const vm = require('vm');
  const context = {
    window: {
      addEventListener: () => {},
      removeEventListener: () => {},
      scrollTo: () => {},
      innerHeight: 900,
      innerWidth: 1400,
      navigator: { userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36' },
      location: { protocol: 'file:', href: 'file:///c:/Users/Enrico/Desktop/Giada/the_irish_year.html' }
    },
    document: {
      getElementById: (id) => createFakeNode('div'),
      createElement: (tag) => createFakeNode(tag),
      createElementNS: (ns, tag) => createFakeNode(tag),
      createTextNode: (txt) => ({ nodeType: 3, textContent: txt }),
      addEventListener: () => {},
      removeEventListener: () => {},
      body: createFakeNode('body'),
      location: { protocol: 'file:', href: 'file:///c:/Users/Enrico/Desktop/Giada/the_irish_year.html' }
    },
    location: { protocol: 'file:', href: 'file:///c:/Users/Enrico/Desktop/Giada/the_irish_year.html' },
    navigator: { userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36' },
    console: console,
    setTimeout: (fn, ms) => setTimeout(fn, ms),
    clearTimeout: () => {},
    setInterval: (fn, ms) => setInterval(fn, ms),
    clearInterval: () => {},
    TextEncoder: global.TextEncoder,
    TextDecoder: global.TextDecoder
  };
  context.window.document = context.document;
  context.window.window = context.window;
  context.window.global = context.window;
  context.window.TextEncoder = global.TextEncoder;
  context.window.TextDecoder = global.TextDecoder;
  context.document.body.ownerDocument = context.document;
  
  vm.createContext(context);
  
  vm.runInContext(reactRes, context);
  vm.runInContext(reactDomRes, context);
  vm.runInContext(reactDomServerRes, context);
  vm.runInContext(babelRes, context);
  
  console.log("Compiling app script...");
  const output = context.Babel.transform(scriptContent, {
    presets: ['react', 'env']
  });
  
  console.log("Executing compiled script...");
  vm.runInContext(output.code, context);
  
  console.log("Testing IrishYearExperience render with loading=false...");
  
  const testRenderScript = `
    const { createElement } = React;
    const { renderToString } = ReactDOMServer;
    
    try {
      // Modify useState temporarily to return loading=false
      const origUseState = React.useState;
      let hookCallCount = 0;
      React.useState = function(initial) {
        hookCallCount++;
        // The first hook in IrishYearExperience is loading
        if (hookCallCount === 1) {
          return [false, () => {}]; // Force loading = false
        }
        return origUseState(initial);
      };
      
      console.log("Rendering full IrishYearExperience (all 13 sections!)...");
      const el = createElement(IrishYearExperience);
      const htmlStr = renderToString(el);
      console.log("SUCCESS! Fully rendered page HTML length:", htmlStr.length);
      
    } catch (err) {
      console.error("REACT RENDER ERROR (loading=false):", err.stack || err);
    }
  `;
  
  vm.runInContext(testRenderScript, context);
}

testFullRender();
