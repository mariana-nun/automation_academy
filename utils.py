import configparser
import os
from configparser import NoOptionError
import logging


def get_capabilities():
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), './setup.cfg'))
    capabilities = ['os_name', 'os_version', 'browser', 'browser_version', 'name', 'build', 'project',
                    'browserstack.console', 'device']
    desired_capabilities = {}
    for capability in capabilities:
        try:
            if os.environ.get("IS_CI_EXECUTION", "no") == "yes":
                desired_capabilities[capability.replace("_name", "")] = os.environ[capability]
            else:
                desired_capabilities[capability.replace("_name", "")] = config.get("capabilities", capability)
        except (NoOptionError, KeyError):
            pass
    return desired_capabilities
