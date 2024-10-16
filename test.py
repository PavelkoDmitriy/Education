def introspection_info(obj):
    result = {}
    result['type'] = type(obj).__name__

    # Get attributes
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('__')]
    result['attributes'] = attributes

    # Get methods
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]
    result['methods'] = methods

    # Get module
    result['module'] = obj.__class__.__module__

    # Additional properties based on object type
    if result['type'] == 'int':
        result['properties'] = ['bit_length', 'conjugate', 'denominator', 'numerator']
    elif result['type'] == 'str':
        result['properties'] = ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']
    # Add more conditions for other types as needed

    return result

# Example usage:
number_info = introspection_info(introspection_info)
print(number_info)


def introspection_info(obj):
    # Получаем тип объекта
    obj_type = type(obj).__name__

    # Получаем атрибуты объекта
    obj_attributes = dir(obj)

    # Получаем методы объекта
    obj_methods = [method for method in dir(obj) if callable(getattr(obj, method))]

    # Получаем модуль, к которому объект принадлежит
    obj_module = obj.__class__.__module__

    # Возвращаем информацию об объекте
    return {
        'type': obj_type,
        'attributes': obj_attributes,
        'methods': obj_methods,
        'module': obj_module
    }

number_info = introspection_info(introspection_info)
print(number_info)

