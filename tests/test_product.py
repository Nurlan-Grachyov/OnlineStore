from src.product import Product


def test_products_init(product):
    product_1 = Product("tomato", "red tomato from Azerbaijan", 150, 10)

    assert product_1.name == "tomato"
    assert product_1.description == "red tomato from Azerbaijan"
    assert product_1.price == 150
    assert product_1.quantity == 10


def test_new_product():
    product_data = {"name": "Banana", "description": "Fresh yellow banana", "price": 0.5, "quantity": 20}
    product_add = Product.new_product(product_data)
    assert product_add.name == "Banana"
    assert product_add.description == "Fresh yellow banana"
    assert product_add.price == 0.5
    assert product_add.quantity == 20


def test_price_setter():
    product = Product("Orange", "Fresh orange", 1.5, 15)
    product.price = 3.0
    assert product.price == 3.0

    product.price = -3.0
    assert product.price == 3.0


def test_str(capsys):
    product = Product("Orange", "Fresh orange", 1.5, 15)
    expected_data = (
        f"Product(name={product.name}, "
        f"description={product.description}, "
        f"price={product.price}, "
        f"quantity={product.quantity})"
    )
    assert str(product) == expected_data

    product1 = Product("apples", "Fresh apples", -7.5, 15)
    str(product1)

    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
