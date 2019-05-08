THIS IS A HIGHLY EXPERIMENTAL SCRIPT THAT YOU SHOULD NOT TRUST AND YOU USE IT AT YOUR OWN RISK! Read the known issues section to know about some of the risks and problems. Watch it at first at least to make sure it works properly before letting it run on its own.

TL;DR Using image text recognition, this script will automatically reroll item properties for you until they are the specific set you want.

Requirements:

- Python 3
- The mod "Reroll Improvements":	https://steamcommunity.com/sharedfiles/filedetails/?id=1487862316
- Google Tesseract:	https://github.com/tesseract-ocr/tesseract
	(Windows installer here: https://github.com/UB-Mannheim/tesseract/wiki )
Python libraries:
	- pillow
	- mss
	- pytesseract
	- pyautogui

How to use:

- Input the path to the tesseract exe in the script.
- Enter the names of the two properties you want. You can leave a property empty by just pressing enter if you only care about one specific property.
- Prepare the item to be rerolled in the game. Go into the reroll crafting menu and select the item so that all you still need to do is click the "Reroll Properties" button.
- When the script tells you to, you focus the game, and place the mouse over the reroll button (not click, just place).
- Then just wait until it's done. (I highly recommend keeping an eye on it to make sure it works for you! see known issues down below)

Known issues:
- If you want to abort the script, keep in mind the script will click every few seconds. So when you switch applications, it might click in places you did not intend to.
- To abort the script, you need to focus the script window.
- The script does not keep track of your materials and if you run out
- If the image recognition does not work properly, it might continue rerolling even if the desired properties appear and so make you lose all your crafting materials. Do some tests to be sure it works for you specifically!
- No support for specific percentages, only looks at the properties
- No support for item traits, or lower quality items with only one property

Known unknown issues:
- Might not work with resolutions other than 1080p. the coordinates for the screenshot area (given by top, left, width and height) are EXTREMELY SENSITIVE and the image recognition completely can easily completely break down for certain properties with minor changes. if you experience issues on a resolution other than 1080p, you can try enabling debug mode (set the debug_mode flag to True) and experimenting with the values, or hit me up and i'll take a look.
- Might not work on Linux or macOS, only tested on windows. I tried to include portable code but no guarantees whatsoever. I also don't know how to install tesseract on other operating systems.

Unknown unknown issues:
Again, this is highly experimental, and you should keep an eye on the script to make sure it works properly.