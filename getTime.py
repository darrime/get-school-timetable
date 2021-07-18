import time
from selenium import webdriver as wd

# 백그라운드 작업
option = wd.ChromeOptions()
option.add_argument("headless")

browser = wd.Chrome(options=option)
#https로 접속 불가
browser.get("http://112.186.146.81:4082/st#")

elem = browser.find_element_by_id("sc")
button = browser.find_element_by_xpath('//*[@id="학교찾기"]/table[1]/tbody/tr[2]/td[2]/input[2]')

elem.click()
elem.send_keys("퇴계원중학교")
button.click()

time.sleep(0.1)

browser.execute_script('sc_disp(82294)')
time.sleep(0.1)
browser.execute_script('bas = document.getElementById("ba")')
time.sleep(0.1)
browser.execute_script('bas.value = "3-6"')
time.sleep(0.1)
browser.execute_script('ba_change()')

mon = {1: 'value', 2: 'value', 3: 'value', 4: 'value', 5: 'value', 6: 'value', 7: 'value'}
tue = {1: 'value', 2: 'value', 3: 'value', 4: 'value', 5: 'value', 6: 'value', 7: 'value'}
wen = {1: 'value', 2: 'value', 3: 'value', 4: 'value', 5: 'value', 6: 'value', 7: 'value'}
thr = {1: 'value', 2: 'value', 3: 'value', 4: 'value', 5: 'value', 6: 'value', 7: 'value'}
fri = {1: 'value', 2: 'value', 3: 'value', 4: 'value', 5: 'value', 6: 'value', 7: 'value'}

for i in range(1, 8):
    mon[i] = browser.find_element_by_xpath(f'//*[@id="hour"]/table/tbody/tr[{i + 2}]/td[2]').text[0:2]
    tue[i] = browser.find_element_by_xpath(f'//*[@id="hour"]/table/tbody/tr[{i + 2}]/td[3]').text[0:2]
    wen[i] = browser.find_element_by_xpath(f'//*[@id="hour"]/table/tbody/tr[{i + 2}]/td[4]').text[0:2]
    thr[i] = browser.find_element_by_xpath(f'//*[@id="hour"]/table/tbody/tr[{i + 2}]/td[5]').text[0:2]
    fri[i] = browser.find_element_by_xpath(f'//*[@id="hour"]/table/tbody/tr[{i + 2}]/td[6]').text[0:2]

browser.quit()