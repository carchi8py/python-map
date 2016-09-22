import folium
import pandas

def color(elev):
    color_name = 'red'
    if elev in range(0,1000):
        color_name = "green"
    elif elev in range(1000,3000):
        color_name = "orange"
    return color_name

df = pandas.read_csv("Volcanoes-USA.txt")
map = folium.Map(location=[df['LAT'].mean(),df['LON'].mean()], zoom_start = 6, tiles = "Stamen Terrain")
for lat, lon, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    map.add_child(folium.Marker(location = [lat,lon], popup = name, icon = folium.Icon(color=color(elev), icon_color="green")))

map.save("test.html")