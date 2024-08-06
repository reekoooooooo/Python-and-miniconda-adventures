from PIL import Image
import os

def resize_image(file_path, width, output_directory):
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # Open and resize the image
    img = Image.open(file_path)
    w_percent = (width / float(img.size[0]))
    h_size = int((float(img.size[1]) * float(w_percent)))
    img = img.resize((width, h_size), Image.LANCZOS)
    
    # Save the resized image to the output directory
    new_file_path = os.path.join(output_directory, 'resized_' + os.path.basename(file_path))
    img.save(new_file_path)
    print(f"Image resized and saved to {new_file_path}")

def resize_images(directory, width, output_directory):
    for filename in os.listdir(directory):
        if filename.endswith(('.jpg', '.png', '.jpeg')):
            file_path = os.path.join(directory, filename)
            resize_image(file_path, width, output_directory)
    print("All images resized successfully.")

# Usage for a single image
resize_image(r'C:\Users\tyrek\OneDrive\Pictures\polaroid\DCIM\PICT0000 - Copy.jpg', 800, r'C:\Users\tyrek\OneDrive\Pictures\polaroid\Resized')

# Usage for all images in a directory
resize_images(r'C:\Users\tyrek\OneDrive\Pictures\polaroid\DCIM', 800, r'C:\Users\tyrek\OneDrive\Pictures\polaroid\Resized')
