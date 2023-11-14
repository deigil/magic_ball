# import the necessary packages
from PIL import Image
import pytesseract
import cv2
import os

def ocr(image_path, preprocess="thresh"):
	# load the image and convert it to grayscale
	image = cv2.imread(image_path)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
	# check preprocessing type
	if preprocess == "thresh": 
		gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	elif preprocess == "blur":
		gray = cv2.medianBlur(gray, 3)
	elif preprocess == "a_thresh":
		block_size = 11
		constant = 2
		gray = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, constant
    	)

	# write the grayscale image to disk as a temporary file so we can
	# apply OCR to it
	filename = "{}.png".format(os.getpid())
	cv2.imwrite(filename, gray)

	# load the image as a PIL/Pillow image, apply OCR, and then delete
	# the temporary file
	print("OCR in progress..")
	custom_config = r'--oem 3 --psm 8'
	text = pytesseract.image_to_string(Image.open(filename), config=custom_config)
	os.remove(filename)
	print(f"Extracted text: {text}")
	# show the output images
	cv2.imshow("Image", image)
	cv2.imshow("Output", gray)
	cv2.waitKey(5000)

	return text