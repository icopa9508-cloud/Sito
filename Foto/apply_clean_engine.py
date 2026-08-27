# Script to update the_irish_year.html cleanly using exact string split/join

with open(r'c:\Users\Enrico\Desktop\Giada\the_irish_year.html', 'r', encoding='utf-8') as f:
    code = f.read()

# Load the replacement text directly
with open(r'c:\Users\Enrico\Desktop\Giada\Foto\update_concept_engine.py', 'r', encoding='utf-8') as f:
    script_content = f.read()

# Extract new_concept_engine
start_str = 'new_concept_engine = """'
end_str = '"""\n\n# Replace the old section'

engine_code = script_content.split(start_str)[1].split(end_str)[0]

old_start_marker = "    // ============================================================================\n    // RICH CONCEPT MAPS & GENERATED VISUAL SCHEMATICS (SECTION 07)"
old_end_marker = "    // ============================================================================\n    // 3. MAIN COMPONENT ARCHITECTURE & SECTIONS\n    // ============================================================================"

if old_start_marker in code and old_end_marker in code:
    before = code.split(old_start_marker)[0]
    after = code.split(old_end_marker)[1]
    new_html = before + engine_code.strip() + "\n\n" + old_end_marker + after
    with open(r'c:\Users\Enrico\Desktop\Giada\the_irish_year.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Replaced concept map engine successfully and saved!")
else:
    print("Error: Markers not found!")
