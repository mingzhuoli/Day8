from appium import webdriver

def init_driver():
    # server 启动参数
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.1.2'  # 逍遥模拟器
    desired_caps['deviceName'] = '127.0.0.1:21503'
    # desired_caps['platformVersion'] = '8.0.0'  # huawei
    # desired_caps['deviceName'] = '4YY4C17525003861'

    # app信息
    desired_caps['appPackage'] = 'com.android.settings'  # 逍遥模拟器设置
    desired_caps['appActivity'] = '.Settings'
    # desired_caps['appPackage'] = 'io.manong.developerdaily'  # 逍遥模拟器 开发者头条
    # desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.MainActivity'
    # desired_caps['appPackage'] = 'com.android.settings'  # huawei设置
    # desired_caps['appActivity'] = '.HWSettings'
    # desired_caps['appPackage'] = 'com.android.mms'  # huawei短信
    # desired_caps['appActivity'] = '.ui.ComposeMessageActivity'

    # 中文输入允许
    # desired_caps['unicodeKeyboard'] = True
    # desired_caps['resetKeyboard'] = True

    # 声明driver对象
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    return driver