import folium

def plot_route(route_points, filename="optimized_route_map.html", emergency_location=None, user_location=None):
    map_center = [route_points[0]['lat'], route_points[0]['lon']]
    route_map = folium.Map(location=map_center, zoom_start=14)

    for index, stop in enumerate(route_points):
        label = chr(65 + index % 26)
        folium.Marker(
            location=[stop['lat'], stop['lon']],
            popup=f"{label}. {stop['input']['Address']}",
            icon=folium.Icon(color='blue' if index == 0 else 'green')
        ).add_to(route_map)

    if emergency_location:
        folium.Marker(
            location=[emergency_location['lat'], emergency_location['lon']],
            popup=f"Emergency: {emergency_location['input']['Address']}",
            icon=folium.Icon(color='red')
        ).add_to(route_map)

    if user_location:
        folium.Marker(
            location=[user_location['lat'], user_location['lon']],
            popup=f"Your Location: {user_location['input']['Address']}",
            icon=folium.Icon(color='orange')
        ).add_to(route_map)

    route_coordinates = [(stop['lat'], stop['lon']) for stop in route_points]

    if route_coordinates[0] != route_coordinates[-1]:
        route_coordinates.append(route_coordinates[0])

    folium.PolyLine(locations=route_coordinates, color='red', weight=5).add_to(route_map)

    route_map.save(filename)
