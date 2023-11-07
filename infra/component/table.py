from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from infra.po.abstract_component import AbsComponent


class Cell(AbsComponent):
    def __init__(self, driver: WebDriver, cell_locator: WebElement):
        super().__init__(driver, root=cell_locator)
        self._driver = driver
        self.cell_element = cell_locator

    def get_cell_text_content(self) -> str:
        return self.cell_element.text


class Row(AbsComponent):
    def __init__(self, driver: WebDriver, row_locator: WebElement):
        super().__init__(driver, root=row_locator)
        self._driver = driver
        self.row_element = row_locator

    def get_cell_by_index(self, index: int):
        cell_root = self.row_element.find_elements(By.XPATH, "td")[index - 1]
        return Cell(self._driver, cell_root)


class Table(AbsComponent):
    def __init__(self, driver: WebDriver, table_locator: WebElement):
        super().__init__(driver, root=table_locator)
        self._driver = driver
        self._table_element = table_locator

    def get_number_of_successful_transactions(self):
        rows = self._table_element.find_elements(By.CSS_SELECTOR, "tbody tr")
        num_of_successful_transactions: int = 0
        for row in rows:
            status: str = Row(self._driver, row). \
                get_cell_by_index(1). \
                get_cell_text_content()

            if status == "Complete":
                num_of_successful_transactions = num_of_successful_transactions + 1

        return num_of_successful_transactions
