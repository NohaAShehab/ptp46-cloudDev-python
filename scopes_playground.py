
"""lexical scoping """
""" --------------- global scope ----------------"""
name = 'ahmed'

print(name)


def test_global_scope():
    print(f'from inside the function name= {name}')

test_global_scope()

"""----------- local scoping -----------"""
"""
    any variable defined inside a function --> its scope --> local scope 
    can be accessed only inside the function 
"""


def sum_num():
    num1 = 10
    num2 = 20
    res = num1 + num2
    print(f'num1= {num1}, num2= {num2}, res= {res}')

sum_num()
print("-----------------")

print(num1, num2, res ) # NameError: name 'num1' is not defined












