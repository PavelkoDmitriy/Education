def print_params(a=1, b='строка', c=True):
    return print(a, b, c)


values_list = ['@', 3.14, "arg"]
values_dict = {'a': "test", 'b': 44, 'c': False}
values_list_2 = ['y', None]

print_params()
print_params('X')
print_params(True, 4, '4')
print_params(3.14, False, None)
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(*values_dict)
print_params(**values_dict)
print_params(*values_list_2, 42)
