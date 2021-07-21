import numpy
import cv2

img = cv2.imread('./smallgray.png')

# slicing and merging arrays
print()
print(img[0:2, 2:4])

# merge horizontally
print("\n\nmerge horizontally\n")
result = numpy.hstack((img, img))
print(result)

# merge vertically
print("\n\nmerge vertically\n")
result = numpy.vstack((img, img))
print(result)

# splitting horizontally
print("\n\nsplitting horizontally\n")
result = numpy.hsplit(img, 5)
print(result)

# splitting vertically
print("\n\nsplitting vertically\n")
result = numpy.vsplit(img, 3)
print(result)
