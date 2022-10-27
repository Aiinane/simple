import time
import pytest
from .pages.product_page import ProductPage # в начале файла

#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#urls = [f"{link}/?promo=offer{no}" for no in range(10)]

 
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{link}?promo=offer{no}" if no != "7"
        else pytest.param("bugged_link", marks=pytest.mark.xfail) for no in range(10)]

 

#@pytest.mark.parametrize( "link",  [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='fail test')) for i in range(10)])
#@pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i==8,9, reason='fail test')) for i in range(10)])
@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    #link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    
    page = ProductPage(browser, link)
    page.open()
    page.should_be_added_thing_in_basket()

    # pytest -s test_books.py   -v 8 9