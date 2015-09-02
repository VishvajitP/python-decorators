# Passing arguments to the decorated function

def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):
       print 'I got args! Look: %s, %s' %(arg1, arg2)
       function_to_decorate(arg1, arg2)
    return a_wrapper_accepting_arguments

# Since you are calling the wrapper function which is returned by the decorator,
# passing arguments to the wrapper will let it pass those to the decorated function

@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print 'My full name is: %s %s' %(first_name, last_name)

print_full_name('Vishvajit', 'Pathak')

# here `a_wrapper_accepting_arguments` remembers the arguments passed to
# `print_full_name`; this concept is called `closure` in python

# as we cant say what parameters will be passed to the decorated function
# we usually pass (*args, **kwargs) to the wrapper function
# eg:
# def a_decorator_passing_arguments(func):
#     def inner(*args, **kwargs):
#         func(*args, **kwargs)
#     return inner
