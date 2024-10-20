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
# OPERATORS: These are the special symbols. Eg- + , * , /, etc.
# OPERAND: It is the value on which the operator is applied.
# 1) Difference between == and is: == cравнивает значения объекта, is сравнивает ссылки. !ВАЖНО! для при глубоком копировании неизменяемых объектов ссылки не будут изменятся 
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True, because the lists 'a' and 'b' have the same values
print(a is b)  # False, because 'a' and 'b' are different objects in memory
print(a is c)  # True, because 'a' and 'c' point to the same object in memory
name = ['alex', 'motalex']
# True

wildCard: для неизменяемых типов, значения которых равны питон для скорости работы будет ссылаться на один и тот же участок памяти. ID оъеста тоже одинаковы. 
a = 5 
b = 5
print(memoryview(bytes(a)))
print(memoryview(bytes(b)))
print(a is b)
# <memory at 0x0000020AA5CCDD80>
# <memory at 0x0000020AA5CCDD80> 
# True

# Precedence of Arithmetic Operators in Python
# The precedence of Arithmetic Operators in Python is as follows:
# P – Parentheses (скобки)
# E – Exponentiation (возведение в степерь) 
# M – Multiplication (Multiplication and division have the same precedence) Деление (/) и умножение (*) имеют одинаковый приоритет и выполняются слева направо.
# D – Division 
# A – Addition (Addition and subtraction have the same precedence)
# S – Subtraction


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

# Comparison of Python Operators
>, <, ==, !=, >=, <=
_ = 1 > 2 | 1 >= 2 | 1 < 2 | 1 <= 2

# Logical Operators
_ = 1 and 2 
_ = 1 or 2
_ = a not b 

# Bitwise Operators in Python
# These operations manipulate the binary representations of the numbers.
&, |, ~, >>, <<, ^

= assign value 
+=
-= 
*= 
/=
%= 
**=
 
# Identity Operators in Python
# In Python, is and is not are the identity operators both are used to check if two values are located on the same part of the memory. 
# Two variables that are equal do not imply that they are identical. 

copy and deepcopy
# Copy - creates a new object that refers to old object - all changes are reflect on origin object
# deepcopy - A deep copy creates a new object and recursively copies all objects found in the original,
# meaning that the new object is entirely independent of the original.


is          True if the operands are identical 
is not      True if the operands are not identical 

a = 10
b = 20
c = a
True
True

print(a is not b)
print(a is c)




# Python – Star or Asterisk operator ( * )  --------------------------------------------------------------------------------------------------------------------------------------------------> 
#Одинарная звёздочка (*)
#В аргументах функций: Используется для передачи переменного количества аргументов. Аргументы будут собраны в кортеж.
def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3)  # Выводит: 1, 2, 3
#При распаковке: Позволяет распаковывать итерируемые объекты в функции и списки.
numbers = [1, 2, 3]
print(*numbers) 
# using asterisk
def addition(*args):
  return sum(args)

print(addition(5, 10, 20, 6))


# Двойная звёздочка (**)
В аргументах функций: Используется для передачи переменного количества именованных аргументов. Аргументы будут собраны в словарь.
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function(a=1, b=2)  # Выводит: a: 1, b: 2

# Присвоение, распаковка, slice 
e, *f, g = types
h = [*f]
_ = [1, 2, 3][:]
_ = {**{}}
=======
# Python – Star or Asterisk operator ( * )  --------------------------------------------------------------------------------------------------------------------------------------------------> 


#Difference between ‘and’ and ‘&’ in Python --------------------------------------------------------------------------------------------------------------------------------------------------> 
and - is logical
& - binary operator, используется для побитовых операций с целыми числами. Он сравнивает каждый бит двух чисел и возвращает новое число, где каждый бит равен 1, только если соответствующие биты обоих чисел равны 1.
#Difference between ‘and’ and ‘&’ in Python  --------------------------------------------------------------------------------------------------------------------------------------------------> 


# not Operator in Python | Boolean Logic --------------------------------------------------------------------------------------------------------------------------------------------------> 
# Ключевое слово not в Python - это логический оператор, который обычно используется для определения отрицания или противоположного булевого значения операнда.
# In the above example, we saw that treating all the data types as operands with not keyword., ‘not’ treats true to all the data types who had value and false to those who were empty value.
a = False
print(not a)
# not Operator in Python | Boolean Logic  --------------------------------------------------------------------------------------------------------------------------------------------------> 


# Ternary Operator in Python --------------------------------------------------------------------------------------------------------------------------------------------------> 
Syntax :  [on_true] if [expression] else [on_false] 
Syntax: true_value if condition else false_value
a = 10
b = 20

min = "a is minimum" if a < b else "b is minimum"  # 

a = not True
print("Test True") if a is True else  print("test2")
# Ternary Operator in Python --------------------------------------------------------------------------------------------------------------------------------------------------> 


# Walrus Operator in Python 3.8 -------------------------------------------------------------------------------------------------------------------------------------------------->
#Этот оператор позволяет присвоить значение переменной внутри выражения, что может быть полезно для сокращения и оптимизации кода.
while (line := input()) != "exit":
    print(f"Вы ввели: {line}")


doubles = [double for i in range(10) if (double := i * 2) > 10]
print(doubles)
# Walrus Operator in Python 3.8 -------------------------------------------------------------------------------------------------------------------------------------------------->


# Increment += and Decrement -= Assignment Operators in Python -> --------------------------------------------------------------------------------------------------------------------------------------------------> 
 Python does not have ++ or -- operators
x = 5
x += 1  # Increment by 1
print(x)  # Output will be 6  TODO CHECK id(x)
# Increment += and Decrement -= Assignment Operators in Python --------------------------------------------------------------------------------------------------------------------------------------------------> 

# Basic Operators 
------------------------------------------------------------------------------------------------------------------


# Conditions, Control Flow. --------------------------------------------------------------------------------------------------------------------------------------------------> 
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


# FOR loop 
for _ in types:
    pass

for _ in types:
    break
else:
    pass



# While loop
while a:
    a.pop()

while a:
    break
else:
    pass

# Conditions --------------------------------------------------------------------------------------------------------------------------------------------------> 



# List Comprehensions
a = [i for i in types]
b = (i for i in types)
c = {i for i in types if isinstance(i, typing.Hashable)}
d = {str(i): i for i in types}



# Assert
assert h, 'test'


# Functions --------------------------------------------------------------------------------------------------------------------------------------------------> 
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
# lambda func --------------------------------------------------------------------------------------------------------------------------------------------------> 


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
