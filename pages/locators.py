from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") #теперь каждый селектор — это пара: как искать и что искать. 

class LoginPageLocators ():
    LOGIN_FORM = (By.ID, "login_form")
    REGISER_FORM = (By.ID, "register_form")

    

