immutable_var = 1.25, "urban", 6, [63, 15, 0], 'y', (5, "test", 3.14, 'x')
print(immutable_var)
immutable_var[3][0] = 5
print(immutable_var)
immutable_var[3].remove(15)
immutable_var[3].append(63)
print(immutable_var)

# immutable_var[0] = 7 -> TypeError: 'tuple' object does not support item assignment. При попытке изменить первый
# элемент кортежа интерпретатор выдает ошибку, поскольку кортеж хранит ссылки на объекты в памяти, а изменение
# объекта подразумевает создание нового объекта в памяти с новой ссылкой. В то же время, если в кортеже будет список,
# при изменении элементов списка ссылка на список не меняется и адрес в памяти не изменится.

mutable_list = [5, "urban, 'x", (1, 2, 3), 5.99]
mutable_list[0] = "five"
mutable_list.append(5)
mutable_list.extend([6, "test, 'x"])
mutable_list[1] = 555
print(mutable_list)
