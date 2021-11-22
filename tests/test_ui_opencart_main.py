import time

from page_objects.MainPage import MainPage
from page_objects.FooterAreaMainPage import FooterAreaPage
from page_objects.TopAreaMainPage import TopAreaMainPage

# Additional Arguments example: --browser chrome/opera/firefox/safari --maximized --headless --url=https://yandex.ru
def test_main_page_first_test(browser, url):
    browser.get(url)
    # browser.implicitly_wait(5)
    # time.sleep(5)
    # browser.save_screenshot("example.png")
    assert browser.title == "Your Store"


def test_main_page_currency(browser, url):
    browser.implicitly_wait(5)
    browser.get(url)
    browser.find_element(*TopAreaMainPage.TOP_CURRENCY_DROP_DOWN).click()
    time.sleep(2)
    browser.find_element(*TopAreaMainPage.TOP_CURRENCY_DROP_DOWN).click()

    time.sleep(2)  # Для демонстрации


def test_main_page_search(browser, url):
    browser.implicitly_wait(5)
    browser.get(url)
    time.sleep(2)
    browser.find_element(*TopAreaMainPage.TOP_SEARCH_INPUT).send_keys("iphone")
    browser.find_element(*TopAreaMainPage.TOP_SEARCH_BUTTON).click()
    time.sleep(2)  # Для демонстрации


def test_main_page_shopping_cart(browser, url):
    # browser.implicitly_wait(5)
    browser.get(url)
    browser.find_element(*TopAreaMainPage.TOP_USER_SHOPPING_CART_BUTTON)
    time.sleep(2)  # Для демонстрации


def test_main_page_logo(browser, url):
    # browser.implicitly_wait(5)
    browser.get(url)
    browser.find_element(*TopAreaMainPage.TOP_LOGO)
    time.sleep(2)  # Для демонстрации


def test_main_page_top_main_menu(browser, url):
    # browser.implicitly_wait(5)
    browser.get(url)
    browser.find_element(*TopAreaMainPage.TOP_MAIN_MENU)
    browser.find_element(*TopAreaMainPage.TOP_MAIN_MENU_DESKTOP_ITEM)
    browser.find_element(*TopAreaMainPage.TOP_MAIN_MENU_LAPTOPS_ITEM)
    browser.find_element(*TopAreaMainPage.TOP_MAIN_MENU_COMPONENTS_ITEM)
    browser.find_element(*TopAreaMainPage.TOP_MAIN_MENU_TABLETS_ITEM)
    time.sleep(2)  # Для демонстрации


def test_main_page_slide_show_top(browser, url):
    # browser.implicitly_wait(5)
    browser.get(url)
    browser.find_element(*MainPage.SLIDE_SHOW_TOP)
    time.sleep(2)  # Для демонстрации


def test_main_page_feature_cards(browser, url):
    browser.implicitly_wait(5)
    browser.get(url)
    browser.find_element(*MainPage.FEATURED_CARD1).click()
    browser.back()
    browser.find_element(*MainPage.FEATURED_CARD2).click()
    browser.execute_script("window.history.go(-1)")  # Use JavaScript to go back one step in the history of the browser
    browser.find_element(*MainPage.FEATURED_CARD3).click()
    browser.execute_script("window.history.go(-1)")
    browser.find_element(*MainPage.FEATURED_CARD4).click()
    browser.execute_script("window.history.go(-1)")
    time.sleep(2)  # Для демонстрации


def test_main_page_slide_show_bottom(browser, url):
    # browser.implicitly_wait(5)
    browser.get(url)
    browser.find_element(*MainPage.SLIDE_SHOW_BOTTOM)
    time.sleep(2)  # Для демонстрации


def test_main_page_bottom_links(browser, url):
    browser.implicitly_wait(5)
    browser.get(url)
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
