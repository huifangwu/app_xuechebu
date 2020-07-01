from Base.base import Base
from Page.page_elements import PageElements


class LoginPage(Base):
    """登录"""

    def __init__(self):
        super().__init__()

    def login(self, user, pwd):
        self.send_ele(PageElements.login_account_id, user)
        self.send_ele(PageElements.login_pwd_id, pwd)
        self.click_ele(PageElements.login_btn_id)

    def click_login_success_btn(self):
        self.click_ele(PageElements.login_confirm_btn_id)

    def click_login_return_btn(self):
        self.click_ele(PageElements.login_return_btn_id)
