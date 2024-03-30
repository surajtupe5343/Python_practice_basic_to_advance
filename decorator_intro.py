def decorator_func(any_func):
    def wraped_func():
        print("This is awesome function..!")
        any_func()
    return wraped_func

# @decorator_func # ---> Shortcut for Decorator function
def func1():
    print("This is func1.")

@decorator_func
def func2():
    print("This is func2.")

func1()
func2()

var = decorator_func(func1) # ---> longcut for Decorator function
var()