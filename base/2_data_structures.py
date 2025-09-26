"""
Basic data structures and Strings
"""
# 1. How to create / modify / delete
# 2. Modifiable / immutable objects
# 3. Basic methods of basic structures

# 1) What Data structures consist of (из встроенных и кастомных данных)

# 2) What's the purpose of Data structures - хранить наборы объектов. 

# 3) Differences between different structures: List, Dictionary, Set, FrozenSet, Tuple, String, Bytearray

# String formatting
"""
STRINGS
1) Конкатенация соединение строк "" + ""
2) OTP = 123 msg = """ Hello %s, %d """ % (username, OTP)
3) Using .format method
4) F-String in Python
"""


# using % 
OTP = 123
name = "Alex"
message = """Hello %s, %d"""% (name, OTP)
print(message)

# using .format()
text = "text {0} + {1}".format('Alex', 2)
print(text)

# f string
test = f"{variable_name} or {func_name}"

# Strings are IMUTABLE date types
#How to check 
name = "Pavel"
print(f"Id of the first objectL {id(name)}")
name = "test"
print(f" it's another object: {id(name)}")

# Access by index. Accessing elements of String
a = "Hello, World!"
print(a[1])

# Since a string is an array, you can iterate over it.
for x in "banana":
  print(x)

# String length   
a = "Hello, World!"
print(len(a))

# Checking for a substring 
txt = "The best things in life are free!"
print("free" in txt)

# Check if not 
txt = "The best things in life are free!"
print("expensive" not in txt)
---------
# SLICING
# from the start to 5 el.
txt = "Hackers"
test = txt[:5]

# slice from the 2 el. to the end 
txt = "Hackers"
test = txt[2:]

# inside
txt = "Hackers"
test = txt[2:5]

# negative slicing 
b = "Hello, World!"
print(b[-5:-2])
---------
# SLICING

----------------
# Modify Strings
# upperCase
a = "Hello, World!"
print(a.upper())

# lower
a = "Hello, World!"
print(a.lower())

# remove white spaces 
# from the beginning or the end
a = " Hello, World! "
print(a.strip())
# returns "Hello, World!"

# replace el in a string
a = "Hello, World!"
print(a.replace("H", "J"))

# split  string
a = "Hello, World!"
print(a.split(",")) 
# returns ['Hello', ' World!']
# Modify Strings
----------------

--------------
# Concatantate 
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)
# Concatantate 
--------------

--------------------------------
# f'string or интерполяция строк
price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
# f'string or интерполяция строк
--------------------------------


# Escape caracters 
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 
#                                                      String
------------------------------------------------------------------------------------------------------------------
https://www.geeksforgeeks.org/python-data-structures/

1) list - осортированный массив ссылок на объекты,
    arr = ['I', 'love', 'you']
2) dict - словарь, основанный на хеш таблицах. is like hash tables with time complexity of O(1)
    dict = {'name': obj }
3) range - is immutabble sequence of numbers, 
   range(1, 5, 2) # start, stop, step
4) tuple - is imutabble collection. elements in the tuple cannot be added or removed once created.
    screen_resolution = (1920, 1200)
5) set - is unordered collection of data that is mutable and does not allow any duplocate element.
    test = set([1, 1, 2, 3])
6) frozenset- (cant add or remove obkects, hashable, ) are imutablle objects that only support mettda and operator that produce a resuilt without affecting sets pr sets.
    frozenset(["e", "f", "g"])
7) string - is immutable array of characters 
    name = 'I love a1qa" 
8) bytearray - givesd a muttable sequnce of integers 0 <=x < 256 
   a = bytearray((12, 8, 25, 2))
   """
   Collections Module
   from collections import defaultdict
   """
9) Counters
10) OrderedDict
11) DefaultDict
12) ChainMap - A ChainMap encapsulates many dictionaries into a single unit
13) NamedTuple
14) Deque
15) UserDict
16) UserList
17) UserString
18) Linked List
19) Linked List Traversal 
20) Stack
21) Queue
22) Priority Queue
23) Heap queue (or heapq)
24) Binary Tree
25) Tree Traversal
26) Graph
27) Adjacency List
28) Graph Traversal

""" How to Choose the Right Data Structure in Python?

Access Speed:
Lists provide O(1) time complexity for indexing.
Dictionaries provide O(1) time complexity for key lookup.
Insertion and Deletion:
Lists have O(n) time complexity for insertion and deletion in the worst case.
Sets and dictionaries have O(1) time complexity for insertion and deletion.
Order:
Lists and tuples maintain the order of elements.
Sets and dictionaries (in Python 3.7+) maintain insertion order, but typically sets are considered unordered collections.
Uniqueness:
Sets ensure all elements are unique.
Lists and tuples allow duplicate elements.
Mutability:
If you need to modify the data structure after creation, use mutable structures like lists or dictionaries.
For fixed collections of items, use immutable structures like tuples or frozensets
"""





# LIST 
"""
 Структуры Данных - Коллекции объектов
 Список упорядоченная, остортированная коллекция
 Содержат объекты любого вида
 Элементы доступны по индексу
 Изменяемый тип данных.
 представляют собой массив ссылок на объекты
 help(list) dir(list)
"""
a = []
a = list()
a = [1] * 10
a = [1, 2, 3] + [3, 4, 5]
a = [*a]
a.append(a) - add a single object even if this is list
a.pop() 
a.extend(a) - concatanate list 
a.sort()
a.copy() - create shallow copy 
a.reverse()
a.index()
a.count()
a.clear()
del a[i:j]
a[1] = value
list(map(ord, 'spam'))

# end of LIST

# TUPLE
"""
коллекция неизменяемых объектов
содрежит коллекцию разных объектов
ПРИМЕЧАНИЕ: чтоб создать кортеж с одним объектом нужно поставить запятую после объекта
"""
b = (1, 2, a)
b = (obj,)
b = tuple([1, 2])
b = b[:]
b, _ = b
# TUPLE

# SET 
"""
Это неупорядоченная коллекция данных, которая является изменяемой и не допускает дублирования элементов
Sets в основном используются для проверки членства и устранения дублирующихся записей
Структура данных, используемая в этом случае, — это хеширование, популярный метод для выполнения вставки, удаления и обхода в среднем за O(1)
"""
c = {1, 2}
d = set([1, 2])
c.add(3)
c.remove(3)
c.update({None, })
_ = c - d
_ = c | d
_ = c & d
_ = frozenset(c)
# SET
# FrozenSet

# FrozenSet

# Dicitonary
"""
похож на хеш таблицы, с временной сложностю O(1)
Неупорядоченная коллеция пар ключ - значение
Доступ осуществляется через ключи
изменяемый тип данных
Ключ это любой хешируемый объект т.е. любой неизменяемый объект
поддерживает создание генератором словаря
"""
d = dict(none123=None)
d = {None: None, **d}
myDict = {x: x**2 for x in [1,2,3,4,5]}
print(myDict)
d[1] = 1
d = d | {2: 2}
_ = d.setdefault(3, 3)
_ = d.get(4)
d.pop(1)
d.items()
d.keys()
d.values()
  dictionary sorting using Lambda
sort_me = [{'age': 10001}, {'age': 23}]
sort_me.sort(key=lambda sort_me: sort_me['age'])
print(sort_me)


# ...


