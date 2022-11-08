from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    __username=(By.ID,"username")
    __password=(By.NAME,"pwd")
    __loginbutton=(By.XPATH,"//div[.='Login ']")
    __errmsg = (By.XPATH,"//span[contains(.,'invalid')]")

    def __init__(self,driver):
        self.__driver=driver

    def set_username(self,un):
        self.__driver.find_element(*self.__username).send_keys(un)

    def set_password(self,pw):
        self.__driver.find_element(*self.__password).send_keys(pw)

    def click_loginbutton(self):
        self.__driver.find_element(*self.__loginbutton).click()

    def verify_errmsg_displayed(self, wait):
        try:
            wait.until(EC.visibility_of_element_located(self.__errmsg))
            print("error message is displayed")
            return True

        except:
            print("error message is not displayed")
            return False