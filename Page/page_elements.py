from selenium.webdriver.common.by import By


class PageElements:
    """管理页面元素"""

    """首页"""
    # 稍后更新
    # home_update_later_btn_id = (By.ID, 'com.bjcsxq.chat.carfriend:id/bt_no')
    home_update_later_btn_xpath = (By.XPATH, '//*[contains(@text, "稍后更新")]')
    # 我的
    home_mine_btn_id = (By.ID, 'com.bjcsxq.chat.carfriend:id/mine_image')

    """我的个人中心"""
    # 登录
    person_login_sign_btn_xpath = (By.XPATH, '//*[contains(@text, "登录/注册")]')
    # 用户名
    person_username_id = (By.ID, 'com.bjcsxq.chat.carfriend:id/mine_username_tv')
    # 设置
    person_setting_btn_id = (By.ID, 'com.bjcsxq.chat.carfriend:id/mine_set_rl')

    """登录"""
    # 账号
    login_account_id = (By.ID, 'com.bjcsxq.chat.carfriend:id/login_phone_et')
    # 密码
    login_pwd_id = (By.ID, 'com.bjcsxq.chat.carfriend:id/login_pwd_et')
    # 登录按钮
    login_btn_id = (By.ID, 'com.bjcsxq.chat.carfriend:id/login_btn')
    # 登录确定按钮
    login_confirm_btn_id = (By.ID, 'com.bjcsxq.chat.carfriend:id/btn_neg')
    # 登录返回按钮
    login_return_btn_id = (By.ID, 'com.bjcsxq.chat.carfriend:id/title_back')


    """设置"""
    # 退出按钮
    setting_logout_btn_id = (By.ID, 'com.bjcsxq.chat.carfriend:id/set_logout_tv')
    # 退出 - 确认
    setting_logout_confirm_btn_id = (By.ID, 'com.bjcsxq.chat.carfriend:id/bt_ok')
    # 退出 - 取消
    setting_logout_cancel_btn_id = (By.ID, 'com.bjcsxq.chat.carfriend:id/bt_no')