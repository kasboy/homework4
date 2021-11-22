from selenium.webdriver.common.by import By


class FooterAreaPage:
    INFORMATION = (By.CSS_SELECTOR, "body > footer > div > div > div:nth-child(1) > h5")
    ABOUT_US_LINK = (By.LINK_TEXT, "About Us")

    CUSTOMER_SERVICE = (By.CSS_SELECTOR, "body > footer > div > div > div:nth-child(2) > h5")
    CONTACT_US_LINK = (By.LINK_TEXT, "Contact Us")

    EXTRAS = (By.CSS_SELECTOR, "body > footer > div > div > div:nth-child(3) > h5")
    BRANDS_US_LINK = (By.LINK_TEXT, "Brands")

    MY_ACCOUNT = (By.CSS_SELECTOR, "body > footer > div > div > div:nth-child(4) > h5")
    MY_ACCOUNT_LINK = (By.LINK_TEXT, "My Account")
