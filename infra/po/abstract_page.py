from selenium.webdriver.chrome.webdriver import WebDriver

from infra.po.abstract_component import AbsComponent


class AbsPage(AbsComponent):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)


