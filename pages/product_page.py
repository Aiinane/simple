import time
from unicodedata import name
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ButtonClick, ProductBascket
import math
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):

    
    # def go_to_login_page(self):
            # price = self.browser.find_elements(*ProductBascket.PRODUCT_PRISE)
            # name_book = self.browser.find_elements(*ProductBascket.PRODUCT_NAME)
            # link = self.browser.find_element(*ButtonClick.BUTTON_BUSKET).click()
            # self.solve_quiz_and_get_code()
            # busket = self.browser.find_element(*ProductBascket.BUSKET).click()
            # produst_price = self.browser.find_elements(*ProductBascket.PRODUCT_PRISE_BASKET)
            # name_basket = self.browser.find_elements(*ProductBascket.PRODUCT_NAME_BASKET)
            # self.browser.implicitly_wait(timeout= 3)
            # # f"{price},{produst_price}, {name_book}, {name_book}"
            # assert price in self.browser.find_elements(*ProductBascket.PRODUCT_PRISE_BASKET) , f"{price[0].text},{produst_price[0].text}"
            # # assert name_book in self.browser.find_elements(*ProductBascket.PRODUCT_NAME_BASKET) , f"{name_book}, {name_book}"

            
    def should_be_added_thing_in_basket(self):
        b_name = self.return_book_name()
        b_price = self.return_book_price()
        button_add_to_basket = self.browser.find_element(*ButtonClick.BUTTON_BUSKET)
        button_add_to_basket.click()
        #self.solve_quiz_and_get_code()
        #time.sleep(30)
        # self.should_be_thing_in_basket(b_name)
        # self.should_be_same_price(b_price)


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

  


    def return_book_name(self):
        book_name = self.browser.find_element(*ProductBascket.PRODUCT_NAME)
        return book_name.text

    def return_book_price(self):
        book_price = self.browser.find_element(*ProductBascket.PRODUCT_PRICE)
        return book_price.text

    def should_be_thing_in_basket(self, book_name):
        alert_book_name = self.browser.find_element(*ProductBascket.PRODUCT_NAME_BASKET)
        assert book_name == alert_book_name.text, "book name is {}, but alert book name is {}".format(book_name, alert_book_name.text)
        # main_book_name = self.browser.find_element(*ProductPageLocators.MAIN_BOOK_NAME)
        #assert main_book_name.text == alert_book_name.text, "book name is {}, but alert book name is {}".format(main_book_name.text, alert_book_name.text)

    def should_be_same_price(self, book_price):
        basket_price = self.browser.find_element(*ProductBascket.PRODUCT_PRICE_BASKET)
        assert basket_price.text == book_price, "basket prise is {}, but book price is {}".format(basket_price.text, book_price)
        # book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        # assert basket_price.text == book_price.text, "basket prise is {}, but book price is {}".format(basket_price.text, book_price.text)
       

        
        

        
         

    