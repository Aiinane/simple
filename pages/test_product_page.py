from pages.locators import ProductBascket
from pages.product_page import ProductPage
from pages.basket_page import BasketPage


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_basket_page()
    assert page.is_not_element_present(*ProductBascket.PRODUCT_NAME_BASKET), \
        "Success message is presented, but should not be"
    page.basket_is_empty_text()


