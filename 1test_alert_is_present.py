import time
import pytest
from .pages.locators import AlertSelector
from .pages.product_page import ProductPage # в начале файла


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    page = ProductPage(browser, link)
    page.open()
    page.should_be_added_thing_in_basket()
    assert page.is_not_element_present(*AlertSelector.SELECTOR_ALERT), \
        "Success message is presented, but should not be"


def test_guest_cant_see_success_message  (browser):
    page = ProductPage(browser, link)
    page.open()
    assert page.is_not_element_present(*AlertSelector.SELECTOR_ALERT), \
            "Success message is presented, but should not be"
 

def test_message_disappeared_after_adding_product_to_basket (browser): 
    page = ProductPage(browser, link)
    page.open()
    page.should_be_added_thing_in_basket()
    assert page.is_disappeared (*AlertSelector.SELECTOR_ALERT), \
                "Success message is presented, but should not be"

                 # pytest -s test_alert_is_present.py
                 #@pytest.mark.xfail