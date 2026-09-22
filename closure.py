def outer_func(msg):
    message = msg
    def inner_func():
        print(message)
    return inner_func   # returning the function without executing it

Hi_func = outer_func('Hi')

Hello_func = outer_func('Hello')

Hi_func()
Hello_func()