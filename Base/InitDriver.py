from appium import webdriver

def init_driver():
    # server ��������
    desired_caps = {}
    # �豸��Ϣ
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.1.2'  # ��ңģ����
    desired_caps['deviceName'] = '127.0.0.1:21503'
    # desired_caps['platformVersion'] = '8.0.0'  # huawei
    # desired_caps['deviceName'] = '4YY4C17525003861'

    # app��Ϣ
    desired_caps['appPackage'] = 'com.android.settings'  # ��ңģ��������
    desired_caps['appActivity'] = '.Settings'
    # desired_caps['appPackage'] = 'io.manong.developerdaily'  # ��ңģ���� ������ͷ��
    # desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.MainActivity'
    # desired_caps['appPackage'] = 'com.android.settings'  # huawei����
    # desired_caps['appActivity'] = '.HWSettings'
    # desired_caps['appPackage'] = 'com.android.mms'  # huawei����
    # desired_caps['appActivity'] = '.ui.ComposeMessageActivity'

    # ������������
    # desired_caps['unicodeKeyboard'] = True
    # desired_caps['resetKeyboard'] = True

    # ����driver����
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    return driver