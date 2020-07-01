from Base.driver import Driver
from Base.page import Page
from selenium.common.exceptions import TimeoutException

# 首页 -稍后更新
Page.get_home_page().click_update_later()

# 首页 -点击我的
Page.get_home_page().click_mine()

# 个人中心 -登录/注册
Page.get_person_page().click_login_sign_btn()

# 登录页面 -登录
Page.get_login_page().login('13048122192', 'Qq123456')

# 登录页面 -登录确认
Page.get_login_page().click_login_success_btn()

# 个人中心 -获取用户名
print(Page.get_person_page().get_user_name())

# 个人中心 -点击设置
Page.get_person_page().click_setting_btn()

# 设置页面 -确认退出
Page.get_setting_page().logout()

# 退出driver
Driver.quit_app_driver()
