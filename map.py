import folium
map = folium.Map(location= [40,-100], tiles= "Stamen Terrain ")
fg= folium.FeatureGroup(name= "My Map")
for coordinates in [[38.2,-99.1],[37.2,-99]]:
    fg.add_child(folium.Marker(location = coordinates, popup="Its a Marker" , icon=folium.Icon(color='green')))

map.add_child(fg)
map.save("Map1.html")
