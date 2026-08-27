# Let's inspect all subjects and their topics in the_irish_year.html

with open(r'c:\Users\Enrico\Desktop\Giada\the_irish_year.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

print("Inspecting topics in the_irish_year.html...")
