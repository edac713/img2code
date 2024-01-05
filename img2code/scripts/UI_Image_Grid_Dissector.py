from PIL import Image

# Define the paths for the input images
original_ui_image_path = '/mnt/data/Original UI Image.png'
ui_image_overlay_path = '/mnt/data/UI Image Overlay.png'

# Load the images
original_ui_image = Image.open(original_ui_image_path)
ui_image_overlay = Image.open(ui_image_overlay_path)

# Resize the "Original UI Image" to (954 x 1892 px)
original_ui_image_resized = original_ui_image.resize((954, 1892))

# Resize the "UI Image Overlay" to (1566 x 2345 px)
ui_image_overlay_resized = ui_image_overlay.resize((1566, 2345))

# Create a blank background with dimensions (1566 x 2345 px)
background = Image.new('RGB', (1566, 2345), color = (255, 255, 255))

# Overlay the "Original UI Image" centered horizontally and vertically on the background
bg_w, bg_h = background.size
img_w, img_h = original_ui_image_resized.size
offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
background.paste(original_ui_image_resized, offset)

# Overlay the "UI Image Overlay" on top of the background, centered as well
# The "UI Image Overlay" is the same size as the background so it will be centered by default
background.paste(ui_image_overlay_resized, (0, 0), ui_image_overlay_resized)

# Save the overlayed images as a single image file called "Processed UI Image"
processed_ui_image_path = '/mnt/data/Processed UI Image.png'
background.save(processed_ui_image_path)

# Display the processed image
background.show()

# Output the path to the saved image (e.g., for download links)
print(processed_ui_image_path)