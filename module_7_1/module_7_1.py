class Product:
    def __init__(self, name=str, weight=float, category=str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self) -> str:
        return f"{self.name}, {self.weight}, {self.category}"
    
class Shop:
    __file_name = 'products.txt'
    
    def get_products(self):
        file = open(self.__file_name, 'r')
        file_ = file.read()
        file.close()
        return file_
        
    def add(self, *products):
        list_ = []
        l = self.get_products().split('\n')
        for i in products:
            if str(i) not in l:
                list_.append(str(i))
            else:
                print(f'Продукт {i} уже есть в магазине')
        file = open(self.__file_name, 'a')
        file.write('\n'.join(list_))
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())