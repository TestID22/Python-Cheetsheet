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
    1j, complex,
    ' ', " ", """ """, f'', r'', str,
    b'', bytes, bytearray, memoryview,
    [], list,
    (), tuple,
    {1, }, set,
    {}, dict
]

Числовые значение: int, float, complex (decimal)
x = 1    # int
y = 2.8  # float
z = 1j   # complex
Строка: str 
Последовательности: list, tuple (кортеж), range 
mapping type: dict - ключ: значение
наборы или множество , set: (),

1) Text Type:	str
2) Numeric Types:	int, float, complex
3) Sequence Types:	list, tuple, range
4) Mapping Type:	dict
5) Set Types:	set, frozenset
6) Boolean Type:	True, False, bool
7) Binary Types:	bytes, bytearray, memoryview
8) None Type:	NoneType
9) ... -  элипсис, спец тип данныз который используется в многомерных массивах в Numpy

range() - возвращает последовательность чисел, которые можно использовать в Loops. 0, 1, 2, 3, 4 
range(start, stop, step)

# Basic Data Types


------------------------------------------------------------------------------------------------------------------
# Types Casting, Conversion 
"""
Приведение типов = это процес преобразования одного типа данных в другой. 
Есть два вида Неявный - когда интерпретатор может преобразовать Типы данных неявно, и Явный, когда мы должны указать тип в который мы хотим привести данные. 
"""
There are two type of types of Type Casting: 
- Explicit - Явное приведение
- Python Implicit Type Conversion и неявное приедение типов.

Implicit Type Casting happens under the hood 
# There can be two types of Type Casting: Explicit and Implicit
# Implicit
a = 1
print(type(a))
# integer

b = 1 + 2.0
print(type(b))
# float 

c = 1j
print(type(c))
# complex

Explicit type - требует явного вмешательства пользователя
Mainly type casting can be done with these data type functions:

int(): Python Int() function take float or string as an argument and returns int type object.
float(): Python float() function take int or string as an argument and return float type object.
str(): Python str() function takes float or int as an argument and returns string type object.

a = 1
b = float(1)
print(type(b))

b = str(a)
print(type(b))

b = int(a)
print(type(b))\

# float to int
a = 1.9
b = int(a)
print(b)
print(type(b))
# Пайтон округлит до целого: вывод будет 1, а не 2
# Тип буде int

What is the Difference Between Type Casting and Type Conversion?
Type casting and type conversion are terms that can be used interchangeably to refer to changing data from one type to another. 
However, some distinctions are often made:

Type Conversion: This can be seen as a broader term that encompasses both implicit and explicit type changes.

Type Casting: Often refers specifically to explicit conversion, where the conversion is clearly specified in the code.
# Types Casting, Conversion 
------------------------------------------------------------------------------------------------------------------


------------------------------------------------------------------------------------------------------------------
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
# Basic Operators 
------------------------------------------------------------------------------------------------------------------


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
'''
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
'''
lambda arguments : expression

a = lambda x: x + 10
hello_user = lambda name: "Hello " + name

command = lambda name_1, name_2, name_3, name_4: name_1 + name_2 + name_3 + name_4 + " are idiots"
func('*' * 11, '', lambda text: ' '.join(i for i in text))
Why should we use lambdas?

1. Краткость, 2. анонимность (не нужно объявлять громоздкий def), 3. Использование внутри функций:

 Лучшее применения когда мы используем лямбду в другой функции.
# lambda func


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
