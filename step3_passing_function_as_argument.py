# If a function can return a function, then a function can also take a function
# as an argument

# Defining a function which we will pass as an argument to another function
def scream(word = 'yes'):
    return '%s!' %(word.upper())

# Function taking a function as argument
def do_something_before(func):

    # Do something before calling the passed function
    print "I do something before then I call the function you gave me"

    # Now call the passed function
    print func()

do_something_before(scream)
# Outputs:
# I do something before then I call the function you gave me
# YES!