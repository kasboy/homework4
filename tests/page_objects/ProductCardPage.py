from selenium.webdriver.common.by import By


class ProductCardPage:
    MAIN_PRODUCT_PHOTO = (By.CSS_SELECTOR, "ul.thumbnails > li:nth-child(1) > a")

    PHOTO_CARD1 = (By.CSS_SELECTOR, "ul.thumbnails > li:nth-child(2) > a > img")
    PHOTO_CARD2 = (By.CSS_SELECTOR, "ul.thumbnails > li:nth-child(3) > a > img")
    PHOTO_CARD3 = (By.CSS_SELECTOR, "ul.thumbnails > li:nth-child(4) > a > img")
    PHOTO_CARD4 = (By.CSS_SELECTOR, "ul.thumbnails > li:nth-child(5) > a > img")

    TAB_DESCRIPTION = (By.CSS_SELECTOR, "ul.nav.nav-tabs > li:nth-child(1) > a")
    TAB_DESCRIPTION_TEXT = (By.CSS_SELECTOR, "#tab-description > div")
    TAB_SPECIFICATION = (By.CSS_SELECTOR, "ul.nav.nav-tabs > li:nth-child(2) > a")
    TAB_REVIEWS = (By.CSS_SELECTOR, "ul.nav.nav-tabs > li:nth-child(3) > a")

    PRODUCT_TITLE = (By.CSS_SELECTOR, "div.col-sm-4 > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "ul.list-unstyled > li > h2")
    PRODUCT_PRICE_EX_TAX = (By.CSS_SELECTOR, "div.col-sm-4 > ul:nth-child(4) > li:nth-child(2)")
    PRODUCT_QTY_AREA = (By.CSS_SELECTOR, "#input-quantity")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#button-cart")



