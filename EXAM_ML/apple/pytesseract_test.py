'''
이미지 읽어 오기
'''
from PIL import Image
from PIL import ImageGrab
from pytesseract import *
import re
import cv2
import numpy as np

# tesseract ocr 실행 경로 설정
pytesseract.tesseract_cmd = r'C:\Users\kdp\AppData\Local\tesseract.exe'

img = cv2.imread('string_test.png', cv2.IMREAD_GRAYSCALE) # 굳이 RGB 다 필요 X
cv2.imshow('image', img)
text = pytesseract.image_to_string(img)

print(text)
cv2.waitKey(0) # 인수로 0 누르면 키보드가 눌리기 전까지 무기한 wait
