import time             # imported to get the time

def decorating(func):
    def inner_decorator(*args):
        print("starting of function")
        func(*args)                         # here the sub method will be called because that is being decorated
        print("ending of the function")
    return inner_decorator

# This is a simple function without decoration
def add(a,b):
    return a+b

add(3,4)


# This is a simple function with decoration
@decorating             
def sub(a,b):          # this method sub is passed as input to the decorating method 
    print(a-b)

sub(6,3)




# calculating the time of program execution

def test_time(func):
    def inner_test_time():
        start = time.time()
        func()
        end = time.time()
        print(end - start)

    return inner_test_time


@test_time
def test():
    print(4+8)
    print(7+9)


test()

@test_time
def loop():
    for i in range(1000000):
        pass


loop()