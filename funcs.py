import functools



def test1():
    print('hello!')

def normaali(argi):
    print(argi())

# 1) Write a normal function that accepts another function as an argument. Output the result of that other function in your “normal” function.
normaali(test1)


# 2) Call your “normal” function by passing a lambda function – which performs any operation of your choice – as an argument.
normaali(lambda: print('huu'))

# 3) Tweak your normal function by allowing an infinite amount of arguments on which your lambda function will be executed.     



# 4) Format the output of your “normal” function such that numbers look nice and are centered in a 20 character column.