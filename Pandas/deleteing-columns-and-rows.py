import pandas

df = pandas.read_csv("supermarkets.csv")
print(df)

# drop columns
print(df.drop(columns=["City", "ID"]))

# drop index
print(df.drop(index=[0, 3]))

# drop both
print(df.drop(columns=["City", "ID"], index=[0, 3]))

# drop columns 0 to 3
droprange = list(range(0, 4))
print(df.drop(df.columns[droprange], axis=1))


# axis
# 0: index, 1: columns
# defa  ult 0
