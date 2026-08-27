import zipfile
import xml.etree.ElementTree as ET

doc_path = r'c:\Users\Enrico\Desktop\Giada\BUSINESS.docx'
out_path = r'c:\Users\Enrico\Desktop\Giada\Foto\dump_business_docx.txt'

with zipfile.ZipFile(doc_path, 'r') as z:
    xml_content = z.read('word/document.xml')
    tree = ET.fromstring(xml_content)
    
    namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    paragraphs = []
    for p in tree.iterfind('.//w:p', namespaces):
        texts = [node.text for node in p.iterfind('.//w:t', namespaces) if node.text]
        if texts:
            paragraphs.append("".join(texts))

with open(out_path, 'w', encoding='utf-8') as f:
    for i, p in enumerate(paragraphs):
        f.write(f"[{i+1}] {p}\n")

print(f"Dumped {len(paragraphs)} paragraphs to {out_path}")
