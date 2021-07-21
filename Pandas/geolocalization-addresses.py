from geopy.geocoders import Nominatim
import pandas

df = pandas.read_csv("supermarkets.csv")
print(df)

nom = Nominatim(user_agent='sample-email@gmail.com')
# https://stackoverflow.com/questions/52600278/correct-way-to-use-geopy-nominatim


# get direction coordinates
# n = nom.geocode("3995 23rd St, San Francisco, CA 94114")
# print(n)

# using geopy with pandas
df["Location"] = df['Address'] + ", " + df['City'] + \
    ", " + df["State"] + ", " + df["Country"]

df["Coordinates"] = df["Location"].apply(nom.geocode)
print(df)


df["Latitude"] = df["Coordinates"].apply(
    lambda x: x.latitude if x != None else None)  # validate none
print(df)
