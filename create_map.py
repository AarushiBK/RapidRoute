import folium

def plot_route(route_points, filename="optimized_route_map.html", emergency_location=None, user_location=None):
    # Create a map centered around the first address
    map_center = [route_points[0]['lat'], route_points[0]['lon']]
    route_map = folium.Map(location=map_center, zoom_start=14)

    # Add markers for each address with order (A, B, C, ...)
    for index, stop in enumerate(route_points):
        label = chr(65 + index % 26)  # Allow more than 26 stops
        folium.Marker(
            location=[stop['lat'], stop['lon']],
            popup=f"{label}. {stop['input']['Address']}",
            icon=folium.Icon(color='blue' if index == 0 else 'green')
        ).add_to(route_map)

    # If there is an emergency location, add it to the map
    if emergency_location:
        folium.Marker(
            location=[emergency_location['lat'], emergency_location['lon']],
            popup=f"Emergency: {emergency_location['input']['Address']}",
            icon=folium.Icon(color='red')
        ).add_to(route_map)

    # If user location is provided, add it to the map
    if user_location:
        folium.Marker(
            location=[user_location['lat'], user_location['lon']],
            popup=f"Your Location: {user_location['input']['Address']}",
            icon=folium.Icon(color='orange')
        ).add_to(route_map)

    # Route coordinates
    route_coordinates = [(stop['lat'], stop['lon']) for stop in route_points]

    # Add line to close the loop if not already present
    if route_coordinates[0] != route_coordinates[-1]:
        route_coordinates.append(route_coordinates[0])  # Return to start

    folium.PolyLine(locations=route_coordinates, color='red', weight=5).add_to(route_map)

    # Save the map
    route_map.save(filename)