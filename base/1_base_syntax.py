"""
Basic Syntax
"""
import typing

------------------------------------------------------------------------------------------------------------------>
# Basic Data Types
"""
Типы данных в питоне делятся на два типа изменяемые list, dict, set а также пользовательские классы
int, byte, string, tuple, bool
"""
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
# key=data_types
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



# Types Casting, Conversion 
"""
Приведение типов = это процес преобразования одного типа данных в другой. 
Есть два вида Неявный - когда интерпретатор может преобразовать Типы данных неявно, и Явный, когда мы должны указать тип в который мы хотим привести данные. 

There are two type of types of Type Casting: 
- Explicit - Явное приведение
- Python Implicit Type Conversion и неявное приедение типов.

# Implicit Type Casting happens under the hood 
# There can be two types of Type Casting: Explicit and Implicit
# Implicit
"""
a = 1
print(type(a))
# integer

b = 1 + 2.0
print(type(b))
# float 

c = 1j
print(type(c))
# complex

# Explicit type - требует явного вмешательства пользователя
# Mainly type casting can be done with these data type functions:
# key=casting
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
# data types, Types Casting, Conversion 
------------------------------------------------------------------------------------------------------------------>


------------------------------------------------------------------------------------------------------------------>
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

copy and deepcopy
# Copy - creates a new object that refers to old object - all changes are reflected on origin object
# deepcopy - A deep copy creates a new object and recursively copies all objects found in the original,
# meaning that the new object is entirely independent of the original.

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
_ = 1 // 2 Division (floor): divides the first operand by the second returns INTEGER
5//2 = 2

_ = 1 % 2 Modulus: returns the remainder when the first operand is divided by the second
Деление по модулю возвращает остаток от деления,
10 % 3 = 1 
10 % 2 = 0
10 % 5 = 0

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

is          True if the operands are identical 
is not      True if the operands are not identical 

a = 10
b = 20
c = a
True
True

print(a is not b)
print(a is c)

#Difference between ‘and’ and ‘&’ in Python 
and - is logical
& - binary operator, используется для побитовых операций с целыми числами. Он сравнивает каждый бит двух чисел и возвращает новое число, где каждый бит равен 1, только если соответствующие биты обоих чисел равны 1.
#Difference between ‘and’ and ‘&’ in Python  


# not Operator in Python | Boolean Logic 
# Ключевое слово not в Python - это логический оператор, который обычно используется для определения отрицания или противоположного булевого значения операнда.
# In the above example, we saw that treating all the data types as operands with not keyword., ‘not’ treats true to all the data types who had value and false to those who were empty value.
a = False
print(not a)
# not Operator in Python | Boolean Logic  


# Ternary Operator in Python
Syntax :  [on_true] if [expression] else [on_false] 
Syntax: true_value if condition else false_value
a = 10
b = 20

min = "a is minimum" if a < b else "b is minimum"  # 

a = not True
print("Test True") if a is True else  print("test2")
# Ternary Operator in Python 


# Walrus Operator in Python 3.8 
#Этот оператор позволяет присвоить значение переменной внутри выражения, что может быть полезно для сокращения и оптимизации кода.
while (line := input()) != "exit":
    print(f"Вы ввели: {line}")


doubles = [double for i in range(10) if (double := i * 2) > 10]
print(doubles)
# Walrus Operator in Python 3.8 


# Increment += and Decrement -= Assignment Operators in Python -> 
 Python does not have ++ or -- operators
x = 5
x += 1  # Increment by 1
print(x)  # Output will be 6  TODO CHECK id(x)
# Increment += and Decrement -= Assignment Operators in Python 

# Basic Operators 
------------------------------------------------------------------------------------------------------------------




"""
# Conditions, Control Flow. --------------------------------------------------------------------------------------------------------------------------------------------------> 
# Conditional statements in Python play a key role in determining the direction of program execution.

# Python If Statement
# Python If Else Statement
# Python Nested If Statement
# Python Elif
# Ternary Statement | Short Hand If Else Statement
"""
if i := d.get(''):
    pass
elif not (q := d.get(1)):
    pass
else:
    ...

# Using the function on odd elements of the list comperhansive 
newList = [i**2 for i in List if i & 1]


# Python program to illustrate short hand if
i = 10
if i < 15: print("i is less than 15")

# ternary
Syntax :  [on_true] if [expression] else [on_false] 
Syntax: true_value if condition else false_value

"""
# LOOPS
# what are the different types of control statements in Python?
# In Python, control statements are used to alter the flow of execution based on specific conditions or looping requirements. The main types of control statements are:
# -- Conditional statements: if, else, elif
# -- Looping statements: for, while
# -- Control flow statements: break, continue, pass, return
# Difference between for loop and while loop in Python
# while зацыкленно выполняет кусок кода, фор нужен для интеации
"""

# while (key=WHILE)
while expression:
    statement(s)

