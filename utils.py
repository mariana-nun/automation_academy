import configparser
import os
from configparser import NoOptionError


def get_capabilities():
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), './setup.cfg'))
    capabilities = ['os', 'os_version', 'browser', 'browser_version', 'name', 'build', 'project',
                    'browserstack.console', 'device']
    desired_capabilities = {}
    for capability in capabilities:
        try:
            desired_capabilities[capability] = config.get("capabilities", capability)
        except NoOptionError:
            pass
    return desired_capabilities
