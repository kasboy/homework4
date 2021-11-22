from selenium.webdriver.common.by import By


class ProductCatalogPage:
    BREADCRUMB = (By.CSS_SELECTOR, "#product-category > ul")

    LEFT_MENU = (By.CSS_SELECTOR, "#column-left")
    LEFT_MENU_IMG = (By.CSS_SELECTOR, "#banner0 > div > div > a > img")

    TITLE_SECTION = (By.CSS_SELECTOR, "#content > h2")
    SECTION_IMG = (By.CSS_SELECTOR, "#content > div:nth-child(2) > div.col-sm-2 > img")
    TITLE_SECTION_DESCRIPTION = (By.CSS_SELECTOR, "#content > div:nth-child(2) > div.col-sm-10 > p")

    REFINE_SEARCH_TITLE = (By.CSS_SELECTOR, "#content > h3")
    REFINE_SEARCH_CATEGORY1 = (By.CSS_SELECTOR, "#content > div:nth-child(5) > div > ul > li:nth-child(1)")
    REFINE_SEARCH_CATEGORY2 = (By.CSS_SELECTOR, "#content > div:nth-child(5) > div > ul > li:nth-child(2)")

    VIEW_TYPE_LIST = (By.CSS_SELECTOR, "#list-view")
    VIEW_TYPE_GRID = (By.CSS_SELECTOR, "#grid-view")

    PRODUCT_COMPARE = (By.LINK_TEXT, "Product Compare (0)")

    TABLE_HEADER = (By.CSS_SELECTOR, "#content > div:nth-child(6)")
    SORT_BY_KEY = (By.CSS_SELECTOR, "#content > div:nth-child(6) > div.col-md-4.col-xs-6 > div > label")
    SORT_BY_VALUE = (By.CSS_SELECTOR, "#input-sort")
    SHOW_KEY = (By.CSS_SELECTOR, "#content > div:nth-child(6) > div.col-md-3.col-xs-6 > div > label")
    SHOW_VALUE = (By.CSS_SELECTOR, "#input-limit")

    PRODUCT_CARD1 = (By.CSS_SELECTOR, "#content > div:nth-child(7) > div:nth-child(1)")
    PRODUCT_CARD2 = (By.CSS_SELECTOR, "#content > div:nth-child(7) > div:nth-child(2)")
    PRODUCT_CARD3 = (By.CSS_SELECTOR, "#content > div:nth-child(7) > div:nth-child(3)")




