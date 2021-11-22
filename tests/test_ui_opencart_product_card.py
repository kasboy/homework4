import time
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from page_objects.FooterAreaMainPage import FooterAreaPage
from page_objects.TopAreaMainPage import TopAreaMainPage
from page_objects.ProductCardPage import ProductCardPage


def test_product_card_test_first_test(browser, url):
    # time.sleep(2)
    browser.implicitly_wait(5)
    browser.get(url + "/index.php?route=product/product&product_id=43")
    time.sleep(2)
    # browser.save_screenshot("example.png")
    # Additional Arguments example: --browser chrome/firefox --maximized --headless --url=https://yandex.ru
    assert browser.title == "MacBook"


def test_product_card_page_currency(browser, url):
    browser.implicitly_wait(5)
    browser.get(url + "/index.php?route=product/product&product_id=43")
    browser.find_element(*TopAreaMainPage.TOP_CURRENCY_DROP_DOWN).click()
    time.sleep(2)
    browser.find_element(*TopAreaMainPage.TOP_CURRENCY_DROP_DOWN).click()

    time.sleep(2)  # Для демонстрации


def test_product_card_page_search(browser, url):
    browser.implicitly_wait(5)
    browser.get(url + "/index.php?route=product/product&product_id=43")
    time.sleep(2)
    browser.find_element(*TopAreaMainPage.TOP_SEARCH_INPUT).send_keys("iphone")
    browser.find_element(*TopAreaMainPage.TOP_SEARCH_BUTTON).click()
    time.sleep(2)  # Для демонстрации


def test_product_card_page_shopping_cart(browser, url):
    # browser.implicitly_wait(5)
    browser.get(url + "/index.php?route=product/product&product_id=43")
    browser.find_element(*TopAreaMainPage.TOP_USER_SHOPPING_CART_BUTTON)
    time.sleep(2)  # Для демонстрации


def test_product_card_page_logo(browser, url):
    # browser.implicitly_wait(5)
    browser.get(url + "/index.php?route=product/product&product_id=43")
    browser.find_element(*TopAreaMainPage.TOP_LOGO)
    time.sleep(2)  # Для демонстрации


def test_product_card_page_top_main_menu(browser, url):
    # browser.implicitly_wait(5)
    browser.get(url + "/index.php?route=product/product&product_id=43")
    browser.find_element(*TopAreaMainPage.TOP_MAIN_MENU)
    browser.find_element(*TopAreaMainPage.TOP_MAIN_MENU_DESKTOP_ITEM)
    browser.find_element(*TopAreaMainPage.TOP_MAIN_MENU_LAPTOPS_ITEM)
    browser.find_element(*TopAreaMainPage.TOP_MAIN_MENU_COMPONENTS_ITEM)
    browser.find_element(*TopAreaMainPage.TOP_MAIN_MENU_TABLETS_ITEM)
    time.sleep(2)  # Для демонстрации


def test_product_card_page_main_product_photo(browser, url):
    # browser.implicitly_wait(5)
    browser.get(url + "/index.php?route=product/product&product_id=43")
    browser.find_element(*ProductCardPage.MAIN_PRODUCT_PHOTO).click()
    time.sleep(2)  # Для демонстрации


def test_product_card_page_photo_cards(browser, url):
    browser.implicitly_wait(5)
    browser.get(url + "/index.php?route=product/product&product_id=43")
    photo_card1 = browser.find_element(*ProductCardPage.PHOTO_CARD1)
    photo_card1.click()
    time.sleep(2)
    webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
    photo_card2 = browser.find_element(*ProductCardPage.PHOTO_CARD2)
    photo_card2.click()
    time.sleep(2)
    webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
    photo_card3 = browser.find_element(*ProductCardPage.PHOTO_CARD3)
    photo_card3.click()
    time.sleep(2)
    webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
    photo_card4 = browser.find_element(*ProductCardPage.PHOTO_CARD4)
    photo_card4.click()
    time.sleep(2)
    webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
    time.sleep(2)  # Для демонстрации


def test_product_card_page_product_tabs(browser, url):
    browser.implicitly_wait(5)
    browser.get(url + "/index.php?route=product/product&product_id=43")
    browser.find_element(*ProductCardPage.TAB_DESCRIPTION).click()
    time.sleep(2)
    browser.find_element(*ProductCardPage.TAB_DESCRIPTION_TEXT)
    time.sleep(2)
    browser.find_element(*ProductCardPage.TAB_SPECIFICATION).click()
    time.sleep(2)
    browser.find_element(*ProductCardPage.TAB_REVIEWS).click()
    time.sleep(2)  # Для демонстрации


def test_product_card_page_product_attr(browser, url):
    browser.implicitly_wait(5)
    browser.get(url + "/index.php?route=product/product&product_id=43")
    browser.find_element(*ProductCardPage.PRODUCT_TITLE)
    browser.find_element(*ProductCardPage.PRODUCT_PRICE)
    browser.find_element(*ProductCardPage.PRODUCT_PRICE_EX_TAX)
    browser.find_element(*ProductCardPage.PRODUCT_QTY_AREA).send_keys("2")
    time.sleep(2)
    browser.find_element(*ProductCardPage.ADD_TO_CART_BUTTON).click()
    time.sleep(2)
    browser.find_element(*ProductCardPage.USER_SHOPPING_CART).click()
    time.sleep(5)  # Для демонстрации


def test_product_card_page_bottom_links(browser, url):
    browser.implicitly_wait(5)
    browser.get(url + "/index.php?route=product/product&product_id=43")
    browser.find_element(*FooterAreaPage.INFORMATION)
    browser.find_element(*FooterAreaPage.ABOUT_US_LINK).click()
    time.sleep(2)
    browser.back()
    browser.find_element(*FooterAreaPage.CUSTOMER_SERVICE)
    browser.find_element(*FooterAreaPage.CONTACT_US_LINK).click()
    time.sleep(2)
    browser.back()
    browser.find_element(*FooterAreaPage.EXTRAS)
    browser.find_element(*FooterAreaPage.BRANDS_US_LINK).click()
    time.sleep(2)
    browser.back()
    browser.find_element(*FooterAreaPage.MY_ACCOUNT)
    browser.find_element(*FooterAreaPage.MY_ACCOUNT_LINK).click()
    time.sleep(2)
    browser.back()
    time.sleep(2)  # Для демонстрации
