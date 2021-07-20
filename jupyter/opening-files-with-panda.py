import pandas
import os

print(os.listdir())

df1 = pandas.read_csv("supermarkets.csv")
print(df1)

print(df1.set_index("ID"))  # setting other id

df2 = pandas.read_json("supermarkets.json")
print(df2)

df3 = pandas.read_excel("supermarkets.xls", sheet_name=0)
print(df3)

df4 = pandas.read_csv("supermarkets_commas.txt")
print(df4)

df5 = pandas.read_csv("supermarkets_semi-colons.txt", sep=";")
print(df5)

df6 = pandas.read_csv("https://pythonhow.com/supermarkets.csv")
print(df6)
