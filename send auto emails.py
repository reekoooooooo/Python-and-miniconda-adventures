from PIL import Image
import os

def resize_image(file_path, width):
    img = Image.open(file_path)
    w_percent = (width / float(img.size[0]))
    h_size = int((float(img.size[1]) * float(w_percent)))
    img = img.resize((width, h_size), Image.LANCZOS)
    new_file_path = os.path.join(os.path.dirname(file_path), 'resized_' + os.path.basename(file_path))
    img.save(new_file_path)
    print(f"Image resized and saved to {new_file_path}")

def resize_images(directory, width):
    for filename in os.listdir(directory):
        if filename.endswith(('.jpg', '.png', '.jpeg')):
            file_path = os.path.join(directory, filename)
            resize_image(file_path, width)
    print("All images resized successfully.")

# Usage for a single image
resize_image(r'C:\Users\tyrek\OneDrive\Pictures\polaroid\DCIM\PICT0000 - Copy.jpg', 800)











