from .base_page import BasePage
from selenium.webdriver.common.by import By
from .search_result_page import SearchResultsPage
from random import randint


class AccountPage(BasePage):
    def __init__(self, url, context):
        super(AccountPage, self).__init__(url, context)
        self.locators = {
            "email_create_input": (By.CSS_SELECTOR, "#email_create"),
            "create_account_button": (By.CSS_SELECTOR, "#SubmitCreate"),
            "gender": "#uniform-id_gender{}",
            "first_name": (By.CSS_SELECTOR, "#customer_firstname"),
            "last_name": (By.CSS_SELECTOR, "#customer_lastname"),
            "password": (By.CSS_SELECTOR, "#passwd"),
            "day": (By.CSS_SELECTOR, "#days"),
            "month": (By.CSS_SELECTOR, "#months"),
            "year": (By.CSS_SELECTOR, "#years"),
            "address": (By.CSS_SELECTOR, "#address1"),
            "city": (By.CSS_SELECTOR, "#city"),
            "state": (By.CSS_SELECTOR, "#id_state"),
            "postcode": (By.CSS_SELECTOR, "#postcode"),
            "country": (By.CSS_SELECTOR, "#id_country"),
            "phone": (By.CSS_SELECTOR, "#phone"),
            "phone_mobile": (By.CSS_SELECTOR, "#phone_mobile"),
            "sent_account_data_button": (By.CSS_SELECTOR, "#submitAccount"),
            "sign_in_email_input": (By.CSS_SELECTOR, "#email"),
            "login_button": (By.CSS_SELECTOR, "#SubmitLogin"),
            "my_account_title": (By.XPATH, "//h1[@class='page-heading']"),
            "user_names": (By.CSS_SELECTOR, ".header_user_info .account"),
        }

    def wait_until_page_load(self):
        self.wait(self.locators["create_account_button"])

    def create_account(self, email):
        email = f"{randint(9999, 99999999)}test_accoun@test.com" if email == "random" else email
        self.find_and_send_keys(self.locators["email_create_input"], email)
        self.find_and_click(self.locators["create_account_button"])

    def complete_account_creation_form(self, data):
        gender = 1 if "gender" in data and data["gender"].lower == "mr" else 2
        self.find_and_click((By.CSS_SELECTOR, self.locators["gender"].format(gender)))
        self.find_and_send_keys(self.locators["first_name"], data["first_name"])
        self.find_and_send_keys(self.locators["last_name"], data["last_name"])
        self.find_and_send_keys(self.locators["password"], data["password"])
        self.select_by_value(self.locators["day"], data["day"])
        self.select_by_value(self.locators["month"], data["month"])
        self.select_by_value(self.locators["year"], data["year"])
        self.find_and_send_keys(self.locators["address"], data["address"])
        self.find_and_send_keys(self.locators["city"], data["city"])
        self.select_by_value(self.locators["state"], data["state"])
        self.select_by_value(self.locators["country"], data["country"])
        self.find_and_send_keys(self.locators["postcode"], data["postcode"])
        self.find_and_send_keys(self.locators["phone_mobile"], data["phone_mobile"])
        self.find_and_click(self.locators["sent_account_data_button"])

    def sign_in(self, email, password):
        self.find_and_send_keys(self.locators["sign_in_email_input"], email)
        self.find_and_send_keys(self.locators["password"], password)
        self.find_and_click(self.locators["login_button"])

    def check_correct_login(self):
        self.wait(self.locators["my_account_title"])
        return self.get_text(self.locators["user_names"])

