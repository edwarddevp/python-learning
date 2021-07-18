# # For loops
# emails = ["email1@email.com", "email2@gmail.com", "email3@email.com"]
#
# for email in emails:
#     print(email)
#     pass

# # For loops advance
# emails = ["email1@email.com", "email2@gmail.com", "email3@email.com"]

# for email in emails:
#     if 'gmail' in email:
#         print(email)
#     # else:  # (optional)
#     #     pass

# # For loops advance
# password = input("Enter your password: ")

# while password != "asd123":
#     print("Sorry, try again")
#     password = input("Enter your password: ")

# print("You are logged in")

# # loop two lists
# names = ['james', 'jhon', 'jack']
# email_domains = ['gmail', 'hotmail', 'yahooo']

# for i, j in zip(names, email_domains):
#     print(i, j)


# inline for

names = ['james\n', 'jhon\n', 'jack\n']
print(names)
names = [i.replace('\n','') for i in names]
print(names)
