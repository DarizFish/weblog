

def first(func):
    def decorator(*k, **kw):
        print(1)
        return func(*k, **kw)
    return decorator

def second(func):
    def decorator(*k, **kw):
        print(2)
        return func(*k, **kw)
    return decorator


def test1():
    pass

test1 = first(test1)
test1 = second(test1)

test1()
