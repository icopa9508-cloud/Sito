# Script to inspect the javascript in the_irish_year.html for syntax errors and unescaped characters
with open(r'c:\Users\Enrico\Desktop\Giada\the_irish_year.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract script tag content
start_tag = '<script type="text/babel">'
end_tag = '</script>'

if start_tag in html and end_tag in html:
    script_part = html.split(start_tag)[1].split(end_tag)[0]
    print(f"Script length: {len(script_part)} characters, {len(script_part.splitlines())} lines")
    
    # Check for unescaped backslashes, bad quotes, syntax errors
    # Let's save script_part to a separate file to test with node if available or test with python
    with open(r'c:\Users\Enrico\Desktop\Giada\Foto\app_script.js', 'w', encoding='utf-8') as f:
        f.write(script_part)
else:
    print("Script tags not found!")
