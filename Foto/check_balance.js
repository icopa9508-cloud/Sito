// Check if @babel/standalone or babel is in npm, or fetch @babel/standalone to run in node
const fs = require('fs');

const html = fs.readFileSync('c:/Users/Enrico/Desktop/Giada/the_irish_year.html', 'utf8');
const scriptContent = html.split('<script type="text/babel">')[1].split('</script>')[0];

console.log("Read script content, length:", scriptContent.length);

// Let's check for basic JS/JSX syntax issues
// Let's see if we can transform it using in-memory babel or check unmatched brackets/parentheses/quotes
let openBraces = 0, openParens = 0, openBrackets = 0;
let inString = null, isEscaped = false;

for (let i = 0; i < scriptContent.length; i++) {
  const ch = scriptContent[i];
  const prev = i > 0 ? scriptContent[i-1] : '';
  
  if (inString) {
    if (ch === inString && !isEscaped) {
      inString = null;
    } else if (ch === '\\' && !isEscaped) {
      isEscaped = true;
      continue;
    }
    isEscaped = false;
  } else {
    if (ch === '"' || ch === "'" || ch === '`') {
      inString = ch;
    } else if (ch === '{') openBraces++;
    else if (ch === '}') openBraces--;
    else if (ch === '(') openParens++;
    else if (ch === ')') openParens--;
    else if (ch === '[') openBrackets++;
    else if (ch === ']') openBrackets--;
  }
}

console.log(`Braces balance: ${openBraces}, Parens balance: ${openParens}, Brackets balance: ${openBrackets}, inString: ${inString}`);
