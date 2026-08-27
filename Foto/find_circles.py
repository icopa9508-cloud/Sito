with open(r'c:\Users\Enrico\Desktop\Giada\the_irish_year.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'animate-ping' in line or 'animate-pulse' in line or 'keyword-side-drawer' in line or 'MAP_LOCATIONS' in line or 'TopicConceptMapModal' in line:
        print(f"Line {i+1}: {line.strip()}")
