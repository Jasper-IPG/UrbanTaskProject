# "Интроспекция"
import inspect


class Object:
    def __init__(self, obj):
        self.obj = obj

    def introspection_info(self):
        result = {}
        if type(self.obj) is int:
            result.update({'type': 'int'})
        else:
            result.update({'type': 'not int'})
        if hasattr(self, 'obj'):
            result.update({'attributes': [...]})
        if dir(self.obj):
            result.update({'methods': ['__abs__', '__add__', ...]})
        if inspect.getmodule(self):
            result.update({'module': '__main__'})
        return result


number_info = Object(42)
print(Object.introspection_info(number_info))
# print(number_info)
