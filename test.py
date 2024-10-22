def introspection_info(obj):
    res = {}
    res["type"] = type(obj).__name__
    res["attributes"] = dir(obj)
    res["methods"] = [method for method in dir(obj) if callable(getattr(obj, method))]
    res["module"] = obj.__class__.__module__
    return res


number_info = introspection_info(introspection_info)
print(number_info)
