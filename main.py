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
	mn,_,mnLoc,_ = cv2.minMaxLoc(result)
	x,y = mnLoc
	print(x,y)
	subprocess.call(f"adb shell input touchscreen tap {x} {y}",shell=True)
	#trows,tcols = small_image.shape[:2]
	#cv2.rectangle(large_image, (x,y),(x+tcols,y+trows),(0,0,255),2)
	#cv2.imshow('output',large_image)
	#cv2.waitKey(0)
	print(time.time() - start)
