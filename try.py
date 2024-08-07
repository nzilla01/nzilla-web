from PIL import Image, ImageDraw, ImageFont

# Create a blank image with white background
image = Image.new('RGB', (800, 600), color=(255, 255, 255))

# Load the fonts
font_lobster_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Placeholder
font_raleway_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Placeholder
font_roboto_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"   # Placeholder
font_montserrat_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Placeholder

# Load the actual font paths if available in your system
try:
    font_lobster = ImageFont.truetype("Lobster-Regular.ttf", 60)
    font_raleway = ImageFont.truetype("Raleway-Regular.ttf", 60)
    font_roboto = ImageFont.truetype("Roboto-Regular.ttf", 60)
    font_montserrat = ImageFont.truetype("Montserrat-Regular.ttf", 60)
except IOError:
    font_lobster = ImageFont.truetype(font_lobster_path, 60)
    font_raleway = ImageFont.truetype(font_raleway_path, 60)
    font_roboto = ImageFont.truetype(font_roboto_path, 60)
    font_montserrat = ImageFont.truetype(font_montserrat_path, 60)

# Initialize ImageDraw
draw = ImageDraw.Draw(image)

# Add the app name with different fonts
y_offset = 50
draw.text((50, y_offset), "FinScope (Lobster)", font=font_lobster, fill=(0, 0, 0))
y_offset += 100
draw.text((50, y_offset), "FinScope (Raleway)", font=font_raleway, fill=(0, 0, 0))
y_offset += 100
draw.text((50, y_offset), "FinScope (Roboto)", font=font_roboto, fill=(0, 0, 0))
y_offset += 100
draw.text((50, y_offset), "FinScope (Montserrat)", font=font_montserrat, fill=(0, 0, 0))

# Save the image
image_path = "/mnt/data/finscope_font_comparison.png"
image.save(image_path)
image_path
