# first define A normal function in python which returns something
# def function_returns_something(arg1=4, arg2=5):
#     return arg1+arg2

# function_returns_something(2,6)

# a surprise : python function can return a function
def function_returned(arg1="Hello"):
    print '%s' % arg1

def function_returns_another_function():
    return function_returned
    # print 'before calling returned function'
    # funct('I have returned a function here !')
    # print 'after calling returned function'

call_me = function_returns_another_function()
print call_me.__name__   # ouput : function_returned
call_me('call me here !')

# function_returns_another_function(function_returned)