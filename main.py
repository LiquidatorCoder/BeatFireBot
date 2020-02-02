import subprocess
subprocess.call("adb devices",shell=True)
import time
import cv2

method = cv2.TM_SQDIFF_NORMED
start = time.time()
for i in range(1):
	subprocess.call("adb shell screencap -p | perl -pe 's/\x0D\x0A/\x0A/g' > screenshot.png",shell=True)
print(time.time() - start)
