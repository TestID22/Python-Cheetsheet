import sys
import copy

# количество имён в sys
print(len(dir(sys)))
print(len([x for x in dir(sys) if not x.startswith('__')]))


names = ['alex', 'pasha', 'novik']
# print(id(list))
names_1 = copy.deepcopy(names)
# print(names_1[1] is names[1])


# using % 
OTP = 123
name = "Alex"
message = """Hello %s, %d"""% (name, OTP)
print(message)

# using .format()
text = "text {0} + {1}".format('Alex', 2)
print(text)


l = list(range(1, 11))
print(l)

l.extend(l)
print(l)