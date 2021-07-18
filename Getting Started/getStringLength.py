# def getStringLength(string):
#     if (type(string) == int or type(string) == float):
#         return "Sorry, numbers don't have length"
#     else:
#         return len(string)


# userInput = input("Write the sentences to count: ")

# print("The length of the sentences is: " + str(getStringLength(userInput)))


def is_number_replace_isdigit(s):
    return s.replace('.', '', 1).isdigit()


def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


def word_length(word):
    return len(word)


string = input("insertar palabra: ")
if is_number(string):
    print("numbers don't do the thing here")
else:
    print(word_length(string))
