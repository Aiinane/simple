from locators import BasketPageLokators
from base_page import BasePage



class BasketPage(BasePage):
    #Реализуйте там необходимые проверки, в том числе отрицательную, которую мы обсуждали в предыдущих шагах
    
    def basket_is_empty_text(self):
         assert "Your basket is empty" in self.browser.find_element(*BasketPageLokators.BASKET_EMPTY) , f"basket isn't empty" 

    

