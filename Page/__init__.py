from selenium.webdriver.common.by import By
"""
    ���ͨѶ¼
"""
# ����û���ť
add_user = (By.ID, "com.android.contacts:id/floating_action_button")
# ������ر���
save_local = (By.XPATH, "//*[contains(@text, '����')]")
# ��λ����
send_name = (By.XPATH, "//*[contains(@text, '����')]")
# ��λ�ֻ���
send_phone = (By.XPATH, "//*[contains(@text, '�绰')]")
# ������ر��水ť
click_save_back = (By.XPATH, "//*[contains(@content-desc, '���ϵ���')]")

"""
    ����
"""
search_btn = (By.ID, "com.android.settings:id/search")
search_text = (By.ID, "android:id/search_src_text")
search_return = (By.CLASS_NAME, "android.widget.ImageButton")






