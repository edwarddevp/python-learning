import pandas

df1 = pandas.read_csv("https://pythonhow.com/supermarkets.csv")

print(df1)

df2 = df1.loc[0:1, "City":"Country"]

print(df2)

df3 = df1.loc[0, "Country"]

print(df3)

df4 = df1.loc[:, "Country"]

print(df4)
