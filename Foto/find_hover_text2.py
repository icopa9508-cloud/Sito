with open(r'c:\Users\Enrico\Desktop\Giada\the_irish_year.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open(r'c:\Users\Enrico\Desktop\Giada\Foto\hover_results.txt', 'w', encoding='utf-8') as out:
    for i, line in enumerate(lines):
        if "HOVER TO REVEAL PHOTO" in line.upper():
            out.write(f"Line {i+1}: {line.strip()}\n")
