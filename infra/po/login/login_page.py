# pages/login_page.py
from selenium.webdriver.common.by import By

from infra.po.abstract_page import AbsPage
from infra.po.transactions.transactions_page import TransactionsPage


class LoginPage(AbsPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._username_input = By.ID, 'username'
        self._password_input = By.ID, 'password'
        self._login_btn = By.ID, 'log-in'
        self._login_header = By.CSS_SELECTOR, 'h4.auth-header'
        self.wait_until_login_header_is_visible()

    def do_login_and_go_to_transaction_page(self, username: str, password: str) -> TransactionsPage:
        self. \
            enter_username(username). \
            enter_password(password). \
            click_login_button()
        return TransactionsPage(driver=self.driver)

    def enter_username(self, username):
        self._bot.send_keys(self._username_input, username, element_name="username_input")
        return self

    def enter_password(self, password):
        self._bot.send_keys(self._password_input, password, element_name="password_input")
        return self

    def click_login_button(self):
        self._bot.click(self._login_btn, element_name="login_btn")

    def wait_until_login_header_is_visible(self):
        self._bot.wait_until_element_is_visible(self._login_header, element_name="login_header")
        return self
