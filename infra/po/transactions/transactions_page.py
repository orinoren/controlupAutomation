from selenium.webdriver.common.by import By

from infra.component.table import Table
from infra.po.abstract_page import AbsPage


class TransactionsPage(AbsPage):
    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self._transactions_table = By.CSS_SELECTOR, 'table.table'
        self.wait_until_transactions_table_is_visible()

    def wait_until_transactions_table_is_visible(self):
        self._bot.wait_until_element_is_visible(self._transactions_table, element_name="transactions_table")
        print(f"Waiting until transactions table is visible")
        return self

    def get_transactions_table(self):
        return Table(self._driver, self._bot.find_element(self._transactions_table, element_name="transactions_table"))
