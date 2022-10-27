
import pytest
from selenium.webdriver.common.by import By



from .pages.main_page import MainPage


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

    #pytest -v --tb=line --language=en test_main_page.py
    #--tb=line, которая указывает, что нужно выводить только одну строку из лога каждого упавшего теста
    #pytest "-m login_guest" --language=en test_main_page.py

    def test_guest_should_see_login_link(browser):
        link = "http://selenium1py.pythonanywhere.com/ "
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     page.go_to_login_page()
    # login_page = LoginPage(browser, browser.current_url)
    # login_page.should_be_login_page()

    # http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer 

    # def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):

    #     link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/"
    #     page = ProductPage(browser, link)
    #     page.open()
    #     page.should_be_login_link()
    #     page.go_to_basket_page()
    #     assert page.is_not_element_present(*ProductBascket.PRODUCT_NAME_BASKET), \
    #         "Success message is presented, but should not be"
    #     page.basket_try()

    #pytest -v --tb=line --language=en test_main_page.py