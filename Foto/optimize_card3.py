from PIL import Image

img_path = r'c:\Users\Enrico\Desktop\Giada\Foto\section_03_arrival.png'
img = Image.open(img_path)
print("Image format:", img.format, "Size:", img.size, "Mode:", img.mode)

# Let's also save an optimized jpg version for fast loading if needed
rgb_img = img.convert('RGB')
jpg_path = r'c:\Users\Enrico\Desktop\Giada\Foto\section_03_arrival.jpg'
rgb_img.save(jpg_path, 'JPEG', quality=92, optimize=True)
print("Saved optimized JPEG to:", jpg_path)
