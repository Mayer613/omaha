from PIL import Image, ImageDraw, ImageFont
import os
import glob
import json
import subprocess
import imagehash
import string
import sys

white = (255, 255, 255)

# Creates png image files for each character in the font
def textToImage(fontName, fontSize):
	font = ImageFont.truetype(fontName , fontSize)
	#letters = string.ascii_uppercase
	letters = '0123456789'
	for letter in letters:
		image = Image.new("RGB", (200, 120), white)
		draw = ImageDraw.Draw(image)
		draw.text((0, 0), letter, fill='black', font=font) #--- risovanie
		filename = "characters/" + letter + ".png"
		image.save(filename, "png")

def generatePixelMatrix(fontName, fontSize):
	global fDict 
	global Sym_Hash
	global COLLISION
	global DOBLE
	global TOTAL
	letters = '0123456789'
	for letter in letters:
		image = Image.open("characters/" + letter + ".png")
		rgbImage = image.convert("RGB")
		matrix = imagehash.dhash(rgbImage,8)
		if str(matrix) in Sym_Hash:
			if Sym_Hash[str(matrix)] != letter:
				COLLISION += 1
				print("COLLISION",letter)
			else:
				DOBLE += 1
		else:
			Sym_Hash[str(matrix)] = letter
			fDict.write(letter + ";" + str(matrix) + "\n")
			TOTAL += 1

def generateDotMatrix(dirName):
	global fDict 
	global Sym_Hash
	global COLLISION
	global DOBLE
	global TOTAL
	Spis_Dot = glob.glob(dirName + "/*")
	for Dot in Spis_Dot:
		image = Image.open(Dot)
		rgbImage = image.convert("RGB")
		matrix = imagehash.dhash(rgbImage,8)
		if str(matrix) in Sym_Hash:
			if Sym_Hash[str(matrix)] != dirName:
				COLLISION += 1
				print("COLLISION")
			else:
				DOBLE += 1
		else:
			Sym_Hash[str(matrix)] = dirName
			fDict.write(dirName + ";" + str(matrix) + "\n")
			TOTAL += 1

# -------------------------------
Sym_Hash = {} ; COLLISION = 0 ; DOBLE = 0 ; TOTAL = 0
fDict = open("ocr-d8.txt", "w")
Spis_Fonts = glob.glob("fonts/*")
for fontName in Spis_Fonts:
	print(fontName)
	for fontSize in range(15,111):
		print(fontSize)
		os.system("rm characters/*.png > /dev/null 2>&1")
		textToImage(fontName, fontSize)
		os.system("mogrify -trim characters/*.png")
		generatePixelMatrix(fontName, fontSize)
generateDotMatrix("dot")
generateDotMatrix("euro")
print("COLLISION = " + str(COLLISION))
print("DOBLE = " + str(DOBLE))
print("TOTAL = " + str(TOTAL))
json.dump(Sym_Hash, open("Cif-d8.txt",'w'))
fDict.close()

