class Product:
    def __init__(self, name=str, weight=float, category=str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self) -> str:
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = "products.txt"
    def get_products(self):
        file = open(__file_name, 'r')
        file_= file.read()
        file.close()
        print(*file_)

Shop.get_products
