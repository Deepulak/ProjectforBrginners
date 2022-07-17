# pip install numpy
# pip install pyautogui
# pip install opencv-python

import pyautogui
import cv2
import numpy as np

# Specify Resolution
resolution = (1920, 1080)
# specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")
# specify name of outputfile
filename = "Recording.avi"
# specify frames rate. We can choose any
# value and experiment with it
fps = 60.0
# Creating video writer object
out = cv2.VideoWriter(filename, codec, fps, resolution)
# create an empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
# Resize the window
cv2.resizeWindow("Live", 480, 270)
while True:
	# Take screenshot using PyAutoGui
	img = pyautogui.screenshot()
	# Convert the screenshot to a numpy array
	frame = np.array(img)
	# Convert it from BGR(Blue, Green, Red) to
	# RGB(Red, Green, Blue)
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	# Write it to the output file
	out.write(frame)
	# Optional: Display the recording screen
	cv2.imshow("Live", frame)
	# Stop recording when we press "q"
	if cv2.waitKey(1) == ord("q"):
		break

# Release the video writer
out.release()
# Destroy all windows
cv2.destroyAllWindows()