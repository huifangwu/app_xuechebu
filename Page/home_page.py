from Base.base import Base
from Page.page_elements import PageElements
from selenium.common.exceptions import TimeoutException


class HomePage(Base):
    """首页"""

    def __init__(self):
        super().__init__()

    def click_update_later(self):
        """点击稍后更新按钮"""
        try:
            self.click_ele(PageElements.home_update_later_btn_xpath)
        except TimeoutException:
            print('当前版本app没有更新提示框')

    def click_mine(self):
        """点击我的"""
        self.click_ele(PageElements.home_mine_btn_id)
