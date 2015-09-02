# without passing arguments to the `decorate_me` function
def decorator(func):
    def inner():
        print('before decorating')
        func()
        print('after decorating')
    return inner

def decorate_me():
    print 'yay ! i was decorated here.'

catch_inner = decorator(decorate_me)
catch_inner()

# OUTPUT :
# before decorating
# yey ! i was decorated here.
# after decorating




## Writing the same thing using the decorator syntax

# @decorator
# def another_decorate_me():
    # print 'Even I was decorated.Yay!'

## Now call the decorated function directly
# another_decorate_me()

# OUTPUT
# before decorating
# Even I was decorated.Yay!
# after decorating
