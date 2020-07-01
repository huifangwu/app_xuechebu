import allure
import pytest
from Base.driver import Driver
from Base.get_data import GetData
from Base.page import Page


def get_login_data():
    login_list = list()

    data = GetData.get_yml_data('login.yml')  # type:dict
    for i in data.values():  # type:dict
        login_list.append((i.get('user'), i.get('pwd'), i.get('toast'), i.get('exp')))

    return login_list


class TestLogin:
    """登录测试"""

    @pytest.fixture(scope='class', autouse=True)
    def home_click_my_btn(self):
        """首页点击我 -一次"""
        # 首页 -点击稍后更新
        Page.get_home_page().click_update_later()
        # 首页 -点击我的
        Page.get_home_page().click_mine()

    @pytest.fixture(autouse=True)
    def person_click_login_sign(self):
        """个人中心点击登录/注册 -每次"""
        Page.get_person_page().click_login_sign_btn()

    @allure.step('登录功能测试')
    @pytest.mark.parametrize('user, pwd, toast, exp', get_login_data())
    def test_login(self, user, pwd, toast, exp):
        """登录测试方法"""
        # 登录
        Page.get_login_page().login(user, pwd)
        # 如果toast有值，就是逆向用例
        if toast is not None:
            """预期失败用例"""
            # 获取toast消息
            msg = Page.get_setting_page().get_toast(toast)
            try:
                # 断言toast消息
                assert msg == exp
            except AssertionError:
                # 截图
                Page.get_setting_page().screen_image()
                # 抛出异常
                raise
            finally:
                # 点击返回按钮
                Page.get_login_page().click_login_return_btn()
                allure.attach('预期失败用例测试步骤\n1、登录失败\n2、获取toast消息\n3、断言toast消息\n4、点击返回按钮', '预期登录失败')

        # 如果toast没有值，就是正向用例
        else:
            """预期通过用例"""
            # 登录确认按钮
            Page.get_login_page().click_login_success_btn()
            # 获取用户名
            user_name = Page.get_person_page().get_user_name()
            try:
                # 断言用户名
                assert user_name == exp
            except AssertionError:
                # 截图
                Page.get_setting_page().screen_image()
                # 抛出异常
                raise
            finally:
                # 点击设置
                Page.get_person_page().click_setting_btn()
                # 点击退出
                Page.get_setting_page().logout()
                allure.attach('预期通过用例测试步骤\n1、登录成功\n2、获取用户名\n3、断言用户名\n4、点击设置按钮\n5、点击退出按钮', '预期登录成功')

    def teardown_class(self):
        """退出driver"""
        Driver.quit_app_driver()
