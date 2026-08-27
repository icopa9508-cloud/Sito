with open(r'c:\Users\Enrico\Desktop\Giada\the_irish_year.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "HOVER TO REVEAL PHOTO" in line.upper():
        print(f"Line {i+1}: {line.strip()}")
