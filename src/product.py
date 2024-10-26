class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def check_price(self):
        return self.__price

    @check_price.setter
    def check_price(self, price):
        if price <= 0:
            print(f"Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price

    @classmethod
    def new_product(cls, product):
        name =  product['name']
        description = product['description']
        price = product['price']
        quantity = product['quantity']
        return  cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = new_price

    def __str__(self):
        return (
            f"Product(name={self.name}, "
            f"description={self.description}, "
            f"price={self.__price}, "
            f"quantity={self.quantity})"
        )

if __name__ == "__main__":
    # product_1 = Product("tomato", "red tomato from Azerbaijan", 150, 10)
    # product_2 = Product("cucumber", "cucumber from Azerbaijan", 100, 20)
    # print(product_1)
    # print(f"{product_2}\n")
    product_1 = {"name" : "Помидоры", "description" : "Помидоры красные, вкусные, не дорого", "price" : 170, "quantity" : 10 }
    product_add = Product.new_product(product_1)
    print(product_add)
    product_add.check_price = -5
    product_add.check_price = 20
    print(product_add)