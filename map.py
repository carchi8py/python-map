import folium
import pandas

df = pandas.read_csv("Volcanoes-USA.txt")
map = folium.Map(location=[45.372,-121.697], zoom_start = 6, tiles = "Stamen Terrain")
for lat, lon, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    color = 'red'
    if elev in range(0,1000):
        color = "green"
    elif elev in range(1000,3000):
        color = "orange"
    map.simple_marker(location = [lat,lon], popup = name, marker_color=color)

map.save("test.html")