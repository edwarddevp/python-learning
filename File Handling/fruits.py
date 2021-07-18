import os


def read_or_write():
    user_input = ''
    while user_input != 'e':
        print("- What do you want to do in fruits.txt file?\n")
        print(" * create(c)?")
        print(" * read(r)?")
        print(" * write(w)?")
        print(" * append(a)?")
        print(" * get lenght of each line(l)?")
        print(" * delete(d)?")
        print(" * exit(e)?\n")
        user_input = str(
            input('Enter you answer: ')).lower().strip()
        if user_input == 'r':
            readFile()
        elif user_input == 'c':
            createFile()
        elif user_input == 'w':
            writeFile()
        elif user_input == 'a':
            appendFile()
        elif user_input == 'l':
            lenghtOfLines()
        elif user_input == 'd':
            deleteFile()
        else:
            print("Error, please enter a valid action\n")
    print("\nThanks for coming\n")


def createFile():
    if os.path.exists("fruits.txt"):
        print("\nFile \"fruits,txt\" already exists\n")
    else:
        file = open("fruits.txt", 'w')
        file.close()
        print("\nFile created successfully\n")


def writeFile():
    # using with the file closes automatically at the end of the block
    with open("fruits.txt", 'w') as file:
        lines = ["pear", "apple", "orange",
                 "mandarin", "watermelon", "pomegranate"]
        for line in lines:
            file.write(line + "\n")

    print("\nFile written successfully\n")


def appendFile():
    # using with the file closes automatically at the end of the block
    with open("fruits.txt", 'a') as file:
        lines = ["pear", "apple", "orange",
                 "mandarin", "watermelon", "pomegranate"]
        for line in lines:
            file.write(line + "\n")

    print("\nFile appended successfully\n")


def readFile():
    # using with the file closes automatically at the end of the block
    try:
        with open("fruits.txt", 'r') as file:
            content = file.read()
            if(content):
                print("\n"+content)
                print("File read successfully\n")
            else:
                print("\nThe file is empty\n")
    except FileNotFoundError:
        print("\nThe file has not been found, please create it first \n")


def lenghtOfLines():
    # using with the file closes automatically at the end of the block
    try:
        with open("fruits.txt", 'r') as file:
            content = file.readlines()
            if(len(content) > 0):
                for line in content:
                    print(str(len(line.strip())))
                print("\nFile read successfully\n")
            else:
                print("\nThe file is empty\n")
    except FileNotFoundError:
        print("\nThe file has not been found, please create it first \n")


def deleteFile():
    if os.path.exists("fruits.txt"):
        os.remove("fruits.txt")
        print("\nFile deleted successfully\n")
    else:
        print("\nThe file does not exist\n")


try:
    read_or_write()
except KeyboardInterrupt:
    print("\n\nThanks for coming\n")
