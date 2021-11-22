import time

from page_objects.FooterAreaMainPage import FooterAreaPage
from page_objects.TopAreaMainPage import TopAreaMainPage
from page_objects.ProductCatalogPage import ProductCatalogPage

def test_product_catalog_test_first_test(browser, url):
    # time.sleep(2)
    browser.implicitly_wait(5)
    browser.get(url + "/index.php?route=product/category&path=20")
    time.sleep(2)
    # browser.save_screenshot("example.png")
    # Additional Arguments example: --browser chrome/firefox --maximized --headless --url=https://yandex.ru
    assert browser.title == "Desktops"


def test_product_catalog_page_currency(browser, url):
    browser.implicitly_wait(5)
    browser.get(url + "/index.php?route=product/category&path=20")
    browser.find_element(*TopAreaMainPage.TOP_CURRENCY_DROP_DOWN).click()
    time.sleep(2)
    browser.find_element(*TopAreaMainPage.TOP_CURRENCY_DROP_DOWN).click()
    time.sleep(2)  # Для демонстрации


def test_product_catalog_page_search(browser, url):
    browser.implicitly_wait(5)
    browser.get(url + "/index.php?route=product/category&path=20")
    time.sleep(2)
    browser.find_element(*TopAreaMainPage.TOP_SEARCH_INPUT).send_keys("iphone")
    browser.find_element(*TopAreaMainPage.TOP_SEARCH_BUTTON).click()
    time.sleep(2)  # Для демонстрации


def test_product_catalog_page_shopping_cart(browser, url):
    # browser.implicitly_wait(5)
    browser.get(url + "/index.php?route=product/category&path=20")
    browser.find_element(*TopAreaMainPage.TOP_USER_SHOPPING_CART_BUTTON)
    time.sleep(2)  # Для демонстрации


def test_product_catalog_page_logo(browser, url):
    # browser.implicitly_wait(5)
    browser.get(url + "/index.php?route=product/category&path=20")
    browser.find_element(*TopAreaMainPage.TOP_LOGO)
    time.sleep(2)  # Для демонстрации


def test_product_catalog_page_top_main_menu(browser, url):
    # browser.implicitly_wait(5)
    browser.get(url + "/index.php?route=product/category&path=20")
    browser.find_element(*TopAreaMainPage.TOP_MAIN_MENU)
    browser.find_element(*TopAreaMainPage.TOP_MAIN_MENU_DESKTOP_ITEM)
    browser.find_element(*TopAreaMainPage.TOP_MAIN_MENU_LAPTOPS_ITEM)
    browser.find_element(*TopAreaMainPage.TOP_MAIN_MENU_COMPONENTS_ITEM)
    browser.find_element(*TopAreaMainPage.TOP_MAIN_MENU_TABLETS_ITEM)
    time.sleep(2)  # Для демонстрации


def test_product_catalog_page_breadcrumb(browser, url):
    # browser.implicitly_wait(5)
    browser.get(url + "/index.php?route=product/category&path=20")
    browser.find_element(*ProductCatalogPage.BREADCRUMB)
    time.sleep(2)  # Для демонстрации


def test_product_catalog_page_left_menu(browser, url):
    # browser.implicitly_wait(5)
    browser.get(url + "/index.php?route=product/category&path=20")
    browser.find_element(*ProductCatalogPage.LEFT_MENU)
    browser.find_element(*ProductCatalogPage.LEFT_MENU_IMG)
    time.sleep(2)  # Для демонстрации


def test_product_catalog_title(browser, url):
    # browser.implicitly_wait(5)
    browser.get(url + "/index.php?route=product/category&path=20")
    browser.find_element(*ProductCatalogPage.TITLE_SECTION)
    browser.find_element(*ProductCatalogPage.SECTION_IMG)
    browser.find_element(*ProductCatalogPage.TITLE_SECTION_DESCRIPTION)

    browser.find_element(*ProductCatalogPage.REFINE_SEARCH_TITLE)
    browser.find_element(*ProductCatalogPage.REFINE_SEARCH_CATEGORY1)
    browser.find_element(*ProductCatalogPage.REFINE_SEARCH_CATEGORY2)
    time.sleep(2)  # Для демонстрации



def test_product_catalog_catalog_table(browser, url):
    browser.implicitly_wait(5)
    browser.get(url + "/index.php?route=product/category&path=20")
    browser.find_element(*ProductCatalogPage.VIEW_TYPE_LIST)
    browser.find_element(*ProductCatalogPage.VIEW_TYPE_GRID)

    browser.find_element(*ProductCatalogPage.PRODUCT_COMPARE)

    browser.find_element(*ProductCatalogPage.TABLE_HEADER)
    browser.find_element(*ProductCatalogPage.SORT_BY_KEY)
    browser.find_element(*ProductCatalogPage.SORT_BY_VALUE)
    browser.find_element(*ProductCatalogPage.SHOW_KEY)
    browser.find_element(*ProductCatalogPage.SHOW_VALUE)
    time.sleep(2)  # Для демонстрации


def test_product_catalog_catalog_items(browser, url):
    browser.implicitly_wait(5)
    browser.get(url + "/index.php?route=product/category&path=20")
    browser.find_element(*ProductCatalogPage.VIEW_TYPE_LIST)
    browser.find_element(*ProductCatalogPage.VIEW_TYPE_GRID)

    browser.find_element(*ProductCatalogPage.PRODUCT_COMPARE)

    browser.find_element(*ProductCatalogPage.PRODUCT_CARD1)
    browser.find_element(*ProductCatalogPage.PRODUCT_CARD2)
    browser.find_element(*ProductCatalogPage.PRODUCT_CARD3)
    time.sleep(2)  # Для демонстрации


def test_product_catalog_page_bottom_links(browser, url):
    browser.implicitly_wait(5)
    browser.get(url + "/index.php?route=product/category&path=20")
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