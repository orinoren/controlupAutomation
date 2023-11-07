from selenium.common import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ActionBot:
    def __init__(self, driver):
        self.driver = driver

    def click(self,
              locator: tuple,
              timeout=30,
              element_name: str = ""):
        element: WebElement = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()
        print(f"Click on {element_name}")

    def send_keys(self,
                  locator: tuple,
                  text, timeout=30,
                  element_name: str = ""):
        element: WebElement = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        element.send_keys(text)
        print(f"Fill {element_name} : {text}")

    def is_displayed(self,
                     locator: tuple,
                     timeout: int = 30,
                     element_name: str = "") -> bool:
        element: WebElement = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        displayed = element.is_displayed()
        print(f"Verifying {element_name} is displayed : {displayed}")
        return displayed

    def wait_until_element_is_visible(self,
                                      locator: tuple,
                                      timeout: int = 30,
                                      throw_exception: bool = True,
                                      element_name: str = "") -> bool:
        try:
            print(f"Waiting for {element_name} to be visible")
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            print(f"{element_name} is visible")
            return True
        except TimeoutException as e:
            if throw_exception:
                raise e

            print(f"{element_name} is not visible")
            return False

    def find_element(self,
                     locator: tuple,
                     timeout: int = 30,
                     throw_exception: bool = True,
                     element_name: str = "") -> WebElement:
        try:
            print(f"Trying to find {element_name} with locator -> {locator} ")
            element: WebElement = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            print(f"{element_name} as found")
            return element
        except TimeoutException as e:
            print(f"{element_name} not found")
            if throw_exception:
                raise e
