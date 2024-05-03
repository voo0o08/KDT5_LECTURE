'''
action_chain_test -> 웹 들어가서 start 버튼 누른 후 map 캡쳐 후 이미지 저장
image_num_read_rgb -> 숫자 읽고 array 반환
'''
from pytesseract import *
import cv2
import numpy as np
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager # pip3 install webdriver-manager

# tesseract ocr 실행 경로 설정
pytesseract.tesseract_cmd = r'C:\Users\kdp\AppData\Local\tesseract.exe'
file = "apple_game_map.png"

def screen_shot(x_loc, y_loc, x_size = (1245-410), y_size = (840-355), filename='apple_game_map.png'):
    # 좌측 상단 Point(x=410, y=355)
    # 우측 상단 Point(x=1245, y=840)
    pyautogui.screenshot(filename, region=(x_loc, y_loc, x_size,y_size))
    print('take screen shot')

def click_play(x, y, actions):
    # 액션 실행
    actions.move_to_element_with_offset(canvas, x, y).click().perform()

def num_check(text):
    if len(text) == 0 or int(text) not in range(1, 10):
        return 100 # 인식 불가 숫자
    return int(text)

def image_num_read(filename):
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    r = img[:, :, 2]
    mask = cv2.threshold(r, 250, 255, cv2.THRESH_BINARY)[1]  # 사과 모양이 검은 색(0)

    gray_mask = np.minimum(mask, gray)

    bin_gray = cv2.threshold(gray_mask, 200, 255, cv2.THRESH_BINARY_INV)[1]

    # 샤프닝 커널 생성
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])

    # 이미지 필터링 (컨볼루션)
    bin_gray = cv2.filter2D(bin_gray, -1, kernel)
    # 255가 흰색

    end = 1245 - 410  # 가로
    hor = np.linspace(start=0, stop=end, num=18, endpoint=True, dtype="int")
    # print(f"가로 : {hor}")

    end = 840 - 355  # 세로
    ver = np.linspace(start=0, stop=end, num=11, endpoint=True, dtype="int")
    # print(f"세로 : {ver}")

    '''
    endpoint = True
    가로 : [  0  49  98 147 196 245 294 343 392 442 491 540 589 638 687 736 785 835]
    세로 : [  0  48  97 145 194 242 291 339 388 436 485]
    '''
    map_list = []
    cnt = 1
    for ver_idx in range(len(ver[:-1])):  # 세로
        temp_list = []
        for hor_idx in range(len(hor[:-1])):  # 가로
            # print(hor[hor_idx], hor[hor_idx+1], ver[ver_idx], ver[ver_idx+1])
            num_img = bin_gray[ver[ver_idx]:ver[ver_idx + 1], hor[hor_idx]:hor[hor_idx + 1]]  # 세로, 가로

            text = pytesseract.image_to_string(num_img, config=r'--psm 6 -c tessedit_char_whitelist=0123456789')

            num = num_check(text)
            temp_list.append(num)

            cnt += 1
        map_list.append(temp_list)
    # print(map_list)
    return np.array(map_list), hor, ver

def ten_cal(length, hor, ver):
    # 세로 묶음
    for i in range(temp_array.shape[1]):  # 17 x
        for j in range(temp_array.shape[0] - length + 1):  # 10 y
            # print(j, i)
            # print(temp_array[j:j + length, i])
            if sum(temp_array[j:j + length, i]) == 10:
                start_point = (hor[i], ver[j]) # 시작 x, y
                end_point = (hor[i+1], ver[j+length]) # 끝 x, y
                print(f"세로 시작 묶음 {hor[i], ver[j]}")
                print(f"세로 끝 묶음 {hor[i+1], ver[j+length]}")
                drag_mouse(start_point, end_point, length)
                temp_array[j:j + length, i] = np.zeros_like(temp_array[j:j + length, i])

    # 가로 묶음
    for i in range(temp_array.shape[0]):  # 10 행
        for j in range(temp_array.shape[1] - length + 1):  # 17 열
            # print(i, j)
            # print(temp_array[i, j:j + length])
            if sum(temp_array[i, j:j + length]) == 10:
                start_point = (hor[j], ver[i])  # 시작 x, y
                end_point = (hor[j+length], ver[i+1])  # 끝 x, y
                print(f"가로 묶음 {hor[j+length], ver[i+1]}")
                drag_mouse(start_point, end_point, length)
                temp_array[i, j:j + length] = np.zeros_like(temp_array[i, j:j + length])
def drag_mouse(start_point, end_point, length):
    # 캡쳐할 때 왼쪽 끝 x = 410, y = 355
    xoffset = 410 + start_point[0] # x
    yoffset = 355 + start_point[1] # y
    pyautogui.moveTo(xoffset, yoffset) # 시작 점 값으로 이동
    print(xoffset, yoffset)
    wait_time = (length+1) / 10
    pyautogui.dragTo(410+end_point[0], 355+end_point[1], 0.5)


# ========================main=================================

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3)

driver.get('https://www.gamesaien.com/game/fruit_box_a/')

# canvas css 찾기
canvas = driver.find_element_by_id('canvas')
# canvas_html = canvas.get_attribute('outerHTML')
# 출력
# print("=============== Canvas HTML Code ===============")
# print(canvas_html)
time.sleep(3)

# canvas css 내의 play 버튼 찾기
# move_to_element_with_offset의 parameter로 사용
# canvas size = x, y
x = 720 // 3
y = 470 // 2

actions = ActionChains(driver)
click_play(x, y, actions)

time.sleep(2)

screen_shot(410, 355)

time.sleep(2)
# print(pyautogui.position())
temp_array, hor, ver = image_num_read('apple_game_map.png')
print(f"가로 {hor}")
print(f"세로 {ver}")
ten_cal(4, hor, ver) # 세로 가로를 만들어야할 성 싶은 데...
ten_cal(3, hor, ver)
ten_cal(2, hor, ver)
ten_cal(5, hor, ver)
ten_cal(6, hor, ver)
ten_cal(7, hor, ver)
ten_cal(8, hor, ver)
print("================직선 끝===================")


img = cv2.imread(file, cv2.IMREAD_COLOR)

cv2.imshow("img", img)
cv2.waitKey(0)

driver.quit()