from PIL import Image

# path of image file
image1 = Image.open("path of image file.png")

im1 = image1.convert("RGB")

# path were pdf file will be saved
im1.save("pdf file name with .pdf extension")