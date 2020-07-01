import allure, os


class TestScreen:

    def test_001(self):
        with open('./Image' + os.sep + '1122.png', 'rb')as f:
            allure.attach(body=f.read(), name='截图', attachment_type=allure.attachment_type.PNG)
