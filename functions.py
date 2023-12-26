# a reusable block of code ,we can pass arguments , easy to maintain

# funtion to greet a user
# we have to define a function before calling it
def greet(name):
    print(f"Marhaba! {name.capitalize()}")


greet('osman gani')


# addition function

def add(num1, num2):
    print(f'{num1} + {num2} = {num1 + num2}')


add(9, 9)  # positional argument

# here a very important concept is "POSITIONAL argument and KEYWORD argument"
# e.g.

add(num1=5, num2=8)  # keyword argument
add(5, num2=5)  # mix , use keyword argument after the positional argument


# Tip: generally use positional argument
# but if we are supplying numerical value to the function
# which can be quite confusing, then use keyword argument

# voting machine

def can_vote(age):
    if age >= 18:
        return True
    else:
        return False


print(can_vote(19))

# by default function return 'None'
