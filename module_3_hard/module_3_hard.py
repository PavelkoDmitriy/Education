def calculate_structure_sum(*args):
    total = 0
    for arg in args:
        match arg:
            case int() | float():
                total += arg
            case str():
                total += len(arg)
            case dict():
                total += calculate_structure_sum(*arg.keys(), *arg.values())
            case (list() | tuple() | set()) as collection:
                total += calculate_structure_sum(*collection)
    return total


# Пример использования
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)  # Выводит: 99
