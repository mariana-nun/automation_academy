from .base_page import BasePage
from selenium.webdriver.common.by import By
from .search_result_page import SearchResultsPage
from .account_page import AccountPage

class HomePage(BasePage):
    def __init__(self, url, context):
        super(HomePage, self).__init__(url, context)
        self.locators ={
            "offers_cards": (By.CSS_SELECTOR, "#htmlcontent_top"),
            "search_input": (By.CSS_SELECTOR, "#search_query_top"),
            "search_button": (By.CSS_SELECTOR, ".button-search"),
            "login_button": (By.XPATH, "//*[@title='Log in to your customer account']")
        }

    def go_to_the_home_page(self):
        self.web_driver.get(self.url)

    def wait_until_page_load(self):
        self.wait(self.locators["offers_cards"])

    def search(self, term):
        self.find_and_send_keys(self.locators["search_input"], term)
        self.find_and_click(self.locators["search_button"])
        return SearchResultsPage(self.url, self.web_driver)

    def go_to_login(self):
        self.find_and_click(self.locators["login_button"])
        return AccountPage(self.url, self.web_driver)

