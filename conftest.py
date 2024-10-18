import pytest

from main import Product, Category


@pytest.fixture
def products():
    return Product("onion", "green onion from grandmom`s garden", 35, 10)


@pytest.fixture
def category():
    return Category("shoes", "winter shoes", ["boots with fur", "winter jacket"])
