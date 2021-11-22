import time

from page_objects.MainAdminPage import MainAdminPage

def test_first_test(browser, url):
    # time.sleep(5)
    browser.get(url)
    time.sleep(5)

    # browser.save_screenshot("example.png")
    # Additional Arguments example: --browser chrome/firefox --maximized --headless --url=https://yandex.ru
    assert browser.title == "Your Store"

def test_main_admin_page(browser, url):
    browser.get(url + "/admin")
    browser.find_element(*MainAdminPage.USERNAME_INPUT)
    browser.find_element(*MainAdminPage.PASSWORD_INPUT)
    browser.find_element(*MainAdminPage.SUBMIT_BUTTON)
    browser.find_element(*MainAdminPage.FORGOTTEN_PASSWORD)
    browser.find_element(*MainAdminPage.OPENCART_LINK)
    time.sleep(2)  # Для демонстрации
