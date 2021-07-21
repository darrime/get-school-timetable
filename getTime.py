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


# 딜레이 함수 추가
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

# 효율적인 코드 구현
for i in js_code:
    run_jscode(i)

mon = {1: 'value', 2: 'value', 3: 'value', 4: 'value', 5: 'value', 6: 'value', 7: 'value'}
tue = {1: 'value', 2: 'value', 3: 'value', 4: 'value', 5: 'value', 6: 'value', 7: 'value'}
wen = {1: 'value', 2: 'value', 3: 'value', 4: 'value', 5: 'value', 6: 'value', 7: 'value'}
thr = {1: 'value', 2: 'value', 3: 'value', 4: 'value', 5: 'value', 6: 'value', 7: 'value'}
fri = {1: 'value', 2: 'value', 3: 'value', 4: 'value', 5: 'value', 6: 'value', 7: 'value'}

# 딕셔너리 자료형으로 코드 간소화 예정
for i in range(1, 8):
    mon[i] = browser.find_element_by_xpath(f'//*[@id="hour"]/table/tbody/tr[{i + 2}]/td[2]').text[0:2]
    tue[i] = browser.find_element_by_xpath(f'//*[@id="hour"]/table/tbody/tr[{i + 2}]/td[3]').text[0:2]
    wen[i] = browser.find_element_by_xpath(f'//*[@id="hour"]/table/tbody/tr[{i + 2}]/td[4]').text[0:2]
    thr[i] = browser.find_element_by_xpath(f'//*[@id="hour"]/table/tbody/tr[{i + 2}]/td[5]').text[0:2]
    fri[i] = browser.find_element_by_xpath(f'//*[@id="hour"]/table/tbody/tr[{i + 2}]/td[6]').text[0:2]

print(mon[1])
browser.quit()
