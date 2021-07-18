# syntax error
# print(1)
# int(9)
# int 1  # syntax error
# a = [5, 2, 3 )  # syntax error
# print 1  # syntax error


# exceptions
# a = 1
# b = "2"
# print(int(2.5))
# print(a + b)
# exception TypeError unsupported operand type(s) for +: 'int' and 'str'
# print(c)
# NameError: name 'c' is not defined
# print(c/0)
# NameError: name 'c' is not defined

# Handling errors
def divide(a, b):  # function definition (def)
    try:
        return a / b
    except Exception:
        print("Zero Division is meaningless")


print(divide(1, 0))

# important note: execpt will cacth all kind of errors
# even the ones we dont want to cacth for this you have to tell except
# what kind of errors you want to cacth like this: except Exception:
