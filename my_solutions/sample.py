from logacall import logged, logformat

logged= logformat('Calling {func.__name__}')

@logged
def add(x,y):
    return x+y

@logged
def sub(x,y):
    return x-y

# from logacall import logformat
@logged
def mul(x,y):
    return x*y