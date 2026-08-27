import zipfile
import xml.etree.ElementTree as ET
import os

doc_path = r'c:\Users\Enrico\Desktop\Giada\sito.docx'

with zipfile.ZipFile(doc_path, 'r') as z:
    # List all files in the docx
    file_list = z.namelist()
    media_files = [f for f in file_list if f.startswith('word/media/')]
    print(f"Total media files in sito.docx: {len(media_files)}")
    
    xml_content = z.read('word/document.xml')
    rels_content = z.read('word/_rels/document.xml.rels')

# Parse rels to map r:embed IDs to image filenames
rels_tree = ET.fromstring(rels_content)
rel_map = {}
for rel in rels_tree:
    r_id = rel.attrib.get('Id')
    target = rel.attrib.get('Target')
    if target and 'media/' in target:
        rel_map[r_id] = os.path.basename(target)

print(f"Total rels mapped: {len(rel_map)}")

# Now let's traverse the document paragraphs and find references to images and section titles
tree = ET.fromstring(xml_content)
namespaces = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
}

items = []
for p in tree.iterfind('.//w:p', namespaces):
    # get text
    texts = [node.text for node in p.iterfind('.//w:t', namespaces) if node.text]
    full_text = "".join(texts).strip()
    
    # get image embeds
    img_ids = []
    for blip in p.iterfind('.//a:blip', namespaces):
        embed_id = blip.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
        if embed_id and embed_id in rel_map:
            img_ids.append(rel_map[embed_id])
            
    if full_text or img_ids:
        items.append({'text': full_text, 'images': img_ids})

print(f"Total structured items found: {len(items)}")

for i, it in enumerate(items):
    if it['text'] or it['images']:
        print(f"[{i+1}] TEXT: {it['text'][:80]} | IMGS: {it['images']}")
