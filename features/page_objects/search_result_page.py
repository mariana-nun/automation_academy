from .base_page import BasePage
from selenium.webdriver.common.by import By


class SearchResultsPage(BasePage):
    def __init__(self, url, context):
        super(SearchResultsPage, self).__init__(url, context)
        self.locators = {
            "result_cards": (By.XPATH, "//a[@class='product_img_link']/img"),
            "no_results_message": (By.CSS_SELECTOR, ".alert-warning"),
            "result_quantity": (By.CSS_SELECTOR, ".heading-counter")
        }

    def get_search_results(self):
        self.wait(self.locators["result_cards"])
        return self.wait_and_find_elements(self.locators["result_cards"])

    def get_result_quantity(self):
        self.wait(self.locators["result_quantity"])
        return self.get_text(self.locators["result_quantity"])

    def get_no_result_message(self):
        return self.get_text(self.locators["no_results_message"])
