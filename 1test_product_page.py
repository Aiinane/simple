

from .pages.product_page import ProductPage # в начале файла



def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_added_thing_in_basket()
    
    
    # login_page = LoginPage(browser, browser.current_url)
    # login_page.should_be_login_page()




# Чтобы увидеть проверочный код в консоли, запускайте PyTest с параметром -s:

# pytest -s test_product_page.py