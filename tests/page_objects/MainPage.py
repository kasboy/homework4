from selenium.webdriver.common.by import By


class MainPage:
    SLIDE_SHOW_TOP = (By.CSS_SELECTOR, "#slideshow0")

    FEATURED_CARD1 = (By.CSS_SELECTOR, "div:nth-child(1) > div > div.image > a > img")
    FEATURED_CARD2 = (By.CSS_SELECTOR, "div:nth-child(2) > div > div.image > a > img")
    FEATURED_CARD3 = (By.CSS_SELECTOR, "div:nth-child(3) > div > div.image > a > img")
    FEATURED_CARD4 = (By.CSS_SELECTOR, "div:nth-child(4) > div > div.image > a > img")

    SLIDE_SHOW_BOTTOM = (By.CSS_SELECTOR, "#carousel0")


