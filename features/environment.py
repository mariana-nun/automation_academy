from page_objects.home_page import HomePage
import os
from dotenv import load_dotenv
import configparser
from selenium import webdriver


def before_all(context):
    load_dotenv()
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), '../setup.cfg'))
    context.env = config.get("env", "environment")


def before_scenario(context, scenario):
    if f"skip_{context.env}" in scenario.effective_tags:
        scenario.skip(f"Marked with @skip_{context.env} tag in feature File")
        return
    else:
        base_url = os.environ[f"{context.env}_URL"]
        context.driver = webdriver.Chrome('chromedriver.exe')
        context.page = HomePage(base_url, context.driver)


def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()
