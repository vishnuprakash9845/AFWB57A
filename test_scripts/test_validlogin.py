import time

import pytest

from generic.base_test import BaseTest
from generic.utility import Excel
from pages.home_page import HomePage
from pages.login_page import LoginPage

class TestValidLogin(BaseTest):

    def test_script1(self):
        print("This is my script1")
        print(self.driver.title)
        v = Excel.get_cellvalue("../data/input.xlsx", "ValidLogin", 2, 1)
        print(v)

    @pytest.mark.run(order=1)
    def test_validlogin(self):
        un = Excel.get_cellvalue("../data/input.xlsx", "ValidLogin", 2, 1)
        pw = Excel.get_cellvalue("../data/input.xlsx", "ValidLogin", 2, 2)
        loginpage=LoginPage(self.driver)
        #1. Enter valid Username
        loginpage.set_username(un)
        # 2. Enter valid password
        loginpage.set_password(pw)
        # 3. click on login button
        loginpage.click_loginbutton()
        # 4. verify that home page is displayed
        homepage = HomePage(self.driver)
        result = homepage.verify_homepage_is_displayed(self.wait)
        assert result


