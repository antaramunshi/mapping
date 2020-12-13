import folium
import pandas

data = pandas.read_csv("Volcanoes.csv")
lat= list(data["LAT"])
lon= list(data["LON"])
elev= list(data["ELEV"])
map = folium.Map(location= [40,-100], tiles= "Stamen Terrain ")
fg= folium.FeatureGroup(name= "My Map")
for lt, ln, el in zip (lat,lon,elev):
    fg.add_child(folium.Marker(location = [lt , ln ], popup=str(el)+" m" , icon=folium.Icon(color='green')))

map.add_child(fg)
map.save("Map1.html")
