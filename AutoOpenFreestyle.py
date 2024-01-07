import time
import pyautogui
import pygetwindow as gw

import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import ctypes
import sys

# input("Press Enter to exit...")
# sys.argv[0]은 스크립트 파일의 경로이므로, 실제 인풋 파라미터는 sys.argv[1:]에서 시작합니다.

user_id = sys.argv[1:2]
user_pw = sys.argv[2:3]

# 받은 인풋 파라미터 출력
print("ID:", user_id)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    # input("Press Enter to exit...")
    sys.exit(1)
    
options = webdriver.ChromeOptions()
options.add_argument("--disable-popup-blocking")  # 팝업 차단 비활성화

# headless 옵션 설정 : 개발환경이 리눅스라면 아래 두가지는 포함
# options.add_argument('headless')
# options.add_argument("no-sandbox")

# 브라우저 사이즈 : 현재 창을 열지 않는 방식으로 구현
# options.add_argument('window-size=800,600')

# user_id = input('아이디를 입력하세요: ')
# user_pw = getpass.getpass('비밀번호를 입력하세요: ')

# 드라이버 위치 경로 입력
driver = webdriver.Chrome(options=options)



# url을 이용하여 브라우저로 접속
driver.get('https://www.joycity.com/user/integrateLogin?redirect=https%3A%2F%2Ffs2.joycity.com%2Fweb%2Fmain.do&SITE_CD=FS2')

# 대기시간 부여
driver.implicitly_wait(3)

# 아이디 입력
driver.find_element(By.ID, 'userID').send_keys(user_id)

# 비밀번호 입력
driver.find_element(By.ID, 'password').send_keys(user_pw)

# 로그인 버튼 클릭tk
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="userLoginForm"]/div/div[2]/div/div[2]/div/a[1]'))
)
login_button.click()

# 대기시간 부여
driver.implicitly_wait(10)

# 게임시작 버튼 클릭
game_start = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="new_ch"]/div/a'))
)
game_start.click()

# 권한 팝업 허용
time.sleep(2)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')

# 출석체크 이벤트
time.sleep(100)
# 찾고자 하는 창의 제목 또는 일부 문자열
target_window_title = "FS2"

# 제목이 일치하는 모든 창 가져오기
windows = gw.getWindowsWithTitle(target_window_title)

# 창이 존재하는지 확인
if windows:
    # url을 이용하여 브라우저로 접속
    driver.get('https://fs2.joycity.com/web/event/1/monthEvent.do')
    # 대기시간 부여
    driver.implicitly_wait(10)

    # 출석체크 버튼 클릭
    attention_check = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/ul/li[4]/a/span[2]'))
    )
    attention_check.click()
    driver.implicitly_wait(3)

    # 출석체크 버튼 클릭2
    attention_check2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/article[4]/div[2]/div[2]/div[2]/a'))
    )
    attention_check2.click()
else:
    print(f"창 '{target_window_title}'를 찾을 수 없습니다.")

# driver.close()
time.sleep(10)  # 10초 동안 스크립트 실행 유지
