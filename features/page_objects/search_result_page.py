from .base_page import BasePage
from selenium.webdriver.common.by import By


class SearchResultsPage(BasePage):
    def __init__(self, url, context):
        super(SearchResultsPage, self).__init__(url, context)
        self.locators = {
            "hotels_result_cards": (By.CSS_SELECTOR, ".results-list .uitk-card-link"),
            "cars_result_cards": (By.XPATH, "//ol[contains(@class, results-list)]/li"),
            "no_hotel_results_message": (By.CSS_SELECTOR, "div.uitk-empty-state-heading"),
            "no_car_results_message": (By.CSS_SELECTOR, ".uitk-error-summary-description")
        }

    def get_search_results(self, type):
        self.wait(self.locators[f"{type}_result_cards"])
        return self.wait_and_find_elements(self.locators[f"{type}_result_cards"])

    def get_the_no_result_message(self, type):
        return self.get_text(self.locators[f"no_{type}_results_message"])
