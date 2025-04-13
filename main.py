from personator_api import enrich_address
from route_optimizer import shortest_route, distance_between_points
from create_map import plot_route

safe_locations = {
    "wildfire/disaster": [
        {"Address": "600 Parkcenter Drive", "City": "Santa Ana", "State": "CA", "Zip": "92705"},
    ],
    "shelters": [
        {"Address": "8 Thomas", "City": "Irvine", "State": "CA", "Zip": "92618"},
        {"Address": "1 Hope Drive", "City": "Tustin", "State": "CA", "Zip": "92618"},
        {"Address": "10200 Pioneer Rd", "City": "Tustin", "State": "CA", "Zip": "92782"},
    ],
    "hospitals": [
        {"Address": "16200 Sand Canyon Ave", "City": "Irvine", "State": "CA", "Zip": "92618"},
        {"Address": "6640 Alton Pkwy", "City": "Irvine", "State": "CA", "Zip": "92618"},
        {"Address": "101 The City Drive South", "City": "Orange", "State": "CA", "Zip": "92868"},
    ],
    "police_stations": [
        {"Address": "1 Civic Center Plaza", "City": "Irvine", "State": "CA", "Zip": "92606"},
        {"Address": "410 E Peltason Dr", "City": "Irvine", "State": "CA", "Zip": "92697"},
        {"Address": "300 Centennial Way", "City": "Tustin", "State": "CA", "Zip": "92780"},
        {"Address": "20202 Windrow Dr", "City": "Lake Forest", "State": "CA", "Zip": "92630"},
    ]
}

def get_user_location():
    user_address = input("Enter your current address: ")
    user_city = input("Enter your current city: ")
    user_state = input("Enter your current state: ")
    user_zip = input("Enter your current zip code: ")
    return {
        "Address": user_address,
        "City": user_city,
        "State": user_state,
        "Zip": user_zip
    }

def get_emergency_type():
    print("Select an emergency type:")
    print("1. Wildfire/disaster")
    print("2. shelters")
    print("3. hospitals")
    print("4. police_station")
    emergency_choice = input("Enter the number of your choice (or press Enter to skip): ")
    emergency_types = { 
        "1": "wildfire/disaster", 
        "2": "shelters", 
        "3": "hospitals", 
        "4": "police_stations" 
    }
    return emergency_types.get(emergency_choice)

def main():
    addresses = [
        {"Address": "515 E Peltason Dr", "City": "Irvine", "State": "CA", "Zip": "92617"},
        {"Address": "4 Alcott Ct", "City": "Irvine", "State": "CA", "Zip": "92617"},
        {"Address": "16 Joyce Ct", "City": "Irvine", "State": "CA", "Zip": "92617"},
    ]

    enriched_addresses = []
    
    for addr in addresses:
        result = enrich_address(addr)
        if result:
            enriched_addresses.append(result)

    if len(enriched_addresses) < 2:
        print("Not enough valid points to calculate a route.")
        return


    best_route, total_distance = shortest_route(enriched_addresses)
    print(f"\nOptimal Route Found! Total Distance: {total_distance:.2f} mi\n")
    for index, stop in enumerate(best_route):
        print(f" - {chr(65 + index)}. {stop['input']['Address']}")


    emergency_enabled = input("Do you want to enable emergency options? (yes/no): ").strip().lower()
    
    user_location = None
    if emergency_enabled == 'yes':
        user_location = get_user_location()
        enriched_location = enrich_address(user_location)
        
        if not enriched_location:
            print("Could not enrich the current location.")
            return

        emergency_type = get_emergency_type()
        if not emergency_type:
            print("No emergency type selected. Exiting.")
            return

        nearest_safe_location = None
        min_distance = float('inf')

        for safe_location in safe_locations[emergency_type]:
            enriched_safe_location = enrich_address(safe_location)
            if enriched_safe_location:
                distance = distance_between_points(enriched_location, enriched_safe_location)
                if distance < min_distance:
                    min_distance = distance
                    nearest_safe_location = enriched_safe_location

        if nearest_safe_location:
            print(f"Nearest safe location for {emergency_type}: {nearest_safe_location['input']['Address']} ({min_distance:.2f} miles away)")

            route_points = best_route + [enriched_location, nearest_safe_location]
            plot_route(route_points, filename="optimized_route_map.html", emergency_location=nearest_safe_location, user_location=enriched_location)
            print("Updated route map saved to optimized_route_map.html")
        else:
            print("No safe locations found for the selected emergency type.")
    else:
        print("Emergency options not enabled. Exiting.")
        plot_route(best_route, filename="optimized_route_map.html", user_location=user_location)

if __name__ == "__main__":
    main()
