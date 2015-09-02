# a surprise : python function can return a function
def function_returned(arg1="Hello"):
    print '%s' % arg1

def function_returns_another_function():  # a first class function
    return function_returned    # returning a function

catch_function_returned = function_returns_another_function()
# print catch_function_returned.__name__   # ouput : function_returned
catch_function_returned('call me here !')
