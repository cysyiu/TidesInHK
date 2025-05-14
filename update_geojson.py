import json
import os

# Path to your GeoJSON file
geojson_path = 'tide_stations.geojson'

# Read the GeoJSON
with open(geojson_path, 'r', encoding='utf-8') as f:
    geo_data = json.load(f)

# Update each feature's Data_url property:
for feature in geo_data['features']:
    old_url = feature['properties'].get('Data_url', '')
    # Assuming the original URL ends with "TIDE_x.csv",
    # replace the base URL with your local directory path.
    if old_url.endswith('.csv'):
        # Extract the filename from the URL:
        file_name = os.path.basename(old_url)
        # Set the new path (adjust according to your hosting context)
        feature['properties']['Data_url'] = f"data/{file_name}"

# Write back the updated GeoJSON
with open(geojson_path, 'w', encoding='utf-8') as f:
    json.dump(geo_data, f, indent=2, ensure_ascii=False)

print("GeoJSON updated to use local CSV paths.")
