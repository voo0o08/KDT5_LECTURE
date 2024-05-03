'''
action_chain_test.py에서 저장한 이미지 파일 숫자 읽기
'''
from PIL import Image
from PIL import ImageGrab
from pytesseract import *
import re
import cv2
import numpy as np

# tesseract ocr 실행 경로 설정
pytesseract.tesseract_cmd = r'C:\Users\kdp\AppData\Local\tesseract.exe'

img = cv2.imread('apple_map.png', cv2.IMREAD_GRAYSCALE) # 굳이 BGR 다 필요 X

img = cv2.blur(img,(5, 5)) # 블러처리 ######################

# gray = cv2.threshold(img, 247, 255, cv2.THRESH_BINARY_INV)[1] # 255=흰색
gray = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)[1] # 255=흰색
# thresh 아래는 0으로 처리
# print(img)
# gray = cv2.blur(gray,(3, 3)) # 블러처리
# text = pytesseract.image_to_string(img, config="--psm 6")

###########################
# 샤프닝 커널 생성
kernel = np.array([[-1, -1, -1],
                   [-1, 9, -1],
                   [-1, -1, -1]])

# 이미지 필터링 (컨볼루션)
# gray = cv2.filter2D(gray, -1, kernel)
#############################

text = pytesseract.image_to_string(gray, config=r'--psm 6 -c tessedit_char_whitelist=0123456789')
print(text)
cv2.imshow('image', gray)
cv2.waitKey(0) # 인수로 0 누르면 키보드가 눌리기 전까지 무기한 wait
# 255가 흰색

# 2차원 숫자 map : 사과의 숫자만 뽑아서 2차원 배열로 만든 것
num_lists = []
for row in text.split('\n'):
    print(row, "=>", len(row))
    num_lists.append(list(row))
print(len(num_lists))