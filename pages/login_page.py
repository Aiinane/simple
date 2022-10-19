from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url , f"This is not login page'"
        # реализуйте проверку на корректный url адрес
        

    def should_be_login_form(self):
        #login_str = str(self.browser.find_element(LoginPageLocators.LOGIN_FORM))
        # реализуйте проверку, что есть форма логина
        assert "login_form" in self.browser.find_element(*LoginPageLocators.LOGIN_FORM) , f"login_form isn't in this page'" 

    def should_be_register_form(self):
        #reg_str = str(self.browser.find_element(LoginPageLocators.REGISER_FORM))
        # реализуйте проверку, что есть форма регистрации на странице
        assert "register_form" in self.browser.find_element(*LoginPageLocators.REGISER_FORM), f"register_form isn't in this page'"

        




