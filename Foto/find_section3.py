with open(r'c:\Users\Enrico\Desktop\Giada\the_irish_year.html', 'r', encoding='utf-8') as f:
    code = f.read()

# Search for section 3
import re
match = re.search(r'(03\s*—.*?</section>)', code, re.DOTALL)
if match:
    print("Found Section 03:")
    print(match.group(1)[:1500])
else:
    print("Section 03 header not found, let's search for 03")
    for line in code.splitlines():
        if "03" in line and ("section" in line.lower() or "FAMILY" in line or "HOST" in line or "HOUSE" in line):
            print(line)
