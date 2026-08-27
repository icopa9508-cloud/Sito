# Let's inspect the target location in the_irish_year.html to add the Concept Map database and component.

with open(r'c:\Users\Enrico\Desktop\Giada\the_irish_year.html', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Total characters: {len(content)}")
print(f"Contains IRELAND_SUBJECTS: {'IRELAND_SUBJECTS' in content}")
print(f"Contains modalSubject: {'modalSubject' in content}")
