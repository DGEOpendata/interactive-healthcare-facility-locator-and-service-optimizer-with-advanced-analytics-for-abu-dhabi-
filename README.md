### Interactive Healthcare Facility Locator and Service Optimizer

#### Overview
This project implements an interactive platform that uses a dataset of healthcare facilities in Abu Dhabi to provide insights and tools for residents, healthcare professionals, and policymakers.

#### Features
1. **Interactive Map Visualization:** Displays all healthcare facilities in Abu Dhabi.
2. **Service Search Tool:** Allows users to search for specific healthcare services.
3. **Proximity Search:** Identifies healthcare facilities within a specified radius of a user's location.
4. **Analytics Dashboard:** Provides policymakers with insights into healthcare facility distribution and service accessibility.
5. **Emergency Locator:** Displays the nearest emergency-ready facility and the quickest route.
6. **Multilingual Support:** Available in both English and Arabic.

#### Prerequisites
1. Python 3.x installed on your local machine.
2. Install the required Python libraries using pip:
    bash
    pip install pandas folium geopy
    
3. Download the dataset (e.g., "Abu_Dhabi_Healthcare_Facilities.csv") and save it in the project directory.

#### How to Use
1. Clone the repository:
    bash
    git clone https://github.com/your-repository/healthcare-locator
    cd healthcare-locator
    
2. Place the dataset file ("Abu_Dhabi_Healthcare_Facilities.csv") in the project directory.
3. Open and edit the Python script to set your desired location (latitude and longitude) and search radius.
4. Run the script:
    bash
    python healthcare_locator.py
    
5. Open the generated HTML file ("healthcare_facilities_map.html") in your web browser to view the map.

#### Dataset Structure
The dataset should include the following columns:
- **facility_name:** Name of the healthcare facility.
- **facility_type:** Type of the facility (e.g., hospital, clinic).
- **latitude:** Latitude coordinate.
- **longitude:** Longitude coordinate.
- **services:** List of services offered at the facility.
- **operational_hours:** Operating hours of the facility.

#### Example
Suppose you are located at latitude 24.4539 and longitude 54.3773, and you want to find healthcare facilities within a 5 km radius:

1. Set the variables in the script:
    python
    user_lat = 24.4539
    user_lon = 54.3773
    max_distance = 5
    
2. Run the script:
    bash
    python healthcare_locator.py
    
3. Open the generated map ("healthcare_facilities_map.html") in your browser to see the results.

#### Contribution
Feel free to contribute to this project by submitting issues or pull requests on the [GitHub repository](https://github.com/your-repository/healthcare-locator).

#### License
This project is licensed under the MIT License. See the LICENSE file for details.