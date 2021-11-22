from selenium.webdriver.common.by import By


class TopAreaMainPage:
    TOP_CURRENCY_DROP_DOWN = (By.CSS_SELECTOR, " #form-currency > div > button > span")

    TOP_SEARCH_INPUT = (By.CSS_SELECTOR, "#search > input")
    TOP_SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='button'].btn.btn-default.btn-lg")

    TOP_USER_SHOPPING_CART_BUTTON = (By.CSS_SELECTOR,
                                 "button[type='button'].btn.btn-inverse.btn-block.btn-lg.dropdown-toggle")

    TOP_LOGO = (By.CSS_SELECTOR, "#logo")

    TOP_MAIN_MENU = (By.CSS_SELECTOR, "div.collapse.navbar-collapse.navbar-ex1-collapse")
    TOP_MAIN_MENU_DESKTOP_ITEM = (By.CSS_SELECTOR, "ul.nav.navbar-nav > li:nth-child(1) > a")
    TOP_MAIN_MENU_LAPTOPS_ITEM = (By.CSS_SELECTOR, "ul.nav.navbar-nav > li:nth-child(2) > a")
    TOP_MAIN_MENU_COMPONENTS_ITEM = (By.CSS_SELECTOR, "ul.nav.navbar-nav > li:nth-child(3) > a")
    TOP_MAIN_MENU_TABLETS_ITEM = (By.CSS_SELECTOR, "ul.nav.navbar-nav > li:nth-child(4) > a")