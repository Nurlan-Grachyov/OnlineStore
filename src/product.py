class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return (
            f"Product(name={self.name}, "
            f"description={self.description}, "
            f"price={self.price}, "
            f"quantity={self.quantity})"
        )



if __name__ == "__main__":
    product_1 = Product("tomato", "red tomato from Azerbaijan", 150, 10)
    product_2 = Product("cucumber", "cucumber from Azerbaijan", 100, 20)
    print(product_1)
    print(f"{product_2}\n")