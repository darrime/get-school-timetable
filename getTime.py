import time

from secret_var import *
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex

option = wd.ChromeOptions()
option.add_argument("headless")

browser = wd.Chrome(options=option)

sub_list = {
    '월': ['class1', 'class2', 'class3', 'class4', 'class5', 'class6', 'class7'],
    '화': ['class1', 'class2', 'class3', 'class4', 'class5', 'class6', 'class7'],
    '수': ['class1', 'class2', 'class3', 'class4', 'class5', 'class6', 'class7'],
    '목': ['class1', 'class2', 'class3', 'class4', 'class5', 'class6', 'class7'],
    '금': ['class1', 'class2', 'class3', 'class4', 'class5', 'class6', 'class7'],
}


def set_delay():
    wait = WebDriverWait(browser, 10).until(
        ex.presence_of_element_located((By.XPATH, '//*[@id="학교명단검색"]/tbody/tr[2]/td[1]')))
    print(wait.text[0:0])


def run_js_code(js_code):
    browser.execute_script(js_code)
    time.sleep(0.1)


# 클래스 정의
class getClassSubject:
    # 이렇게 클래스 안에 넣어도 되는건지 모르겠다...
    browser.get("http://112.186.146.81:4082/st#")

    elem = browser.find_element_by_id("sc")
    button = browser.find_element_by_xpath('//*[@id="학교찾기"]/table[1]/tbody/tr[2]/td[2]/input[2]')

    elem.click()
    elem.send_keys(school_name)
    button.click()

    # 효율적인 딜레이 구현
    try:
        set_delay()
        print("-" * 6 + "로딩 성공" + "-" * 6)
    except:
        print("failed")

    # 자바스크립트 코드 목록
    js_code = [school_code, 'bas = document.getElementById("ba")', f'bas.value = "{class_num}"', 'ba_change()']

    # 자바스크립트 코드 실행
    for i in js_code:
        run_js_code(i)

    for k, i in enumerate(sub_list.keys(), 2):
        for j in range(0, 6):
            sub_list[i][j] = browser.find_element_by_xpath(
                f'//*[@id="hour"]/table/tbody/tr[{j + 3}]/td[{k}]').text[0:2]
    browser.quit()

    def __init__(self, day: str, class_time: int):
        self.day = day
        self.class_time = class_time

    def getSub(self):
        return sub_list[self.day][self.class_time - 1]
