from src.category import Category
from src.product import Product


def test_category_init(category_1, product):
    product1 = Product("boots with fur", 100, 10, 15)
    product2 = Product("winter jacket", 150, 5, 15)
    category = Category("shoes", "winter shoes", [product1, product2])

    assert category.name == "shoes"
    assert category.description == "winter shoes"
    assert category.category_count == 2
    assert category.product_count == 4

    expected_product_1 = (
        f"Название продукта : {product1.name}, цена : {product1.price} рублей, Остаток: {product1.quantity} штук."
    )
    expected_product_2 = (
        f"Название продукта : {product2.name}, цена : {product2.price} рублей, Остаток: {product2.quantity} штук."
    )

    assert category.products[0] == expected_product_1
    assert category.products[1] == expected_product_2

    product3 = Product("summer dress", 100, 345, 25)
    category.add_product(product3)

    assert len(category.products) == 3
    assert "summer dress" in category.products[-1]

    product1 = Product("Товар1", 100, 10, 45)
    product2 = Product("Товар2", 200, 5, 46)
    category = Category("Электроника", "Различные электронные устройства", [product1, product2])
    expected_str = "Category(name=Электроника, description=Различные электронные устройства, products=[{'Product(name=Товар1, description=100, price=10, quantity=45), Product(name=Товар2, description=200, price=5, quantity=46)'}])"
    assert str(category) == expected_str
