'''
action_chain_test.py에서 저장한 이미지 파일 숫자 읽기
'''

from pytesseract import *
import cv2
import numpy as np

def num_check(text):
    if len(text) == 0 or int(text) not in range(1, 10):
        return 100 # 인식 불가 숫자
    return int(text)


# tesseract ocr 실행 경로 설정
pytesseract.tesseract_cmd = r'C:\Users\kdp\AppData\Local\tesseract.exe'

img = cv2.imread('apple_map.png', cv2.IMREAD_COLOR)
gray = cv2.imread('apple_map.png', cv2.IMREAD_GRAYSCALE)

g = img[:,:,0]
b = img[:,:,1]
r = img[:,:,2]
mask = cv2.threshold(r, 250, 255, cv2.THRESH_BINARY)[1] # 사과 모양이 검은 색(0)

gray_mask = np.minimum(mask, gray)
# cv2.imshow('image', gray_mask)
bin_gray = cv2.threshold(gray_mask, 200, 255, cv2.THRESH_BINARY_INV)[1]


# 샤프닝 커널 생성
kernel = np.array([[-1, -1, -1],
                   [-1, 9, -1],
                   [-1, -1, -1]])

# 이미지 필터링 (컨볼루션)
bin_gray = cv2.filter2D(bin_gray, -1, kernel)

# cv2.imshow('bin_gray', bin_gray)
# cv2.waitKey(0) # 인수로 0 누르면 키보드가 눌리기 전까지 무기한 wait
# 255가 흰색

################################### 숫자 하나 하나 쪼개기

end = 1245-410 # 가로
hor = np.linspace(start=0, stop=end, num=18, endpoint=True, dtype="int")
print(f"가로 : {hor}")

end = 840-355 # 세로
ver = np.linspace(start=0, stop=end, num=11, endpoint=True, dtype="int")
print(f"세로 : {ver}")

'''
endpoint = True
가로 : [  0  49  98 147 196 245 294 343 392 442 491 540 589 638 687 736 785 835]
세로 : [  0  48  97 145 194 242 291 339 388 436 485]
'''
map_list = []
cnt = 1
for ver_idx in range(len(ver[:-1])): # 세로

    temp_list = []
    for hor_idx in range(len(hor[:-1])):  # 가로
        # print(hor[hor_idx], hor[hor_idx+1], ver[ver_idx], ver[ver_idx+1])
        num_img = bin_gray[ver[ver_idx]:ver[ver_idx+1], hor[hor_idx]:hor[hor_idx+1]] # 세로, 가로
        # cv2.imshow("num_img", num_img)
        # cv2.waitKey(0)
        text = pytesseract.image_to_string(num_img, config=r'--psm 6 -c tessedit_char_whitelist=0123456789')
        # print(f"{cnt} : {text}")
        # if len(text) == 0:
            # 인식이 안되는 숫자 이미지로
            # cv2.imshow("num_img", num_img)
            # cv2.waitKey(0)
        num = num_check(text)
        temp_list.append(num)

        cnt += 1
    map_list.append(temp_list)
print(map_list)