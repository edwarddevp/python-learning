import datetime
import time

now = datetime.datetime.now()  # get current date
otherDate = datetime.datetime(2016, 5, 13, 11, 0, 0, 0)  # get current date

# print("\nNow and other date\n")

# print(now)
# print(otherDate)

# print("\nTime Between\n")

# time_between = now - otherDate

# print(time_between)
# print(str(time_between.days) + " days")
# print(str(time_between.total_seconds()) + " seconds")

# print("\nAdd two days\n")

# after = now + datetime.timedelta(days=2)
# print(after)

# print("")


def create_file(fileName, body):
    with open(fileName+".txt", "w") as file:
        file.write(body)


# create_file(now.strftime("%Y-%m-%d-%H-%M-%S-%f"), now.strftime("%B %Y %d"))

# Time Module
# Put the script to sleep

list = []
for i in range(5):
    list.append(datetime.datetime.now())
    time.sleep(2)
print(list)
