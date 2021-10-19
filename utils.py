import configparser
import os
from configparser import NoOptionError
import logging
import json

"""
For local parallel execution put the EXECUTION=local on the setup file and the environment variable PARALLEL_EXECUTION=no
"""


def get_capabilities():
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), './setup.cfg'))
    capabilities = ['os_name', 'os_version', 'browser', 'browser_version', 'name', 'build', 'project',
                    'browserstack.console', 'device']
    desired_capabilities = {}
    if os.environ.get("PARALLEL_EXECUTION", "no") == "yes":
        TASK_ID = int(os.environ['TASK_ID']) if 'TASK_ID' in os.environ else 0
        with open("browsers.json", "r") as f:
            capabilities = json.loads(f.read())
        f.close()
        desired_capabilities = capabilities["environments"][TASK_ID]
        for key in capabilities["capabilities"]:
            if key not in desired_capabilities:
                desired_capabilities[key] = capabilities["capabilities"][key]
    else:
        for capability in capabilities:
            try:
                if os.environ.get("IS_CI_EXECUTION", "no") == "yes":
                    desired_capabilities[capability.replace("_name", "")] = os.environ[capability]
                else:
                    desired_capabilities[capability.replace("_name", "")] = config.get("capabilities", capability)
            except (NoOptionError, KeyError):
                pass
    return desired_capabilities


def get_sauce_capabilities():
    sauce_capabilities = ['browserName', 'platform', 'version', 'build', 'name', 'platformName', 'platformVersion',
                          'appiumVersion', 'deviceName', 'browserName']
    desired_capabilities = {}
    if os.environ.get("PARALLEL_EXECUTION", "no") == "yes":
        TASK_ID = int(os.environ['TASK_ID']) if 'TASK_ID' in os.environ else 0
        with open("sauce_labs_browsers.json", "r") as f:
            capabilities = json.loads(f.read())
        f.close()
        desired_capabilities = capabilities["environments"][TASK_ID]
        for key in capabilities["capabilities"]:
            if key not in desired_capabilities:
                desired_capabilities[key] = capabilities["capabilities"][key]
    else:
        for capability in sauce_capabilities:
            try:
                if os.environ.get("IS_CI_EXECUTION", "no") == "yes":
                    desired_capabilities[capability.replace(".", ":")] = os.environ[capability]
                else:
                    config = configparser.ConfigParser()
                    config.read(os.path.join(os.path.dirname(__file__), './setup.cfg'))
                    desired_capabilities[capability.replace(".", ":")] = config.get("capabilities", capability)
            except (NoOptionError, KeyError):
                pass
    return desired_capabilities