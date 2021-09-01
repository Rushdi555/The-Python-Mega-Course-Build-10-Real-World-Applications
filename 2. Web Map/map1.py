import folium
import pandas

volcanoes = pandas.read_csv("Volcanoes.txt")
lat_vol = list(volcanoes["LAT"])
lon_vol = list(volcanoes["LON"])
name_vol = list(volcanoes["NAME"])
elev_vol = list(volcanoes["ELEV"])
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22+volcano" target="_blank">%s</a><br>
Height: %s m
"""

def color_producer(elevation):
    if elevation<1000:
        return 'green'
    elif 1000 <= elevation <3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[38.58,-99.09],zoom_start=6)
#can use different tiles using (tiles="Stamen Terrain",etc)

fgv = folium.FeatureGroup(name='volcanoes')

for lt, ln,name, elev in zip(lat_vol,lon_vol,name_vol,elev_vol):
    iframe = folium.IFrame(html=html % (name,name,elev), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(iframe), 
    fill_color=color_producer(elev), color='grey', fill_opacity=0.7, radius=5))

fgp = folium.FeatureGroup(name='population')

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] <10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] <50000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")