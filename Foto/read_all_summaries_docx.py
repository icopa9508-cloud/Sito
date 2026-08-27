import zipfile
import xml.etree.ElementTree as ET

doc_path = r'c:\Users\Enrico\Desktop\Giada\Riassunti_Completi_Tutte_Materie.docx'

with zipfile.ZipFile(doc_path, 'r') as z:
    xml_content = z.read('word/document.xml')
    tree = ET.fromstring(xml_content)
    
    namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    paragraphs = []
    for p in tree.iterfind('.//w:p', namespaces):
        texts = [node.text for node in p.iterfind('.//w:t', namespaces) if node.text]
        if texts:
            paragraphs.append("".join(texts))

    print(f"Total paragraphs found: {len(paragraphs)}\n")
    for i, p in enumerate(paragraphs):
        print(f"[{i+1}] {p}\n")