# the loop runs while the expression is True
count = 0
while (count < 3):
    count = count + 1
    print("Hello Geek")

# Syntax of While Loop with else statement:
while condition:
     # execute these statements
else:
     # execute these statements
counter = 5 
while counter >= 0:
    print(counter)
    counter -= 1
else:
    print('end of loop')
# else returns when loop is finished


# While loop
while a:
    a.pop()

while a:
    break
else:
    pass

"""
# For is used for sequential traversal. Использует для обхода последовательности.
# Последовательность - это упорядоченные коллеции элементов, под упорядоченными имеется ввиду остортированные.
# - Последовательности: string, list, set, tuple, dict 
# В Python последовательности, которые реализуют интерфейс __iter__ и __next__, называются итерируемыми объектами. 
# Это позволяет использовать их в циклах и других конструкциях, которые требуют итерации.

# FOR loop 
# The underscore _ is often used as a variable name when you want to indicate that the variable is a placeholder and its value is not needed. 
# This is a common Python convention when the loop variable is not used.
"""
for _ in types:
    pass


for type_name in types:
    print(type_name)  # This will print each type in the types list

#The code uses a Python for loop that iterates over the values from 0 to 3 (not including 4), as specified by the range(0, n) construct. 
#It will print the values of ‘i' in each iteration of the loop.
n = 4
for i in range(0, n):
    print(i)


for _ in types:
    break
else:
    pass

list = ["geeks", "for", "geeks"]
for index in range(len(list)):
    print(list[index])
else:
    print("Inside Else Block")    
    

# Nested Loops in Python 
rows = 5
cols = 10

for y in range(rows): # берём первый элемент из rows - 0
    for x in range(cols): # и проходим по всем элементам второго объекта (0, 0) (1, 0)
        print(f"({x}, {y})", end=' ') # end=' ': Это позволяет выводить все координаты в одной строке с пробелами между ними. После завершения внутреннего цикла, print() без аргументов переходит на новую строку.
    print() #  print()  # Переход на новую строку после каждой строки
    
(0, 0) (1, 0) (2, 0) (3, 0) (4, 0) (5, 0) (6, 0) (7, 0) (8, 0) (9, 0) 
(0, 1) (1, 1) (2, 1) (3, 1) (4, 1) (5, 1) (6, 1) (7, 1) (8, 1) (9, 1) 
(0, 2) (1, 2) (2, 2) (3, 2) (4, 2) (5, 2) (6, 2) (7, 2) (8, 2) (9, 2)
(0, 3) (1, 3) (2, 3) (3, 3) (4, 3) (5, 3) (6, 3) (7, 3) (8, 3) (9, 3)
(0, 4) (1, 4) (2, 4) (3, 4) (4, 4) (5, 4) (6, 4) (7, 4) (8, 4) (9, 4)


# Loop Control Statements
# continue, break, return, pass 

# The continue statement in Python returns the control to the beginning of the loop.
for y in range(rows):
    for x in range(cols):
        if x == 0: 
            continue
        print(f"({x}, {y})", end=' ')
    print()

# Break Statement
for i in "Elliot": 
    if i =='i':
        break
    print(i)
else:
    print("we got i letter")


# manualy
fruits = ["apple", "orange", "kiwi"]
iter_obj = iter(fruits)
while True:
    try:
        fruit = next(iter_obj)
        print(fruit)
    except StopIteration:
        break

# The break statement in Python brings control out of the loop.



# match qwe:
#     case "1":
#         pass
#     case _:
#         pass


# Conditions, Control Flow. --------------------------------------------------------------------------------------------------------------------------------------------------> 



# List Comprehensions
a = [i for i in types]
b = (i for i in types)
c = {i for i in types if isinstance(i, typing.Hashable)}
d = {str(i): i for i in types}



# Assert
assert h, 'test'

