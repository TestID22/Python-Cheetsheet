"""
try/execpt in func
"""
def indexer(obj, index):
    return obj[index]

def catcher(name, index):
    try:
        print(indexer(name, index))
    except:
        print(f"index: {index} is out of range in {name}")
    print("try/catch was successfull")

catcher("ALEX", 7)
# output:
# index: 7 is out of range in ALEX
# try/catch was successfull 
"""
end of try/execpt in func
"""

def finally_indexer(obj, index):
    return obj[index]

def finally_catcher(name, index):
    try:
        print(indexer(name, index))
    finally:
        print(f"I am executed anyway")

finally_catcher("ALEX", 3)


"""
Raise execption manualy 
"""
# throw exeption
def usless_index_error_thorwer():
    try:
        raise IndexError
    except:
        print("got IndexError")

usless_index_error_thorwer()

"""
Custom Exception
"""
class AlreadyGotOne(Exception): pass

def getOne():
    raise AlreadyGotOne()

try:
    getOne()
except AlreadyGotOne as ago: # "as" Operator provides access to exception obj
    print(f"{ago.__ne__}got ALREADYGotOne")
"""
end custom Exception
"""

