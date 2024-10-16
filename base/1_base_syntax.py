"""
Basic Syntax
"""
import typing


# Basic Data Types
types = [
    ...,
    None,
    True, False, bool,
    1, int,
    1.1, float,
    ' ', " ", """ """, f'', r'', str,
    b'', bytes,
    [], list,
    (), tuple,
    {1, }, set,
    {}, dict
]


# Basic Operators 
_ = 1 + 2 Addition: adds two operands
_ = 1 - 2 Subtraction: subtracts two operands
_ = 1 * 2 Multiplication: multiplies two operands
_ = 1 ** 2 Power: Returns first raised to power second

There are two types of division operators: 
-Float division
-Floor division
_ = 1 / 2 Division (float): divides the first operand by the second
_ = 1 // 2 Division (floor): divides the first operand by the second

_ = 1 % 2 Modulus: returns the remainder when the first operand is divided by the second
_ = 1 and 2 
_ = 1 or 2
_ = 1 > 2 | 1 >= 2 | 1 < 2 | 1 <= 2


# FOR loop 
for _ in types:
    pass

for _ in types:
    break
else:
    pass


# List Comprehensions
a = [i for i in types]
b = (i for i in types)
c = {i for i in types if isinstance(i, typing.Hashable)}
d = {str(i): i for i in types}


# Присвоение, распаковка, slice 
e, *f, g = types
h = [*f]
_ = [1, 2, 3][:]
_ = {**{}}


# Assert
assert h, 'test'


# While loop
while a:
    a.pop()

while a:
    break
else:
    pass


# Functions
def func(text: str, space: str, action: typing.Callable) -> None:
    if not text:
        return

    print(space + action(text))
    func(text[1:], space + ' ', action)
    print(space + action(text))


# lambda func
func('*' * 11, '', lambda text: ' '.join(i for i in text))


# Decorators
def decorator(multiplier: int):

    def dec(func: typing.Callable):
        # Variable scopes
        global a, b, c, d
        nonlocal multiplier

        if multiplier % 2 == 0:
            multiplier += 1

        def wrap(*args, **kwargs):
            for _ in range(multiplier):

                # Generators
                yield func(*args, **kwargs)

        return wrap

    return dec


@decorator(10)
def f(num: int) -> int:
    return num


qwe = [*f(1)]


# Conditions
if i := d.get(''):
    pass
elif not (q := d.get(1)):
    pass
else:
    ...


# match qwe:
#     case "1":
#         pass
#     case _:
#         pass


# Исключения и их обработка
try:
    1 / 0
except ZeroDivisionError as exc:
    pass
else:
    pass
finally:
    ...


# Классы
class A:

    class_attrs = None

    def __init__(self, *args, **kwargs):
        self.args, self.kwargs = args, kwargs
        self.__test_arg = None

    def main(self) -> None:
        ...

    @property
    def test_arg(self) -> typing.Any:
        return self.__test_arg

    @test_arg.setter
    def test_arg(self, value: typing.Any):
        self.__test_arg = value


class B(A):

    def main(self) -> None:
        super().main()
        print(self.test_arg)

    @classmethod
    def create(cls, *args, **kwargs) -> 'B':
        return cls(*args, **kwargs)

    @staticmethod
    def get_test() -> str:
        return 'test'
