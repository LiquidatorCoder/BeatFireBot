import subprocess
subprocess.call("adb devices",shell=True)
import time
import cv2

method = cv2.TM_SQDIFF_NORMED
start = time.time()
for i in range(20):
	name = "screenshot"+str(time.time() - start)+".png"
	subprocess.call(f"adb shell screencap -p | perl -pe 's/\x0D\x0A/\x0A/g' > {name}",shell=True)
print(time.time() - start)
