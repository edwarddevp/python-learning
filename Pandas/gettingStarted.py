import pandas

df = pandas.DataFrame([[2, 4, 6], [10, 20, 30]])

df_columns = pandas.DataFrame([[2, 4, 6], [10, 20, 30]],
                              columns=["Price", "Age", "Value"])

df_columns_index = pandas.DataFrame([[2, 4, 6], [10, 20, 30]],
                              columns=["Price", "Age", "Value"],
                              index=["first","second"])

print(df_columns)
