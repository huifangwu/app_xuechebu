from appium import webdriver


class Driver:

    app_driver = None

    @classmethod
    def get_app_driver(cls):
        if cls.app_driver is None:
            desired_caps = {
                'platformName': 'Android',
                'platformVersion': '5.1',
                'deviceName': 'sanxing',
                'appPackage': 'com.bjcsxq.chat.carfriend',
                'appActivity': '.module_main.activity.MainActivity'
            }

            cls.app_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            return cls.app_driver

        else:
            return cls.app_driver

    @classmethod
    def quit_app_driver(cls):
        if cls.app_driver is not None:
            cls.app_driver.quit()
            cls.app_driver = None
