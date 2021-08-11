from functools import wraps

def bold(func):
    '''This is the bold function'''
    @wraps(func)
    def wrapper():
        '''This is the wrapper function'''
        result = "<b>" + func() + "</b>"
        return result
    return wrapper

def italic(func):
    '''This is the italic function'''
    @wraps(func)
    def wrapper():
        '''This is the wrapper function'''
        result = "<i>" + func() + "</i>"
        return result
    return wrapper

@bold
@italic
def printfib():
    '''return Fibonacci'''
    return 'Fibonacci'

print(printfib())
