**Note: Created by Rutu Aarabhi Kuchi and Bruhati Aarushi Kuchi
# RapidRoute

# Emergency Route Optimizer

## Overview

The Emergency Route Optimizer is a Python-based application designed to help users find the optimal route to various emergency locations (such as shelters, hospitals, and police stations) based on their current location. The application enriches address data using the Personator API to obtain geolocation information and calculates the shortest route to visit predefined addresses while considering emergency options.

## Features

- **User  Input**: Users can input their current address and select an emergency type.
- **Address Enrichment**: The application enriches both predefined and user-provided addresses with geolocation data using the Personator API.
- **Route Optimization**: Calculates the shortest route to visit all predefined addresses and return to the starting point.
- **Emergency Handling**: Finds the nearest safe location based on the selected emergency type and the user's current location.
- **Map Visualization**: Generates an HTML file displaying the optimized route and emergency locations on an interactive map using Folium.

## Technologies Used
- **Programming Language**: Python
- **APIs**: 
  - Melissa Personator API for address verification and enrichment
- **Libraries**:
  - Requests for making HTTP requests
  - Folium for creating interactive maps
- **Mathematical Functions**: Custom distance calculation using spherical geometry
