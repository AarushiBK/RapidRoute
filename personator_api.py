import requests
import urllib.parse
import json
import os

BASE_URL = "https://personator.melissadata.net/v3/WEB/ContactVerify/doContactVerify"
LICENSE = "FNBofqXaFm0Cmwp4qOJ1C-**nSAcwXpxhQ0PC2lXxuDAZ-**"  # Use environment variable for license


def enrich_address(address_dict):
    params = {
        "id": LICENSE,
        "act": "Check",
        "a1": address_dict["Address"],
        "city": address_dict["City"],
        "state": address_dict["State"],
        "postal": address_dict["Zip"],
        "ctry": "US",
        "format": "json",
        "cols": "GrpGeocode"
    }

    url = f"{BASE_URL}?{urllib.parse.urlencode(params)}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()

        # Check if there are any valid records
        record = data.get("Records", [{}])[0]
        
        # Fetch latitude and longitude
        lat = record.get("Latitude", None)
        lon = record.get("Longitude", None)

        if lat is None or lon is None:
            print(f"Warning: No geolocation found for {address_dict['Address']}")

        return {
            "input": address_dict,
            "mak": record.get("MelissaAddressKey", ""),
            "type": record.get("AddressType", ""),
            "lat": float(lat),
            "lon": float(lon)
        }

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except Exception as e:
        print(f"Error processing address: {address_dict}")
        print(e)
        return None