'''
셀레니움 액션 체인 테스트
- start 버튼 누르기 까지!! ㅇ
- 화면 캡쳐하기 ㅇ
'''
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager # pip3 install webdriver-manager

def screen_shot(x_loc, y_loc, x_size = (1245-410), y_size = (840-355), filename='apple_map.png'):
    # 좌측 상단 Point(x=410, y=355)
    # 우측 상단 Point(x=1245, y=840)
    pyautogui.screenshot(filename, region=(x_loc, y_loc, x_size, y_size))
    print('take screen shot')

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3)

driver.get('https://www.gamesaien.com/game/fruit_box_a/')

# # canvas css 찾기
canvas = driver.find_element_by_id('canvas')
# canvas_html = canvas.get_attribute('outerHTML')
# # 출력
# print("=============== Canvas HTML Code ===============")
# print(canvas_html)
time.sleep(5)

# canvas css 내의 play 버튼 찾기
# move_to_element_with_offset의 parameter로 사용

x = 720 // 3
y = 470 // 2

# 액션 실행
actions = ActionChains(driver)
actions.move_to_element_with_offset(canvas, x, y).click().perform()

time.sleep(2)
screen_shot(410, 355)
time.sleep(2)
print(pyautogui.position())
driver.quit()



