import sys
import copy

# количество имён в sys
print(len(dir(sys)))
print(len([x for x in dir(sys) if not x.startswith('__')]))


names = ['alex', 'pasha', 'novik']
print(id(list))
names_1 = copy.deepcopy(names)
print(names_1[1] is names[1])