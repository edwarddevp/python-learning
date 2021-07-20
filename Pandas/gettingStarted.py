import pandas

df = pandas.DataFrame([[2, 4, 6], [10, 20, 30]])

df_columns = pandas.DataFrame([[2, 4, 6], [10, 20, 30]],
                              columns=["Price", "Age", "Value"])

df_columns_index = pandas.DataFrame([[2, 4, 6], [10, 20, 30]],
                                    columns=["Price", "Age", "Value"],
                                    index=["first", "second"])

df_columns_dictionaries = pandas.DataFrame([{
    'name': 'Jhon',
    'age': 24
}, {
    'name': 'jack',
    'age': 21
}, {
    'name': 'James',
    'age': 18
}])

print(df_columns)
print(df_columns.mean())  # get average of each column
# get average of the total average of every column
print(df_columns.mean().mean())
print(df_columns.Price.mean())  # get average of Price column
