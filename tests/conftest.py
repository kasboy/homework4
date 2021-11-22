import os
import pytest

from selenium import webdriver
from selenium.webdriver.opera.options import Options as OperaOptions
from selenium.webdriver.safari.options import Options as SafariOptions

DRIVERS = os.path.expanduser("~/Downloads/soft/drivers")


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox", "opera", "safari"])
    # parser.addoption("--browser", action="store", default="chrome", required = True)
    parser.addoption("--url", action="store", default="https://demo.opencart.com/")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    # https://github.com/SeleniumHQ/selenium/wiki/DesiredCapabilities
    maximized = request.config.getoption("--maximized")

    driver = None

    if _browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.headless = True
        driver = webdriver.Chrome(executable_path=f"{DRIVERS}/chromedriver", options=options)
    elif _browser == "opera":
        options = OperaOptions()
        if headless:
            options.headless = True
        driver = webdriver.Opera(executable_path=f"{DRIVERS}/operadriver", options=options)
    elif _browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.headless = True
        driver = webdriver.Firefox(executable_path=f"{DRIVERS}/geckodriver", options=options)
    elif _browser == "safari":
        options = SafariOptions()
        if headless:
            options.headless = True
        driver = webdriver.Safari(options=options)

    if maximized:
        driver.maximize_window()

    def final():
        driver.quit()

    request.addfinalizer(final)

    return driver
