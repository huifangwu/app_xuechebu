from Base.base import Base
from Page.page_elements import PageElements


class PersonPage(Base):
    """我的个人中心"""

    def __init__(self):
        super().__init__()

    def click_login_sign_btn(self):
        """点击登录/注册按钮"""
        self.click_ele(PageElements.person_login_sign_btn_xpath)

    def get_user_name(self):
        """获取用户名"""
        return self.find_ele(PageElements.person_username_id).text

    def click_setting_btn(self):
        """点击设置按钮"""
        # 向上滑动
        self.swipe_screen()
        self.click_ele(PageElements.person_setting_btn_id)
