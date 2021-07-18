# def celsiusToFarenheit(celsius):
#     if celsius > -273.15:
#         return celsius * 9 / 5 + 32
#     else:
#         print("Not a valid temperature")
#
#
# celsius = input("Write the celsius unit to be converted to farenheit: ")
#
# try:
#     farenheit = celsiusToFarenheit(float(celsius))
#     if(farenheit is not None):
#         print("Celsius: " + str(celsius) + " fahrenheit: " + str(farenheit))
# except ValueError:
#     print("Not a valid temperature")

# # Iterate
# temperatures = [10, -20, -289, 100]


# def celsiusToFarenheit(celsius):
#     if celsius > -273.15:
#         return celsius * 9 / 5 + 32
#     else:
#         return "Not a valid temperature"


# for temperature in temperatures:
#     print(celsiusToFarenheit(temperature))


# This is wrong look here for more info
# https://adamj.eu/tech/2020/01/21/why-does-python-3-8-syntaxwarning-for-is-literal/
# x = int(2000.0)
# if x is 2000:
#     print("It's 1000!")
