import pyproj
import what3words

def grid_ref_to_lat_lon(grid_ref):
    # Create a Transverse Mercator projection instance
    proj = pyproj.TransverseMercator()

    # Extract the grid reference components (easting and northing)
    easting = float(grid_ref[:4])
    northing = float(grid_ref[4:])

    # Convert the grid reference to latitude and longitude
    lon, lat = proj(easting, northing, inverse=True)

    return lat, lon

def lat_lon_to_what3words(lat, lon):
    api = what3words.Geocoder("YOUR_API_KEY")
    try:
        result = api.convert_to_3wa(lat=lat, lng=lon)
        return result["words"]
    except what3words.GeocoderError as e:
        print(f"Error: {e}")

# Example usage
grid_ref = "SU387148"
lat, lon = grid_ref_to_lat_lon(grid_ref)
what3words_address = lat_lon_to_what3words(lat, lon)
print(f"What3words address: {what3words_address}")
