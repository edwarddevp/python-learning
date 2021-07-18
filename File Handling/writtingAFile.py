file = open("example.txt", 'w')

lines = ["Custom Line 1", "Custom Line 2", "Custom Line 3"]

for line in lines:
    file.write(line + "\n")

file.close()
