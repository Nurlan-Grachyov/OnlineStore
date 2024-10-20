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
        self.products = products

    def __str__(self):
        return f"Category(name={self.name}," f"description={self.description}," f"products={self.products})"

if __name__ == "__main__":
    category_1 = Category("products", "products for salad", ["tomato", "cucumber", "onion"])
    category_2 = Category("sweets", "sweet", ["chocolate", "candies"])
    print(category_1)
    print(category_2)
    print(Category.category_count)
    print(Category.product_count)