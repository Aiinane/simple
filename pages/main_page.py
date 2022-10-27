from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class MainPage(BasePage):
    #В аргументы больше не надо передавать экземпляр браузера, 
    # мы его передаем и сохраняем на этапе создания Page Object. 
    # Вместо него нужно указать аргумент self , чтобы иметь доступ к атрибутам и методам класса: 
    #Так как браузер у нас хранится как аргумент класса BasePage, обращаться к нему нужно соответствующим образом с помощью self: 

    # def go_to_login_page(self):
    #     login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     #login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    #     login_link.click()

    # def __init__(self, *args, **kwargs):
    #     super(MainPage, self).__init__(*args, **kwargs) #Как вы уже знаете, метод __init__ вызывается при создании объекта. Конструктор выше с ключевым словом super на самом деле только вызывает конструктор класса предка и передает ему все те аргументы, которые мы передали в конструктор MainPage.

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented" #здесь на символ *, он указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать.

    # def go_to_login_page(self):
    #     link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
    #     link.click()
    #     alert = self.browser.switch_to.alert
    #     alert.accept()

    
        # return LoginPage(browser=self.browser, url=self.browser.current_url) 