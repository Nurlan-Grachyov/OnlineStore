def test_products_init(product):
    assert product.name == "onion"
    assert product.description == "green onion from grandmom`s garden"
    assert product.__price == 35
    assert product.quantity == 10