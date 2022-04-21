# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pyautogui
import time
import random

#pyautogui.displayMousePosition()
sleep = time.sleep
def reserver():
    driver = webdriver.Chrome()
    # 新增預約頁面
    driver.get("http://tw.store.dev.clinico.cloud/cl/appointment/create")
    driver.maximize_window()
    sleep(0.5)
    driver.find_element('xpath',"//span[text()='Cancel']").click()
    sleep(1)
    email = driver.find_element('xpath',"//input[@class='ant-input']")
    email.send_keys('mark.tseng@clinico.com.tw')
    password = driver.find_element('xpath',"(//input[@class='ant-input'])[2]")
    password.send_keys("tekfrvia47386")
    sleep(1)
    driver.find_element('xpath',"//button[contains(@class,'ant-btn ant-btn-block')]").click() #進入網站
    sleep(3)

    print(driver.title)

    # 抓取下拉選單元件
    select = driver.find_element('id',"appointmentEditForm_dataSource")
    select.click()
    #list_1 =['門市預約','臨櫃','TM']
    var1 = random.choice(['門市預約','臨櫃','TM'])
    #預約來源
    xpath_list_1 = "//div[text()='" + var1 + "']"
#    xpath_list_1 = "//div[text()='TM']"
    print(xpath_list_1)
    sleep(0.5)
    driver.find_element('xpath',xpath_list_1).click()
    sleep(0.5)
    #選新客戶
    driver.find_element('xpath','//*[@id="appointmentEditForm_memberType"]/label[1]/span[2]').click()
    sleep(0.5)
    #選男 class="ant-radio-input" value="Man"
    driver.find_element('xpath', '//*[@id="appointmentEditForm_gender"]/label[1]/span[1]/input').click()
    sleep(1)
    #名稱
    test = 'test' + str(random.randint(1,100))
    driver.find_element('id', 'appointmentEditForm_name').send_keys(test)
    sleep(0.5)
    #電話號碼
    phone_str = ""
    for i in range(8):
        phone_str = phone_str + random.choice("0123456789")
    phone = "09" + phone_str
    driver.find_element('id', 'appointmentEditForm_mobile').send_keys(phone)
    #預約身分
    select = driver.find_element('id',"appointmentEditForm_identity")
    select.click()
    sleep(0.5)
    list2 = ['本人','親友']
    xpath_list_2 = "//div[text()='" + random.choice(list2) +"']"
    driver.find_element('xpath',xpath_list_2).click()
    sleep(0.5)
    #門市
    select = driver.find_element('id',"appointmentEditForm_storeId")
    select.click()
    sleep(0.5)
    driver.find_element('xpath',"//div[text()='N297 - 衡陽門市']").click()
    sleep(0.5)

    #選配
    #pyautogui.moveTo(1908,736)
    #pyautogui.doubleClick()
    #select = driver.find_element("xpath","//input[@id='rc_select_10']")
    #select.click()
    sleep(0.5)
    pyautogui.moveTo(1168,961)
    pyautogui.click()
    sleep(0.5)
    driver.find_element('xpath',"//div[text()='L0149-蔡鋕鑫']").click()
    #pyautogui.moveTo(1905,867)
    #pyautogui.doubleClick()
    #預約項目
    select = driver.find_element('id',"appointmentEditForm_appointmentItemId")
    select.click()
    sleep(0.5)
    driver.find_element('xpath',"//span[@class='ant-badge-status-text']").click()
    #日期
    try:
        driver.find_element('xpath', "//*[@id='appointmentEditForm_appointmentDate']").send_keys('2022-04-25')
        sleep(0.5)
    except:
        pass

    driver.find_element('xpath',"//*[@id='appointmentEditForm_time']").send_keys('1030')
    sleep(0.5)
    driver.find_element('xpath',"//*[@id='appointmentEditForm']/div[3]/div/div[1]/button").click()
    sleep(4)

    url_id = driver.current_url[-6:]
    #門市新增會員
    try:
        driver.find_element('xpath', "//*[@id='rc-tabs-0-panel-/appointment/detail?id=" + url_id + "']/div/div/div/div[1]/div[1]/span/div/div[2]/button/span").click()
        sleep(2)
        driver.find_element('xpath', "/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/button[2]/span").click()
        sleep(2)
    except:
        pass


    #新增會員
    #try:
        #driver.find_element('xpath',"//span[text()='門市預約']")
    if var1 == '門市預約':
        driver.find_element('xpath',"//*[@id='rc-tabs-0-panel-/appointment/detail?id=" + url_id + "']/div/div/div/div[1]/div[1]/span/div/div[2]/button/span[2]").click()
    #except:
    #    pass

    #try:
    elif var1 == 'TM':
    #    driver.find_element('xpath',"//span[text()='TM']")
        driver.find_element('xpath',"//*[@id='rc-tabs-0-panel-/appointment/detail?id=" + url_id + "']/div/div/div/div[1]/div[1]/span/div/div[2]/button/span[2]").click()
    #except:
    #    pass
    #driver.find_element('xpath',"//*[@id='rc-tabs-0-panel-/appointment/detail?id=" + url_id +"']/div/div/div/div[1]/div[1]/span/div/div[2]/button/span[2]").click()
    sleep(5)

    # 填資料 郵件
    select = driver.find_element('id',"createMember_isBlockEmail")
    select.click()
    driver.find_element('xpath',"//div[text()='否']").click()
    sleep(1)
    # 填資料 個資文件
    select = driver.find_element('id',"createMember_isAgreePersonalInfoDocs")
    select.click()
    sleep(0.5)
    #driver.find_element('xpath',"//div[text()='同意']").click()
    personal_info= ['同意','不同意','未填寫']
    driver.find_element('xpath',"//div[text()='"+random.choice(personal_info)+"']").click()
    #xpath_list_1 = "//div[text()='" + random.choice(list_1) + "']"
    sleep(1)
    # 填資料 資料來源
    select = driver.find_element('id',"createMember_dataSource")
    select.click()
    sleep(0.5)
    driver.find_element('xpath',"//div[text()='舊客介紹']").click()
    sleep(1)
    # 填資料 地址
    select = driver.find_element('id',"createMember_region")
    select.click()
    sleep(0.5)
    area = ['(108) 臺北市 - 萬華區', '(106) 臺北市 - 大安區', '(105) 臺北市 - 松山區', '(112) 臺北市 - 北投區']
    driver.find_element('xpath',"//div[text()='"+random.choice(area)+"']").click()
    #driver.find_element('xpath',"//div[text()='(106) 臺北市 - 大安區']").click()
    sleep(1)
    driver.find_element('xpath',"//*[@id='createMember_address']").send_keys('11111111111')
    sleep(0.5)

    # 確認鍵
    driver.find_element('xpath',"//*[@id='createMember']/div[3]/div/div[1]/button/span").click()
    print('新增會員成功')
    driver.close()


sum = 0
for i in range(10):
    reserver()
    sum = sum + 1
    print('執行第',sum,'次')


