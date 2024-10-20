import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product():
    return Product("onion", "green onion from grandmom`s garden", 35, 10)


@pytest.fixture
def category():
    return Category("shoes", "winter shoes", ["boots with fur", "winter jacket"])
