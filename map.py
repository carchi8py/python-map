import folium
map = folium.Map(location=[45.372,-121.697], zoom_start = 12, tiles = "Stamen Terrain")
map.create_map(path="test.html")