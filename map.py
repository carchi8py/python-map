import folium
import pandas

df = pandas.read_csv("Volcanoes-USA.txt")
map = folium.Map(location=[45.372,-121.697], zoom_start = 6, tiles = "Stamen Terrain")
for lat, lon, name in zip(df['LAT'], df['LON'], df['NAME']):
    map.simple_marker(location = [lat,lon], popup = name, marker_color="red")

map.save("test.html")