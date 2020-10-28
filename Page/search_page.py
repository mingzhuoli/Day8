from Base.Base import Base
import Page

class Search_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_search_btn(self):
        # ���������ť
        self.click_element(Page.search_btn)

    def search_input(self, text):
        # ����
        self.input_element(Page.search_text, text)

    def search_return(self):
        # �������
        self.click_element(Page.search_return)