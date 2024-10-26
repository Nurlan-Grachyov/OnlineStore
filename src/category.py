from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        Category.category_count += 1
        Category.product_count += len(products)
        self.name = name
        self.description = description
        self.__products = products

    @property
    def return_product(self):
        return [f"Название продукта : {product.name}, цена : {product.check_price} рублей, Остаток: {product.quantity} штук."  for product in self.__products]

    def add_product(self, product):
        self.__products.append(product)

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, new_products):
        self.__products = new_products

    def __str__(self):
        products_str = ", ".join(str(product) for product in self.__products)
        return f"Category(name={self.name}," f"description={self.description}," f"products={[{products_str}]})"

if __name__ == "__main__":
    product_1 = Product("tomato", "red tomato from Azerbaijan", 150, 10)
    product_2 = Product("cucumber", "cucumber from Azerbaijan", 100, 20)
    category_1 = Category("products", "products for salad", [product_1, product_2])
    product_3 = Product("lettuce", "fresh lettuce", 50, 15)
    category_1.add_product(product_3)
    # print(category_1.return_product)


