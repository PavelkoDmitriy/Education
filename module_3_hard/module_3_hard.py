def calculate_structure_sum(*arg):
    res = 0
    for i in arg:
        match i:
            case int() | float():
                res += i
            case str():
                res += len(i)
            case dict():
                res += calculate_structure_sum(*i.values())
                res += calculate_structure_sum(*i.keys())
            case list() | tuple() | set():
                res += calculate_structure_sum(*i)
    return res


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
