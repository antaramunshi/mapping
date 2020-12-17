import folium
import pandas

data = pandas.read_csv("Volcanoes.csv")
lat= list(data["LAT"])
lon= list(data["LON"])
elev= list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'

html = """<h4>Volcano information:</h4>
Height: %s m
"""

map = folium.Map(location= [40,-100], tiles= "Stamen Terrain ")
fg= folium.FeatureGroup(name= "My Map")

for lt, ln, el in zip (lat,lon,elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fg.add_child(folium.CircleMarker(location = [lt , ln ], radius= 6 , popup=str(el)+" m" , 
    fill_color= color_producer(el) ,color='grey', fill_opacity = 0.7))
 
fg.add_child(folium.GeoJson(data= open('world.json' , 'r' , encoding='utf-8-sig').read()))
map.add_child(fg)

map.save("Map1.html")
