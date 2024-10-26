def line_separator(func):
    def wrapper(*args, **kwargs):
        print(f'-------------------{func.__name__}------------->')
        result = func(*args, **kwargs)
        print(f'-------------------{func.__name__}------------->')
        print('\n')
        return result
    return wrapper
        

"""
try/execpt in func
"""
def indexer(obj, index):
    return obj[index]

@line_separator
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

"""
try/finally
"""
def finally_indexer(obj, index):
    return obj[index]

@line_separator
def finally_catcher(name, index):
    try:
        print(indexer(name, index))
    finally:
        print(f"I am executed anyway")

finally_catcher("ALEX", 3)
"""
try/finally
"""

"""
Raise execption manualy 
"""
# throw exeption
@line_separator
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
@line_separator
def class_ex_catcher():
    try:
        getOne()
    except AlreadyGotOne as ago: # "as" Operator provides access to exception obj
        print(f"{ago} got ALREADYGotOne")
class_ex_catcher()
"""
end custom Exception
"""


"""
try/except/else/finally
"""
@line_separator
def try_except_else_finally():
    try:
        print(f"{10 / 2}")
    except:
        print("EXECPTioN is here")  # выполнится, если try c исключениями
    else:
        print("there are no erros") # выполнится, если try без исключений
    finally:
        print(f"{try_except_else_finally.__name__} finished") # выпаолнятеся всегда

try_except_else_finally()
"""
try/except/else/finally
"""



