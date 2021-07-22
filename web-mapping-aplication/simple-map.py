import folium


# creating map class
map = folium.Map(location=[38.5, 58.7], zoom_start=6)

# creating a feature Group
fg = folium.FeatureGroup(name="My Map")

# adding a single point
# fg.add_child(folium.Marker(
#     location=[36, 98], popup="HIIIIII I am a marker", icon=folium.Icon(color='green')))

# adding many points
for coordinates in [[36, 98], [39, 97]]:
    fg.add_child(folium.Marker(
        location=coordinates, popup="HIIIIII I am a marker", icon=folium.Icon(color='green')))


# adding feature Group
map.add_child(fg)

map.save("simple-map-example.html")
