// Download babel standalone and test-compile the script
const fs = require('fs');

async function testCompile() {
  const html = fs.readFileSync('c:/Users/Enrico/Desktop/Giada/the_irish_year.html', 'utf8');
  const scriptContent = html.split('<script type="text/babel">')[1].split('</script>')[0];
  
  console.log("Fetching Babel standalone...");
  const res = await fetch("https://unpkg.com/@babel/standalone@7.24.0/babel.min.js");
  const babelCode = await res.text();
  
  console.log("Evaluating Babel...");
  // create sandbox
  const vm = require('vm');
  const context = { window: {}, console: console };
  vm.createContext(context);
  vm.runInContext(babelCode, context);
  
  const Babel = context.Babel || context.window.Babel;
  console.log("Babel loaded! Compiling React script...");
  
  try {
    const output = Babel.transform(scriptContent, {
      presets: ['react', 'env']
    });
    console.log("SUCCESS! Script compiled without any syntax error!");
    
    // Now let's test running the compiled JS in a mock React environment to see if a runtime exception is thrown at startup
    console.log("Testing runtime execution...");
    const runtimeContext = {
      React: {
        useState: (init) => [init, () => {}],
        useEffect: (fn) => {},
        useRef: (init) => ({ current: init }),
        useMemo: (fn) => fn(),
        useCallback: (fn) => fn,
        createContext: () => ({ Provider: () => {}, Consumer: () => {} }),
        createElement: () => ({})
      },
      ReactDOM: {
        createRoot: () => ({ render: () => {} })
      },
      document: {
        getElementById: () => ({ innerHTML: '' }),
        addEventListener: () => {},
        removeEventListener: () => {}
      },
      window: {
        addEventListener: () => {},
        removeEventListener: () => {},
        scrollTo: () => {}
      },
      console: console,
      LucideIcons: new Proxy({}, { get: () => () => ({}) })
    };
    
    vm.createContext(runtimeContext);
    vm.runInContext(output.code, runtimeContext);
    console.log("SUCCESS! Runtime execution completed without throwing any error!");
  } catch (err) {
    console.error("COMPILE OR RUNTIME ERROR:", err);
  }
}

testCompile();