"""
# Methods --------------------------------------------------------------------------------------------------------------------------------------------------> 
# 
Regular methods
Static methods
Class methods
Using methods of parent class
args and kwargs

# Методы определяются ключевым словом Def - метод это поименованая область кода, которая нужна для многократного использования. обязательно указываем self первым параметром функции, если конечно это не статик. 

# Static methods - определяются декоратором @staticmethod и не принимают self, cls. они могут быть вызваны по имени класса или по объекту класса. Статические методы не получают доступ и не изменяют ни класс, ни объект. 

# Class Method - методы определяются декоратором @classmethod как и их первый параметр cls, Метод класса — это метод, привязанный к классу , а не к объекту класса.
# У них есть доступ к состоянию класса, поскольку он принимает параметр класса, указывающий на класс, а не на экземпляр объекта.
# Он может изменить состояние класса, которое будет применяться ко всем экземплярам класса. Например, он может изменить переменную класса, которая будет применяться ко всем экземплярам.
#
# Когда использовать класс или статический метод?
# Обычно мы используем метод класса для создания фабричных методов. Фабричные методы возвращают объекты класса (аналогично конструктору) для различных вариантов использования.
# Обычно мы используем статические методы для создания служебных функций.
#
# 1) Позиционные аргументы передаются в функцию по порядку. То есть порядок передачи аргументов важен
# 2) Keyword args именнованые, greet(age=25, name="Alice")
# 3) default def greet(name, age=30):
# 4) *args собирает все позиционные аргументы в кортеж.
# 5) **kwargs собирает все именованные аргументы в словарь.
# 6) yield yield отправляет результирующий объект вызывающему коду, но запоминает место, где он остановился. 
# 7) return, 
# 8) global - global объявляет переменные уровня модуля, предназначенные для присваивания. По умолчанию все имена, присваиваемые в функции, являются локальными для функции и существуют только во время ее выполнения. Чтобы
     присвоить значение имени из включающего модуля, необходимо указать его в
     операторе global внутри функции 
# 9) nonlocal - nonlocal объявляет переменные объемлющей функции, предназначенные
     для присваивания. Подобным образом оператор nonlocal, появившийся в
     Python З.Х, позволяет функции присваивать имя, которое существует в области
     видимости синтаксически объемлющего оператора def. В итоге объемлющие
     функции могут служить местом сохранения состояния, т.е. информации, запоминаемой между вызовами функции, без потребности в применении разделяемых глобальных имен
# 10) lambda создает объект, но возвращает его в качестве результата. Функции можно также создавать с помощью выражения lambda — средства, которое позволяет
     встраивать определения функций в места, где оператор def синтаксически не допускается
# 11) map, filter, reduce, max, min
"""
def func(text: str, space: str, action: typing.Callable) -> None:
    if not text:
        return

    print(space + action(text))
    func(text[1:], space + ' ', action)
    print(space + action(text))

# @staticmethod
"""
Может быть вызван по имени класса, без создания объекта, и также поддерживает вызов через объкт класса
"""
@staticmethod
def hello(name):
    return f"Hello, {name}"


# @classmethod
""" 
# @classmethod - используется для работы с атрибутами класса,  Class Method - методы определяются декоратором @classmethod как и их первый параметр cls, Метод класса — это метод, привязанный к классу , а не к объекту класса.
# У них есть доступ к состоянию класса, поскольку он принимает параметр класса, указывающий на класс, а не на экземпляр объекта.
# Он может изменить состояние класса, которое будет применяться ко всем экземплярам класса. Например, он может изменить переменную класса, которая будет применяться ко всем экземплярам.
"""
сlass Car:
    car_count = 0
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        Car.car_count += 1
    
    # Метод класса
    @classmethod
    def total_cars(cls):
        return f'Total cars: {cls.car_count}'  
    
# Создаем два экземпляра
car1 = Car('Toyota', 'Camry', 2020)
car2 = Car('Honda', 'Accord', 2021)

print(Car.total_cars())  # Вывод: Total cars: 2


# Вызовы родтельских методов
class Animal:
    def sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def sound(self):
        # Используем super() для вызова метода родителя
        parent_sound = super().sound()
        return f'{parent_sound}, but also: Woof woof!'

# Экземпляр класса Dog использует метод sound, который вызывает родительский метод
dog = Dog()
print(dog.sound())  # Вывод: Some generic animal sound, but also: Woof woof!

# *args **kwargs
"""
# Python – Star or Asterisk operator ( * ) 
# *args собирает все позиционные аргументы в кортеж.
# **kwargs собирает все именованные аргументы в словарь.
"""
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




# Exceptions
"""
Исключения генерируются автоматически при ощибках и могут быть перехвачены, обрабатываюся 4 операторами. по факту их 5
- Если не перехватывать исключения, то рантайм падает. М
- Можно самостоятельно определять новые исключения

What are the exceptions
How to catch an exception
How to throw an exception

# 1) try/except - перехватывает и произваодит восстановления после исключения
# 2) try/finally - происходят в любом случае, было ли исключение или нет. Выполняется всегда. 
# 3) raise - генерирует исключение вручную в коде. Код тоже может генерировать исключение.
# 4) assert - генерирует исключение условно в коде 
# 5) with/as - реализует диспетчеры контекстов


try/excep:
- Перехватывает и обрабатывает исключения
- Не выполняет код, если не возникло исключение
- Обычно используется для контроля потока программы
try/finally:
- Гарантирует выполнение кода после try
- Выполняется в любом случае, даже если не было исключений
- Чаще используется для освобождения ресурсов, Блок finally часто применяется для освобождения ресурсов, закрытия файлов, завершения соединений с базами данных и других задач, которые должны быть выполнены в любом случае.

"""
try:
    1 / 0
except ZeroDivisionError as exc:
    pass
else:
    pass
finally:
    ...
    
try:
    raise IndexError 
except IndexError:
    print("got IndexError")
    
# Exceptions



# Class 
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
# Class