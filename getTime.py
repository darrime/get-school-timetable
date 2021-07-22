import time
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex

# 백그라운드 작업
option = wd.ChromeOptions()
option.add_argument("headless")

browser = wd.Chrome(options=option)


# 자바스립트 코드 실행 함수 추가
def run_jscode(jscode):
    browser.execute_script(jscode)
    time.sleep(0.1)


# 효율적인 딜레이 함수
def get_delay():
    wait = WebDriverWait(browser, 10).until(
        ex.presence_of_element_located((By.XPATH, '//*[@id="학교명단검색"]/tbody/tr[2]/td[1]')))
    print(wait.text[0:0])


# https로 접속 불가한 사이트
browser.get("http://112.186.146.81:4082/st#")

elem = browser.find_element_by_id("sc")
button = browser.find_element_by_xpath('//*[@id="학교찾기"]/table[1]/tbody/tr[2]/td[2]/input[2]')

elem.click()
elem.send_keys("퇴계원중학교")
button.click()

# 효율적인 딜레이 구현
try:
    get_delay()
    print("-" * 6 + "로딩 성공" + "-" * 6)
except:
    print("failed")

# 자바스크립트 코드 목록
js_code = ['sc_disp(82294)', 'bas = document.getElementById("ba")', 'bas.value = "3-6"', 'ba_change()']

# 자바스크립트 코드 실행
for i in js_code:
    run_jscode(i)

class_list = {
    '월': ['class1', 'class2', 'class3', 'class4', 'class5', 'class6', 'class7'],
    '화': ['class1', 'class2', 'class3', 'class4', 'class5', 'class6', 'class7'],
    '수': ['class1', 'class2', 'class3', 'class4', 'class5', 'class6', 'class7'],
    '목': ['class1', 'class2', 'class3', 'class4', 'class5', 'class6', 'class7'],
    '금': ['class1', 'class2', 'class3', 'class4', 'class5', 'class6', 'class7'],
}

for k, i in enumerate(class_list.keys(), 2):
    for j in range(0, 6):
        class_list[i][j] = browser.find_element_by_xpath(f'//*[@id="hour"]/table/tbody/tr[{j + 3}]/td[{k}]').text[0:2]


# 수업 과목 구하는 함수
def get_classes(day: str, time: int):
    return class_list[day][time - 1]


browser.quit()
