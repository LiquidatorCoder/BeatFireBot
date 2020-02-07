import subprocess
import time
import cv2

subprocess.call("adb devices",shell=True)
method = cv2.TM_SQDIFF_NORMED

for i in range(10):
	start = time.time()
	small_image = cv2.imread('TEST SS/small_dark_blue.png')
	#cv2.imshow("image",small_image)
	#cv2.waitKey(0)
	subprocess.call("adb shell screencap -p | perl -pe 's/\x0D\x0A/\x0A/g' > screenshot.png",shell=True)
	large_image = cv2.imread('screenshot.png')
	result = cv2.matchTemplate(small_image, large_image, method)
	# We want the minimum squared difference
	mn,_,mnLoc,_ = cv2.minMaxLoc(result)

	# Draw the rectangle:
	# Extract the coordinates of our best match
	MPx,MPy = mnLoc

	# Step 2: Get the size of the template. This is the same size as the match.
	trows,tcols = small_image.shape[:2]

	# Step 3: Draw the rectangle on large_image
	cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

	# Display the original image with the rectangle around the match.
	cv2.imshow('output',large_image)

	# The image is only displayed if we call this
	cv2.waitKey(0)
	print(time.time() - start)
