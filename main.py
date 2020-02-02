import subprocess
subprocess.call("adb devices",shell=True)
subprocess.call("adb shell screencap -p /sdcard/screenshot.png",shell=True)
subprocess.call("adb pull /sdcard/screenshot.png",shell=True)
subprocess.call("adb shell rm /sdcard/screenshot.png",shell=True)
