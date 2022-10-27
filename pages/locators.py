from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") #теперь каждый селектор — это пара: как искать и что искать. 

class LoginPageLocators ():
    LOGIN_FORM = (By.ID, "login_form")
    REGISER_FORM = (By.ID, "register_form")

class ButtonClick ():
    BUTTON_BUSKET =  (By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']")

class ProductBascket ():
    PRODUCT_PRICE =(By.CSS_SELECTOR, "p.price_color:nth-child(2)") 
    PRODUCT_PRICE_BASKET = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info.fade.in:nth-child(3) div.alertinner p:nth-child(1) > strong:nth-child(1)")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div[class='col-sm-6 product_main'] > h1")
    PRODUCT_NAME_BASKET = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1) div.alertinner > strong:nth-child(1)")
    BUSKET = (By.CSS_SELECTOR, "a[class='btn btn-default']")

class AlertSelector ():
    SELECTOR_ALERT = (By.CSS_SELECTOR, ".alert-success")
    #.alert-success
    #div.alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1) > div.alertinner
class BasePageLocators ():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLokators():
    BASKET_LINK = (By.CSS_SELECTOR,"span.btn-group:nth-child(2) > a.btn.btn-default:nth-child(1)")
    BASKET_EMPTY = (By.CSS_SELECTOR,"div.page_inner div.content:nth-child(4) div:nth-child(2) > p:nth-child(1)") ##content_inner
