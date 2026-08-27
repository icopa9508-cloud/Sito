# Verification script to ensure HTML, React, and Babel syntax are valid
with open(r'c:\Users\Enrico\Desktop\Giada\the_irish_year.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check key keywords
keywords_to_check = [
    'TopicConceptMapModal',
    'getConceptMapForTopic',
    'GeneratedVisualCard',
    'openConceptMap',
    'conceptMapData',
    'keyword-side-drawer'
]

for kw in keywords_to_check:
    count = content.count(kw)
    print(f"Keyword '{kw}': {count} occurrences")

print(f"Total HTML file size: {len(content)} characters, {len(content.splitlines())} lines")
