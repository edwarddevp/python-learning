import pandas

df = pandas.read_csv("supermarkets.csv")

print(df)

df["Series"] = ['a', 'b', 'c', 'd', 'e', 'f']

print(df)

df["Series2"] = df.shape[1] * ['a']

print(df)

# df.shape (2,5) = (index,columns)
# df.shape[0]  rows len
# df.shape[1]  columns len

# updating column
df['Series3'] = df["Series"] + ',' + ' text'
print(df)

# adding Row
df = df.append({'City': "MCBO", 'ID': "10", "State": "Zulia",
                "Name": 'Jhon'}, ignore_index=True)  # ignore_index require in case we are inserting dict
