import requests
import json
import pandas
from pathlib import Path
us_states = {
    'ALABAMA': 'AL',
    'ALASKA': 'AK',
    'ARIZONA': 'AZ',
    'ARKANSAS': 'AR',
    'CALIFORNIA': 'CA',
    'COLORADO': 'CO',
    'CONNECTICUT': 'CT',
    'DELAWARE': 'DE',
    'FLORIDA': 'FL',
    'GEORGIA': 'GA',
    'HAWAII': 'HI',
    'IDAHO': 'ID',
    'ILLINOIS': 'IL',
    'INDIANA': 'IN',
    'IOWA': 'IA',
    'KANSAS': 'KS',
    'KENTUCKY': 'KY',
    'LOUISIANA': 'LA',
    'MAINE': 'ME',
    'MARYLAND': 'MD',
    'MASSACHUSETTS': 'MA',
    'MICHIGAN': 'MI',
    'MINNESOTA': 'MN',
    'MISSISSIPPI': 'MS',
    'MISSOURI': 'MO',
    'MONTANA': 'MT',
    'NEBRASKA': 'NE',
    'NEVADA': 'NV',
    'NEW HAMPSHIRE': 'NH',
    'NEW JERSEY': 'NJ',
    'NEW MEXICO': 'NM',
    'NEW YORK': 'NY',
    'NORTH CAROLINA': 'NC',
    'NORTH DAKOTA': 'ND',
    'OHIO': 'OH',
    'OKLAHOMA': 'OK',
    'OREGON': 'OR',
    'PENNSYLVANIA': 'PA',
    'RHODE ISLAND': 'RI',
    'SOUTH CAROLINA': 'SC',
    'SOUTH DAKOTA': 'SD',
    'TENNESSEE': 'TN',
    'TEXAS': 'TX',
    'UTAH': 'UT',
    'VERMONT': 'VT',
    'VIRGINIA': 'VA',
    'WASHINGTON': 'WA',
    'WEST VIRGINIA': 'WV',
    'WISCONSIN': 'WI',
    'WYOMING': 'WY'
}

# Example usage:


#ip_address = requests.get('http://api.ipify.org').text
#geo_data = requests.get(f'http://api.ipstack.com/{ip_address}?access_key=c7941656ee9e082bd1666d35d494caa3').json()
#print(geo_data)
#lat = geo_data['latitude']
#long = geo_data['longitude']
#print(lat, long)
#response = requests.get(f'https://api.weather.gov/alerts?point={44.040950775146484},{-122.95088958740234}').json()

#features = response.get('features', [])

'''

#data = []

# Loop through each feature and extract relevant properties (e.g., 'areaDesc')
#for feature in features:
    properties = feature.get('properties', {})
    area_desc = properties.get('areaDesc', 'N/A')  # Default to 'N/A' if 'areaDesc' doesn't exist
    headline = properties.get('headline', 'N/A')
    severity = properties.get('severity', 'N/A')
    event = properties.get('event', 'N/A')
    
    # Add this data as a new row to the list
    data.append({
        'areaDesc': area_desc,
        'headline': headline,
        'severity': severity,
        'event': event
    })
'''
# Convert the list of dictionaries to a pandas DataFrame
#df = pandas.DataFrame(data)

# Display the DataFrame
#print(df)


def load_csv_with_header(file_path):
    """
    This function loads a CSV file and treats the first line as the header.
    
    Parameters:
        file_path (str): Path to the CSV file.
    
    Returns:
        pd.DataFrame: The loaded DataFrame with the first row as header.
    """
    # Load the CSV and treat the first line as the header
    df = pandas.read_csv(file_path, header=0)  # 'header=0' tells pandas to use the first line as header
    
    return df

# Example usage
csv_file_path = Path("cityData.csv")
df = load_csv_with_header(csv_file_path)
def get_shorthand(state_str):
    state_str = state_str.upper()
    shorthand = us_states[state_str]
    return shorthand

def cities_in_states(shorthand):
    list = []
    for index, row in df.iterrows():
        rowDict=row.to_dict()
        if rowDict['abbr'] == shorthand:
            citiesInState = (row.to_dict()['city'])
            if citiesInState not in list:
                list.append(citiesInState)
    return list
    #if x['abbr'] == "OR":
        #print(x)
# Display the DataFrame
#print(df['stateID'])
