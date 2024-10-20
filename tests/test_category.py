def test_category_init(category):
    assert category.name == "shoes"
    assert category.description == "winter shoes"
    assert category.products == ["boots with fur", "winter jacket"]
    assert category.category_count == 1
    assert category.product_count == 2