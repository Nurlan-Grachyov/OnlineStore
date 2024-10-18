def test_products_init(products):
    assert products.name == "onion"
    assert products.description == "green onion from grandmom`s garden"
    assert products.price == 35
    assert products.quantity == 10


def test_category_init(category):
    assert category.name == "shoes"
    assert category.description == "winter shoes"
    assert category.products == ["boots with fur", "winter jacket"]
