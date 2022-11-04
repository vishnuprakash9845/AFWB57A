import time
from generic.base_test import BaseTest
from generic.utility import Excel
from pages.home_page import HomePage
from pages.login_page import LoginPage

class TestValidLogin(BaseTest):

    def test_script1(self):
        print("This is my script1")
        print(self.driver.title)
        v = Excel.get_cellvalue("../data/input.xlsx", "Sheet1", 2, 1)
        print(v)

    def test_validlogin(self):
        loginpage=LoginPage(self.driver)
        #1. Enter valid Username
        loginpage.set_username("admin")
        # 2. Enter valid password
        loginpage.set_password("dmanager")
        # 3. click on login button
        loginpage.click_loginbutton()
        # 4. verify that home page is displayed
        homepage = HomePage(self.driver)
        result = homepage.verify_homepage_is_displayed(self.wait)
        assert result


