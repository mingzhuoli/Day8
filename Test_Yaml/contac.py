# -*-coding:utf-8 -*-
# -*-coding:GBK -*-
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

# server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '7.1.2'  # 逍遥模拟器
# desired_caps['deviceName'] = '127.0.0.1:21503'
# desired_caps['noReset'] = 'true'

desired_caps['platformVersion'] = '8.0.0'  # huawei
desired_caps['deviceName'] = '4YY4C17525003861'
desired_caps['noReset'] = 'true'

# app信息
# desired_caps['appPackage'] = 'com.android.settings'  # 逍遥模拟器设置
# desired_caps['appActivity'] = '.Settings'
# desired_caps['appPackage'] = 'io.manong.developerdaily'  # 逍遥模拟器 开发者头条
# desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.MainActivity'
# desired_caps['appPackage'] = 'com.android.settings'  # huawei设置
# desired_caps['appActivity'] = '.HWSettings'
# desired_caps['appPackage'] = 'com.android.mms'  # huawei短信
# desired_caps['appActivity'] = '.ui.ComposeMessageActivity'

desired_caps['appPackage'] = 'com.android.contacts'
desired_caps['appActivity'] = '.activities.DialtactsActivity'

# 中文输入允许
# desired_caps['unicodeKeyboard'] = True
# desired_caps['resetKeyboard'] = True

# 声明driver对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

try:
    WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element_by_xpath("//*[contains(@text, '联系人')]").click())
    # data = WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element_by_id("com.android.contacts:id/menu_add_contact"))
    # data.click()

    # data = WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element_by_xpath("//*[contains(@text, '王五')]"))
    data = WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element_by_xpath("//*[contains(@text, '王五')]/.."))
    # print(data.text)
    # print(data.get_attribute("className"))
    print(data.location)
    # data.click()
except:
    pass

time.sleep(5)
driver.quit()