"""
    appium方法二次封装
"""
from selenium.webdriver.support.wait import WebDriverWait

class Base:
    def __init__(self, driver): # 初始化
        self.driver = driver

    # def find_element(self, loc, loc_value, timeout=10, poll=0.5):
    def find_element(self, loc, timeout=10, poll=0.5):
        """
        :param loc: 元组类型 定位方式+属性值，类似(By.XPATH, "xpath语句")(By.ID, "id属性值")
        :return:
        """
        return WebDriverWait(self.driver, timeout, poll).\
            until(lambda driver: driver.find_element(*loc))

    def click_element(self, loc):
        # 元组类型 定位方式+属性值，类似(By.XPATH, "xpath语句")(By.ID, "id属性值")
        # 点击元素函数
        self.find_element(loc).click()

    def input_text(self, loc, text):
        """
        :param loc: 元组类型 (By.XPATH, "xpath语句")(By.ID, "id属性值")
        :param text: 输入内容
        :return:
        """
        # self.find_element(loc).send_keys(text)
        ele = self.find_element(loc)
        ele.clear()
        ele.send_keys(text)