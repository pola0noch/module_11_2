# Домашнее задание по теме "Интроспекция"
import inspect
import pprint

def introspection_info(obj):
    info = {}

    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    methods = [meth for meth in dir(obj) if callable(getattr(obj, meth)) and not meth.startswith("__")]

    info['type'] = type(obj).__name__
    info['attributes'] = attributes
    info['methods'] = methods
    info['module'] = getattr(obj, '__module__', '__main__')
    info['is_class'] = inspect.isclass(obj)
    info['is_function'] = inspect.isfunction(obj)
    info['is_instance'] = isinstance(obj, object) and not inspect.isclass(obj)

    if info['is_class']:

        info['base_classes'] = [base.__name__ for base in obj.__bases__]

        class_attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
        class_methods = [method for method in dir(obj) if isinstance(getattr(obj, method), classmethod)]

        info['class_attributes'] = class_attributes
        info['class_methods'] = class_methods

    return info


if __name__ == "__main__":
    class Example:
        class_attr = "I am a class attribute."

        def __init__(self):
            self.attr1 = "value1"
            self.attr2 = "value2"

        def method1(self):
            pass


    example_obj = Example()
    example_info = introspection_info(example_obj)
    pprint.pprint(f'Информация об объекте класса: \n{example_info}')

    class_info = introspection_info(Example)
    pprint.pprint(f'Информация о классе: \n{class_info}')

    number_info = introspection_info(42)
    pprint.pprint(f'Информация о числе: \n{number_info}')

    func_info = introspection_info(sum)
    pprint.pprint(f'Информация о функции: \n{func_info} ')







