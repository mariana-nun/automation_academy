from page_objects.home_page import HomePage
import os
from dotenv import load_dotenv
import configparser
from selenium import webdriver
from utils import get_capabilities

def before_all(context):
    load_dotenv()
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), '../setup.cfg'))
    context.execution = config.get("env", "execution")
    context.env = config.get("env", "environment")


def before_scenario(context, scenario):
    if f"skip_{context.env}" in scenario.effective_tags:
        scenario.skip(f"Marked with @skip_{context.env} tag in feature File")
        return
    else:
        base_url = os.environ[f"{context.env}_URL"]
        if context.execution == "browserstack":
            USERNAME = os.environ['BROWSERSTACK_USERNAME']
            BROWSERSTACK_ACCESS_KEY = os.environ["BROWSERSTACK_ACCESS_KEY"]
            url = "https://%s:%s@hub.browserstack.com/wd/hub" % (
                USERNAME, BROWSERSTACK_ACCESS_KEY
            )
            context.driver = webdriver.Remote(
                command_executor=url,
                desired_capabilities=get_capabilities()
                #                desired_capabilities= DesiredCapabilities.FIREFOX
            )
        else:
            context.driver = webdriver.Chrome('chromedriver.exe')
        context.page = HomePage(base_url, context.driver)


def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()
        if context.execution == "browserstack":
            if context.failed:
                context.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", '
                                              '"arguments": {"status":"failed", '
                                              '"reason": "At least 1 assertion failed"}}')
            else:
                context.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", '
                                              '"arguments": {"status":"passed", "reason": "All assertions passed"}}')
