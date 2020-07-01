import time, allure, os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Base.driver import Driver


class Base:

    def __init__(self):
        self.driver = Driver.get_app_driver()

    def find_ele(self, loc, timeout=5, poll_frequency=1.0):
        """
        定位一个元素
        :param loc: (By.ID, 定位元素) (By.CLASS_NAME, 定位元素) (By.XPATH, 定位元素)
        :param timeout: 等待最长时间，超出返回TimeOut报错
        :param poll_frequency: 间隔时间
        :return:
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def find_eles(self, loc, timeout=5, poll_frequency=1.0):
        """
        定位一组元素
        :param loc: (By.ID, 定位元素) (By.CLASS_NAME, 定位元素) (By.XPATH, 定位元素)
        :param timeout: 等待最长时间，超出返回TimeOut报错
        :param poll_frequency: 间隔时间
        :return:
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_ele(self, loc, timeout=5, poll_frequency=1.0):
        """
        点击方法
        :param loc: (By.ID, 定位元素) (By.CLASS_NAME, 定位元素) (By.XPATH, 定位元素)
        :param timeout: 等待最长时间，超出返回TimeOut报错
        :param poll_frequency: 间隔时间
        :return:
        """
        self.find_ele(loc, timeout, poll_frequency).click()

    def send_ele(self, loc, text, timeout=5, poll_frequency=1.0):
        """
        输入方法
        :param loc: (By.ID, 定位元素) (By.CLASS_NAME, 定位元素) (By.XPATH, 定位元素)
        :param text: 输入文本内容
        :param timeout: 等待最长时间，超出返回TimeOut报错
        :param poll_frequency: 间隔时间
        :return:
        """
        input_text = self.find_ele(loc, timeout, poll_frequency)
        input_text.clear()
        input_text.send_keys(text)

    def swipe_screen(self, tag=1):
        """
        滑动屏幕
        :param tag: 1：向上 2：向下 3：向左 4：向右
        :return:
        """
        # 分辨率
        size = self.driver.get_window_size()
        # 宽
        width = size.get('width')
        # 高
        height = size.get('height')

        time.sleep(1)
        if tag == 1:
            # 向上滑动
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2, 2000)
        if tag == 2:
            # 向下滑动
            self.driver.swipe(width * 0.5, height * 0.2, width * 0.5, height * 0.8, 2000)
        if tag == 3:
            # 向左滑动
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.2, height * 0.5, 2000)
        if tag == 4:
            # 向右滑动
            self.driver.swipe(width * 0.2, height * 0.5, width * 0.8, height * 0.5, 2000)

    def get_toast(self, message):
        """
        获取toast文本
        :param message: toast文本信息
        :return:
        """
        toast_xpath = (By.XPATH, '//*[contains(@text, "{}")]'.format(message))
        # 定位toast
        return self.find_ele(toast_xpath, timeout=3, poll_frequency=0.5).text

    def screen_image(self, name='截图'):
        """
        截图
        :param name: allure报告中，图片的名字
        :return:
        """
        # 图片名字
        png_name = './Image' + os.sep + '{}.png'.format(time.strftime('%Y%m%d%H%M%S'))
        # 获取截图
        self.driver.get_screenshot_as_file(png_name)
        # 把截图写入allure报告
        with open(png_name, 'rb')as f:
            allure.attach(f.read(), name, attachment_type=allure.attachment_type.PNG)
