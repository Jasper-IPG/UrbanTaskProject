# "Интроспекция"
import inspect


def introspection_info(obj):
    result = {'type': type(obj),
              'attributes': [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
              'methods': [method for method in dir(type(obj)) if callable(getattr(obj, method))],
              'module': obj.__class__.__module__}
    return result


number_info = introspection_info(42)
print(number_info)
