# With file handling
temperatures = [10, -20, -289, 100]


def writeCelsiusToFarenheit(temperatures, filepath):
    with open(filepath, 'w') as file:
        for celsius in temperatures:
            if celsius > -273.15:
                fahrenheit = celsius*9/5+32
                file.write(str(fahrenheit)+"\n")


writeCelsiusToFarenheit(temperatures, 'Farenheit.txt')
