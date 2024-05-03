# Selenium 임포트
from selenium import webdriver # 4.17.2
from selenium.webdriver.common.by import By # find_element 때문에
import time # sleep 때문에


# 크롬 드라이버 생성
driver = webdriver.Chrome()
driver.implicitly_wait(3)
# 웹사이트 로딩안된 상태로 뒤로 넘어가면 오류날 가능성이 있기 때문에 몇초 정지

# 사이트 접속하기
driver.get('https://workey.codeit.kr/costagram/index')

# BS처럼 CSS선택자를 통해 요소 받아오기
driver.find_element(By.CLASS_NAME, "top-nav__login-link").click() # 로그인 버튼의 CSS 선택자
driver.find_element(By.CLASS_NAME, "login-container__login-input").send_keys("codeit") # 아이디 입력
driver.find_element(By.CLASS_NAME, "login-container__password-input").send_keys("datascience") # 비밀번호 입력

# 로그인 버튼 클릭
driver.find_element(By.CLASS_NAME, "login-container__login-button").click()
time.sleep(10) # 브라우저 창 너무 빨리 닫히면 sleep 넣어주기

# 크롬 드라이버 종료
# driver.quit()
