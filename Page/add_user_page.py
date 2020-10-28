from Base.Base import Base
import Page, time

class Add_User_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_add(self):
        # �������û���ť
        print("Page.add_user: ", Page.add_user)
        self.click_element(Page.add_user)

    def click_save_local(self):
        # ������ر���
        self.click_element(Page.save_local)

    def input_user_info(self, name, phone):
        # �����û���
        self.input_text(Page.send_name, name)
        # �绰
        self.input_text(Page.send_phone, phone)
        # ������ر���
        self.click_element(Page.click_save_back)
        time.sleep(5)
        self.driver.keyevent(4)