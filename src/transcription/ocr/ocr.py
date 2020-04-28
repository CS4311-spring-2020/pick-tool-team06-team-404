import os
from PIL import Image
import pytesseract
import argparse
import difflib

class optical_character_recognition:
    # img_path: String of full system path to the image

    def ocr_reader(self, img_path):
        '''OCR Reader using PyTesseract as the backend'''

        # SYSTEM CREATES THE OUTPUT TEXT FILE
        img_output = img_path[:-4]
        img_output = img_path + ".txt"

        # SYSTEM OPENS AND TRANSCRIBES THE IMAGE
        img = Image.open(img_path)  # Opens file, pre-transcription
        img_txt = pytesseract.image_to_string(img, lang="eng")

        # SYSTEM WRITES IMAGE TEXT TO FILE
        text_file = open(img_output, "w")
        text_file.write(img_txt)
        text_file.close()
