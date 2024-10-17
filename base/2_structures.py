"""
Basic data structures
"""
# 1. How to create / modify / delete
# 2. Modifiable / immutable objects
# 3. Basic methods of basic structures
a = []
a = list()
a = [1] * 10
a = [1, 2, 3] + [3, 4, 5]
a = [*a]
a.append(a)
a.pop()
a.extend(a)

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
                                                      String
------------------------------------------------------------------------------------------------------------------







# TUPLE

b = (1, 2, a)
b = tuple([1, 2])
b = b[:]
b, _ = b
# TUPLE

# SET 
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

d = dict(none123=None)
d = {None: None, **d}
d[1] = 1
d = d | {2: 2}
_ = d.setdefault(3, 3)
_ = d.get(4)
d.pop(1)
d.items()
d.keys()
d.values()
# ...
