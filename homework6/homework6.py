my_dict = {"Anna": 1992, "Julia": 1989, "Nikolay": 1999, "Svetlana": 1996}
print(my_dict)
# print(my_dict["Svetlana"])
print(my_dict.get("Svetlana"))
print(my_dict.get("Dmitriy", "Имя отсутствует"))
my_dict.update({"Anton": 2000, "Stepan": 1998})
print(my_dict.pop("Anna"))
print(my_dict)
my_set = {"test", 5, 5, 5, 4, 8, 9, "test", 36.6, 'x', 4, (5, 7, 9, "xyz"), (5, 7, 9, "xyz")}
print(my_set)
my_set.add("Pi")
my_set.add(3.14)
my_set.discard("test")
print(my_set)
