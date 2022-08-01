# This is a sample Python script.

#print(movie.watchable());
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
class Decoratordemo():
    def __init__(self):
        print("Inside init ctor")
    def __call__(self):
        print("I am the parent being called")

#@Decoratordemo
def decorator():
    print("Inside decorated function")

class MyCustomDecorator(Decoratordemo):
    def __init__(self):
        print("My own ctor")
        #func(1,2)

    def __call__(self, a, b):
        print("Inside custom.call()", a + b)

#@MyCustomDecorator
def custom(a, b):
   print(a + b)




class DecoratorManyArgs():
    def __init__(self, arg1, arg2):
        print("Decorator with many arguments", arg1, arg2)


    def __call__(self, func):
        def wrapped_func(*args):
            func(*args)
        return wrapped_func

@DecoratorManyArgs("Hello", "Decorators_without_args")
def decoratedFunc(arg1, arg2):
    print("I am the celebrity function with args", arg1, arg2)

if __name__ == '__main__':
     decoratedFunc("Hi", "How are you")




