import sys
import mss
import mss.tools
import time
import pyautogui
import os

debug_mode = False			# set this to True if you experience issues and want to look at the screenshots the script creates (which normally get deleted again right away after being processed). will also disable clicking.

if debug_mode:
	print("Debug mode active")

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

print("THIS IS A HIGHLY EXPERIMENTAL SCRIPT!\nIf you haven't read the readme yet, do it now.")


screenWidth, screenHeight = pyautogui.size()				# get screen resolution

top = 600
left = 720
height = 52
width = 470

#detects most properties, except crit chance: (also turned out not enough for longer names like "damage reduction vs area damage")
#top = 598
#left = 800
#height = 54
#width = 310

def clickhold(s):											# since you need to hold down the mouse a bit to reroll stats
	pyautogui.mouseDown()
	time.sleep(s)
	pyautogui.mouseUp()

def make_screenshot(top, left, height, width, name):
	with mss.mss() as sct:
		monitor = {"top": int(screenHeight/1080*top), "left": int(screenWidth/1920*left), "width": int(screenWidth/1920*width), "height": int(screenHeight/1080*height)}
		output = name.format(**monitor)

		# Grab the data
		sct_img = sct.grab(monitor)
		
		# Save to the picture file
		mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
		#print(output)

# load the saved path for the tesseract exe, if it exists. otherwise, ask for path
try:
	with open("tesseract_path.txt", "r") as fsource:
		tesseract_path = fsource.read()
		answer = None
		while answer == None:
			print("Use the saved path? y/n")
			answer = input()
			if answer == 'n':
				tesseract_path = None
			elif answer == 'y':
				continue
			else:
				answer = None
			
except:
	pass
	tesseract_path = None

if tesseract_path == None:
	print("Please enter the full path to the tesseract exe (For example: c:/program files/tesseract-OCR/tesseract.exe): ")
	tesseract_path = input()
	print("Save path? y/n")
	if input() == 'y':
		with open("tesseract_path.txt", "w") as ftarget:
			ftarget.write(tesseract_path)

print("Please enter the name of the first property. Be careful to enter it EXACTLY as it is displayed in the game! (For example: \"Attack Speed\" (without the \"), or \"Push/Block Angle\"): ")
property_one = input().lower()
print("Please enter the name of the second property now: ")
property_two = input().lower()


print("Prepare the item to be rerolled now. Go to the reroll tab in the crafting menu, and select the item you want to reroll. Make sure you have the mod \"Reroll Improvements\" installed so you now can see the properties of the item without having to mouse over it!")
print("Press enter when you have done that and are ready to continue.")
input()

wait_time = 10
print("Please focus the game window now and point the mouse over the reroll button (only point, without clicking). The script will start rerolling in " + str(wait_time) + " seconds. Switch to this window and press CTRL+C to abort.")
time.sleep(wait_time)


prop_one_rolled = False
prop_two_rolled = False


while not (prop_one_rolled and prop_two_rolled):
	prop_one_rolled = False
	prop_two_rolled = False
	
	infile1 = "sct_1.png"
	infile2 = "sct_2.png"
	
	make_screenshot(top, left, height/2, width, infile1)
	make_screenshot(top+height/2, left, height/2, width, infile2)

	try:
		pytesseract.pytesseract.tesseract_cmd = tesseract_path
	except:
		print("Error calling tesseract. Please check if you entered the path to the tesseract exe correctly.")
		break

	while True:
		try:
			test_file = open(infile1, 'r')
			test_file.close()
			test_file = open(infile2, 'r')
			test_file.close()
			break
		except:
			pass
		time.sleep(0.1)			# wait in 0.1s increments until screenshot file has been saved, in case it takes a bit
		print("Waiting for image files to be saved...")

	s = pytesseract.image_to_string(Image.open(infile1)).lower() + "\n" + pytesseract.image_to_string(Image.open(infile2)).lower()
	print(s + "\n")
	if not debug_mode:
		os.remove(infile1)
		os.remove(infile2)

	if property_one in s:
		prop_one_rolled = True
		print("contains " + property_one)
		
	if property_two in s:
		prop_two_rolled = True
		print("contains " + property_two)
		
		
	if not (prop_one_rolled and prop_two_rolled):
		if not debug_mode:
			clickhold(0.1)
		time.sleep(2.4)

print("Done! Press Enter to exit.")
input()
