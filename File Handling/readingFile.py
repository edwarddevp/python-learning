file = open("example.txt", 'r')

content = file.read()

print("\nText file bare content: \n" + content)

file.seek(0)

content = file.readlines()

print("Text file bare lines: \n" + str(content))

content = [i.replace("\n", "") for i in content]

print("\nText file lines replacing \\n: \n" + str(content) + "\n")

file.close()
