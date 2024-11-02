from abc import ABC, abstractmethod

class MixinProduct:
    def __init__(self):
        print(str(self))

    def __str__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"

class BaseProduct(ABC):
    @abstractmethod
    def __add__(self, other):
        pass


class Product(MixinProduct, BaseProduct):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description} {self.price} {self.quantity}')"

    def __str__(self):
        if self.__price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        sum_product = self.price * self.quantity + other.price * other.quantity
        return sum_product

    @classmethod
    def new_product(cls, product):
        name = product["name"]
        description = product["description"]
        price = product["price"]
        quantity = product["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is __class__:
            summ = self.price + other.price
            return summ
        else:
            raise TypeError


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is __class__:
            summ = self.price + other.price
            return summ
        else:
            raise TypeError


class Car:
    def __init__(self, name, price, quantity, color):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.color = color


if __name__ == "__main__":
    product_1 = Product("tomato", "red tomato from Azerbaijan", 150, 10)
    product_2 = Product("cucumber", "cucumber from Azerbaijan", 100, 20)
    # print(product_1)
    product_3 = {
        "name": "Помидоры",
        "description": "Помидоры красные, вкусные, не дорого",
        "price": 180,
        "quantity": 10,
    }
    product_add = Product.new_product(product_3)
    print(product_add)
    # product_2.price = 20
    # print(product_2)
    # product_phone_1 = Smartphone("xiaomi", "xiaomi 8gb", 500, 20, "Good", "note 8 pro", "128 gb", "blue")
    # product_phone_2 = Smartphone("infinix", "infinix 128/8", 700, 30, "Good", "Note 30", "128 gb", "Green")
    # res = product_phone_1 + product_phone_2
    # print(res)
