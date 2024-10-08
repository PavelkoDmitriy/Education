class House:
    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object().__new__(cls)
    """
    def __new__(cls, name, number_of_floors):
        cls.houses_history.append(name)
        return super().__new__(cls)
    """
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(new_floor):
                print(i + 1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    @staticmethod
    def isinstance_(arg):
        match arg:
            case House():
                return arg.number_of_floors
            case int():
                return arg

    def __eq__(self, other):
        return self.number_of_floors == House.isinstance_(other)

    def __lt__(self, other):
        return self.number_of_floors < House.isinstance_(other)

    def __le__(self, other):
        return self.number_of_floors <= House.isinstance_(other)

    def __gt__(self, other):
        return self.number_of_floors > House.isinstance_(other)

    def __ge__(self, other):
        return self.number_of_floors >= House.isinstance_(other)

    def __ne__(self, other):
        return self.number_of_floors != House.isinstance_(other)

    def __add__(self, value):
        self.number_of_floors += House.isinstance_(value)
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __del__(self):
        return print(f"{self.name} снесён, но он останется в истории")


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
