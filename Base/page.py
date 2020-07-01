from Page.home_page import HomePage
from Page.login_page import LoginPage
from Page.person_page import PersonPage
from Page.setting_page import SettingPage


class Page:
    """所有页面类实例化对象"""

    @classmethod
    def get_home_page(cls):
        """主页"""
        return HomePage()

    @classmethod
    def get_person_page(cls):
        """个人中心"""
        return PersonPage()

    @classmethod
    def get_login_page(cls):
        """登录"""
        return LoginPage()

    @classmethod
    def get_setting_page(cls):
        """设置"""
        return SettingPage()
