from .base_page import BasePage
from selenium.webdriver.common.by import By
from .search_result_page import SearchResultsPage

class HomePage(BasePage):
    def __init__(self, url, context):
        super(HomePage, self).__init__(url, context)
        self.locators ={
            "destination": (By.CSS_SELECTOR, "#location-field-destination-menu button"),
            "start_date": (By.CSS_SELECTOR, "#d1"),
            "end_date": (By.CSS_SELECTOR, "#d2"),
            "submit_button": (By.CSS_SELECTOR, ".uitk-layout-grid-item-columnspan-large-2 .uitk-button"),
            "suggestion": (By.CSS_SELECTOR, '.uitk-menu-open li.uitk-typeahead-result-item'),
            "suggestion_icon": (By.CSS_SELECTOR, ".uitk-menu-open li.uitk-typeahead-result-item .uitk-icon-leading"),
            "suggestion_by_text": '//*[text()="Search for “{}”"]',
            "option_icon": (By.CSS_SELECTOR, "li[class*='active']"),
            "tab_button": '//*[@id="uitk-tabs-button-container"]//*[text()="{}"]',
            "cars_origin": (By.CSS_SELECTOR, "#location-field-locn-menu button"),
            "cars_destination": (By.CSS_SELECTOR, "#location-field-loc2-menu button")
        }

    def go_to_the_home_page(self):
        self.web_driver.get(self.url)

    def wait_until_page_load(self):
        self.wait(self.locators["submit_button"])

    def sent_travel_data(self, destination):
        self.find_and_send_keys(self.locators["destination"], destination)
        self.find_and_click(self.locators["suggestion"])
        self.find_and_click(self.locators["submit_button"])
        return SearchResultsPage(self.url, self.web_driver)

    def search_cars(self, origin, destination):
        self.find_and_click((By.XPATH, self.locators["tab_button"].format("Cars")))
        self.find_and_send_keys(self.locators["cars_origin"], origin)
        self.wait(self.locators["suggestion_icon"])
        self.find_and_click(self.locators["suggestion"])
        self.find_and_send_keys(self.locators["cars_destination"], destination)
        self.wait(self.locators["suggestion_icon"])
        self.find_and_click(self.locators["suggestion"])
        self.find_and_click(self.locators["submit_button"])
        return SearchResultsPage(self.url, self.web_driver)
