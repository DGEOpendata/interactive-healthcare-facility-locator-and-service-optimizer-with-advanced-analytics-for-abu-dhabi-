python
import folium
import pandas as pd
import geopy.distance

# Load dataset (assuming CSV format)
data = pd.read_csv('Abu_Dhabi_Healthcare_Facilities.csv')

# Function to calculate distance
def calculate_distance(user_location, facility_location):
    return geopy.distance.distance(user_location, facility_location).km

# Function to find nearest facilities
def find_nearest_facilities(user_lat, user_lon, max_distance):
    user_location = (user_lat, user_lon)
    facilities_within_distance = []

    for index, row in data.iterrows():
        facility_location = (row['latitude'], row['longitude'])
        distance = calculate_distance(user_location, facility_location)
        if distance <= max_distance:
            facilities_within_distance.append({
                'name': row['facility_name'],
                'type': row['facility_type'],
                'services': row['services'],
                'distance': distance,
                'operational_hours': row['operational_hours']
            })
    
    return sorted(facilities_within_distance, key=lambda x: x['distance'])

# Example usage
user_lat = 24.4539  # Example latitude
user_lon = 54.3773  # Example longitude
max_distance = 5  # Search radius in kilometers

nearest_facilities = find_nearest_facilities(user_lat, user_lon, max_distance)

# Create a map to visualize the facilities
map = folium.Map(location=[user_lat, user_lon], zoom_start=12)
folium.Marker([user_lat, user_lon], popup='You are here', icon=folium.Icon(color='blue')).add_to(map)

for facility in nearest_facilities:
    folium.Marker(
        [facility['latitude'], facility['longitude']],
        popup=f"{facility['name']}\n{facility['services']}\n{facility['operational_hours']}",
        icon=folium.Icon(color='green')
    ).add_to(map)

# Save map to HTML
map.save('healthcare_facilities_map.html')
print("Map saved as 'healthcare_facilities_map.html'")
