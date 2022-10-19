
import pytest
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#     page.open()                      # открываем страницу
#     page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

    #pytest -v --tb=line --language=en test_main_page.py
    #--tb=line, которая указывает, что нужно выводить только одну строку из лога каждого упавшего теста

# def test_guest_should_see_login_link(browser):
#     link = "http://selenium1py.pythonanywhere.com/ "
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    # login_page = LoginPage(browser, browser.current_url)
    # login_page.should_be_login_page()

    # http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer 



    #pytest -v --tb=line --language=en test_main_page.py