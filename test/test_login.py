# tests/test_login_and_transaction.py
import pytest
from assertpy import assert_that

from config.defentions import username, password
from infra.helpers.steps import Given, When, Then
from infra.po.login.login_page import LoginPage


@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("https://demo.applitools.com/")


def test_login_and_count_transactions(driver):
    with Given("a user in login page"):
        login_page = LoginPage(driver)

    with When("the user make a successful login"):
        transactions_page = login_page. \
            do_login_and_go_to_transaction_page(username=username, password=password)
        transactions_table = transactions_page.get_transactions_table()

    with Then("transactions page is displayed with a table that have 2 successful transaction "):
        assert_that(transactions_table.get_number_of_successful_transactions() == 2).is_true()
