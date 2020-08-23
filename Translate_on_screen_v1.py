import time
import win32api
import numpy as np
import cv2
import os
import pyscreenshot as ImageGrab
import pytesseract
import pyautogui
from googletrans import Translator

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'


x, y = 0 , 0
binded_key = 0x54
Start_pos = [0, 0]
End_pos = [0, 0]
filename = 'Image.png'
translator = Translator()
last_time = time.time()


def key_pressed(key):
	if win32api.GetKeyState(key) < 0:
		return True
	return False



while True:
	if key_pressed(0x11) and key_pressed(binded_key): # 0x11 = "T"
		Start_pos = [0, 0]
		End_pos = [0, 0]
	while key_pressed(binded_key):
		x, y = pyautogui.position()
		if Start_pos[0] == 0 and Start_pos[1] == 0:
			Start_pos = [x, y]
		time.sleep(0.01)
	if End_pos[0] == 0 and End_pos[1] == 0:
		End_pos = [x , y]
	print(Start_pos, End_pos)
	if Start_pos[0] != 0 and Start_pos[1] != 0 and End_pos[0] != 0 and End_pos[1] != 0:
		screen = np.array(ImageGrab.grab(bbox = (Start_pos[0], Start_pos[1], End_pos[0], End_pos[1])))
		cv2.imwrite(filename, screen)
		img = cv2.imread('Image.png')
		text = pytesseract.image_to_string(img)
		text = text.replace("\r"," ")
		text = text.replace("\n"," ")
		try:
			text_tr = translator.translate(text, src = 'en', dest = 'ru')
		except TypeError:
			print("")
		print(text_tr.text)
		print('loop took {} seconds'.format(time.time()-last_time))
		last_time = time.time()