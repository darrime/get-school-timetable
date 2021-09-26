import time

from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex

class_list = {
    '월': ['class1', 'class2', 'class3', 'class4', 'class5', 'class6', 'class7'],
    '화': ['class1', 'class2', 'class3', 'class4', 'class5', 'class6', 'class7'],
    '수': ['class1', 'class2', 'class3', 'class4', 'class5', 'class6', 'class7'],
    '목': ['class1', 'class2', 'class3', 'class4', 'class5', 'class6', 'class7'],
    '금': ['class1', 'class2', 'class3', 'class4', 'class5', 'class6', 'class7'],
}


class getSchoolTime:

    def __init__(self, school_name: str, class_number: str):
        self.school_name = school_name
        self.class_number = class_number

        option = wd.ChromeOptions()
        option.add_argument("headless")

        self.browser = wd.Chrome(options=option)

    def set_delay(self):
        wait = WebDriverWait(self.browser, 10).until(
            ex.presence_of_element_located((By.XPATH, '//*[@id="학교명단검색"]/tbody/tr[2]/td[1]')))
        print(wait.text[0:0])

    def run_js_code(self, js_code):
        self.browser.execute_script(js_code)
        time.sleep(0.1)

    def loading_timetable(self):

        self.browser.get("http://112.186.146.81:4082/st#")

        # 효율적인 딜레이 구현
        try:
            self.set_delay()
        except Exception:
            print("failed")

        # 자바스크립트 코드 목록
        js_code = [f'school_ra("{self.school_name}")',
                   'sc_disp(H학교명단.학교검색[0][3])',
                   'bas = document.getElementById("ba")',
                   f'bas.value = "{self.class_number}"',
                   'ba_change()']

        # 자바스크립트 코드 실행
        for i in js_code:
            self.run_js_code(i)

        for k, i in enumerate(class_list.keys(), 2):
            for j in range(0, 7):
                class_list[i][j] = self.browser.find_element_by_xpath(
                    f'//*[@id="hour"]/table/tbody/tr[{j + 3}]/td[{k}]').text[0:2]
        self.browser.quit()
        return class_list
