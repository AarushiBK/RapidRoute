import itertools
from math import sin, cos, acos, radians, inf

def calculate_distance(lat1, lon1, lat2, lon2):
    lat1_rad, lon1_rad = radians(lat1), radians(lon1)
    lat2_rad, lon2_rad = radians(lat2), radians(lon2)

    A = sin(lat1_rad) * sin(lat2_rad) + cos(lat1_rad) * cos(lat2_rad) * cos(lon2_rad - lon1_rad)
    A = min(1, max(A, -1))
    D = 3959 * acos(A)
    return D

def shortest_route(enriched_addresses):
    starting_point = enriched_addresses[0]
    other_addresses = enriched_addresses[1:]

    best_route = None
    min_distance = inf

    for perm in itertools.permutations(other_addresses):
        route = [starting_point] + list(perm)

        total_distance = 0
        for i in range(len(route) - 1):
            total_distance += calculate_distance(
                route[i]['lat'], route[i]['lon'], route[i+1]['lat'], route[i+1]['lon']
            )

        total_distance += calculate_distance(
            route[-1]['lat'], route[-1]['lon'], starting_point['lat'], starting_point['lon']
        )
        
        if total_distance < min_distance:
            min_distance = total_distance
            best_route = route

    return best_route, min_distance

def distance_between_points(point1, point2):
    return calculate_distance(point1['lat'], point1['lon'], point2['lat'], point2['lon'])
