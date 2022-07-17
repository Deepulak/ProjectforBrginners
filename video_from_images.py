# importing libraies
import os
import cv2
from PIL import Image

# Checking the current directory path
print(os.getcwd())

# Folder which contaions all the image 
# from which video is to be generated
os.chdir("image folder path")
path = "image folder path"

mean_height = 0
mean_width = 0

num_of_images = len(os.listdir("."))
# print(num_of_images)

for file in os.listdir("."):
	im = Image.open(os.path.join(path, file))
	width, height = im.size
	mean_width = width
	mean_height = height
	# is.show() 	# uncomment this for displaying the image

# Finding the mean height and width of all images.
# This is required beacause the video frame needs.
# to be set with same width and height. Otherwise
# images not equal to that width height will not get
# enbedded into the video 

mean_width = int(mean_width / num_of_images)
mean_height = int(mean_height / num_of_images)

# print(mean_height)
# print(mean_width)

# Resizing of the images to give
# them same width and height
for file in os.listdir("."):
	if file.endswith("jpg") or file.endswith("jpeg") or file.endswith("png"):
		# Opening image using pil image
		im = Image.open(os.path.join(path, file))

		# im.size()  includes the height and width of image
		width, height = im.size
		print(width, height)

		# resizing 
		imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
		imResize.save(file, "JPEG", quality=95)
		# setting quality
		# printing each resized image name
		print(im.filename.split("\\")[-1], "is resized")

# Video Generating function
def generate_video():
	image_folder = "."	# make suren to use your folder
	video_name = "video.avi"
	os.chdir("path the file or folder previously get")
	images = [img for img in os.listdir(image_folder) if img.endswith("jpg") or img.endswith(".jpeg") or img.endswith(".png")]

	# Array images should only consider
	# the image files ignoring other if any
	print(images)

	frame = cv2.imreads(os.path.join(image_folder, image[0]))

	# setting the frame width, height width
	# the width, height of first image
	height, width, layers = frame.shape

	video = cv2.VideoWriter(video_name, 0, 1, (width, height))

	# Appending the images to the video one by one
	for image in images:
		video.write(cv2.imread(os.path.join(image_folder, image)))

	cv2.destroyAllWindows()
	video.release()

# Calling the generate_video function
generate_video()