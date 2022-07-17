# we are going to plot a basic base map
# Folium is a powered Python library that
# helps you create several types of Leaflet maps.

import folium as fo

map = fo.Map()
# Displaying map
print(map)

# Adding child
# Open google search the latitude and longitude of 27.1751N, 78.0421E
# TajMahal and Paste 

x = fo.Featuregroup(name="My Map")
x.add_child(fo.Marker(location=[27.1750, 78.0422], popup="hello", icon=fo.Icon(color="green")))
map.add_child(x)

# Multiple Markers
# Here we are going to use for loop 
# and we will use one for latitude and 
# one for longitude

for lat,lon in ([34, 53], [24, -50], [90, -68]):
	x.add_child(fo.Marker(location-[lat,lon], popup="hello", icon=fo.Icon(color="red")))
map.add_child(x)


