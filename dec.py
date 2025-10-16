import functools

def top_func(func, *args):
    print("begin")
    print(func(*args))
    print("end")


def decorator(func):
    def wrap(*args):
        count = 0
        while count < 10:
            func(*args)
            count +=1       
    return wrap


def param_decorator(limit):
    def decorator(func):
        @functools.wraps(func)
        def wrap(*args):
            count = 0
            while count < limit:
                func(*args)
                count +=1 
                print(count)      
        return wrap
    return decorator



@decorator
def my_func(x: int, y: int) -> int:
    print(x + y)

# @param_decorator(33)
# def privet():
#     """ Say Hello"""
#     print("Hello")


class ClassDecorator:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *arg, **kwargs):
        count = 0
        while count < 10:
            self.func(*arg, **kwargs)
            count +=1 
            print(count)     

def param_class_decor(count):
    class ClassDecorator:
        def __init__(self, func):
            functools.update_wrapper(self, func)
            self.func = func
            self.count = count

        def __call__(self, *arg, **kwargs):
            count = 0
            while count < self.count:
                self.func(*arg, **kwargs)
                count +=1 
                print(count)     

    return ClassDecorator



@param_class_decor(29)
def privet():
    """ Say Hello"""
    print("Hello")


if __name__ == "__main__":

    # my_func(2, 2)

    # privet()

    # print(privet.__name__)
    # print(privet.__doc__)

    privet()
    