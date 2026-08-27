import zipfile
import os

doc_path = r'c:\Users\Enrico\Desktop\Giada\sito.docx'
out_dir = r'c:\Users\Enrico\Desktop\Giada\Foto'

with zipfile.ZipFile(doc_path, 'r') as z:
    for filename in z.namelist():
        if 'image37.' in filename:
            print("Found image file in docx:", filename)
            data = z.read(filename)
            ext = os.path.splitext(filename)[1]
            out_file = os.path.join(out_dir, f"section_03_arrival{ext}")
            with open(out_file, 'wb') as f:
                f.write(data)
            print(f"Extracted to {out_file}, size: {len(data)} bytes")
