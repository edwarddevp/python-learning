import folium
import pandas


def getPopupColor(elevation):
    if(elevation < 1000):
        return 'green'
    elif(1000 <= elevation < 3000):
        return 'orange'
    else:
        return 'red'


# loading volvanoes file
df = pandas.read_csv("Volcanoes_USA.txt")

# creating map class
map = folium.Map(location=[48.5, -121], zoom_start=6)

# creating a feature Group
fgPointers = folium.FeatureGroup(name="Population")
fgGeoJson = folium.FeatureGroup(name="Volcanoes")

# adding points from volcanoes file
df.apply(lambda x: fgPointers.add_child(folium.Marker(
    location=[x["LAT"], x["LON"]], popup=x["NAME"] +
    ". Elevation: " + str(x["ELEV"]) + "m",
    icon=folium.Icon(color=getPopupColor(x["ELEV"])))), axis=1)


# adding geoJson
fgGeoJson.add_child(folium.GeoJson(
    data=open('world.json', 'r', encoding='utf-8-sig').read(),
    style_function=lambda x: {
        'fillColor': 'green'
        if x['properties']['POP2005'] < 10000000 else 'orange'
        if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


# adding feature Group
map.add_child(fgPointers)
map.add_child(fgGeoJson)

# adding layer controller
map.add_child(folium.LayerControl())

map.save("map-volcanoes.html")
