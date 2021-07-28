import numpy

# normal python list
list = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]

# numpy array
arr1 = numpy.arange(27)
print(arr1)

# shaping array two dimension
arr2 = arr1.reshape(3, 9)
print(arr2)

# shaping array three dimension
arr3 = arr1.reshape(3, 3, 3)
print(arr3)

# converting python list to numpy array
arr4 = numpy.asarray([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
print(arr4)

