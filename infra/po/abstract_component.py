from abc import ABC

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from infra.helpers.action_bot import ActionBot


class AbsComponent(ABC):

    def __init__(self, driver: WebDriver, root: WebElement = None):
        self._driver = driver
        self._bot = ActionBot(driver)
        if root:
            self._root = root
