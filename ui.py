from pathlib import Path
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
<<<<<<< HEAD
csv_file_path = "/Users/benelster/Documents/Hackathon fall 2024/UOHackathon/UOHackathon/cityData.csv"
=======
csv_file_path = Path("cityData.csv")
>>>>>>> ff376a21bcaaeeaef6fba457ed5df0e2ca911643
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
<<<<<<< HEAD

def get_cords(city):
    list = []
    for index, row in df.iterrows():
        rowDict=row.to_dict()
        if rowDict['city'] == city:
            list.append(row.to_dict()['lat'])
            list.append(row.to_dict()['long'])
            return list
  


#print(get_cords('Coconino'))
def get_forecast(city_cords):
    response = requests.get(f'https://api.weather.gov/points/{city_cords[0]},{city_cords[1]}')
    data = response.json()
    forecast_urls = data['properties']['forecast']
    forecast_res = requests.get(forecast_urls)

    # Convert the forecast response to JSON
    forecast_data = forecast_res.json()

    # Access the forecast periods
    periods = forecast_data['properties']['periods']
    for period in periods:
        nameVar = period['name']
        tempVar = period['temperature']
        castVar = period['shortForecast']
        prepVar = period['probabilityOfPrecipitation'].get('value', 'N/A')
        windVar = period['windSpeed']
        if prepVar == None:
            print(f'{nameVar}, {tempVar}F, {castVar}, 0%, {windVar}')
        else:
            print(f'{nameVar}, {tempVar}F, {castVar}, {prepVar}%, {windVar}')

def main():
    # Example location - you can replace 'Coconino' with any valid location name
    location = 'Coconino'
    
    # Get coordinates based on location
    results = get_cords(location)

    
    # Fetch the weather forecast data
    forecast_data = get_forecast(results)
    
    # Print the forecast data
    

# Entry point of the script
if __name__ == '__main__':
    main()



=======
    #if x['abbr'] == "OR":
        #print(x)
# Display the DataFrame
#print(df['stateID'])

def get_cords(city, state):
   list = []
   for index, row in df.iterrows():
       rowDict=row.to_dict()
       state_code = get_shorthand(state)
       if rowDict['city'] == city and rowDict['abbr'] == state_code:
           if state_code == 'AK' or state_code == 'HI':
               #data set is inconsistent with HI and AK so must adjust
               list.append(row.to_dict()['dir'])
               list.append(row.to_dict()['lat'])
           else:
               #else add lat, long normally
               list.append(row.to_dict()['lat'])
               list.append(row.to_dict()['long'])

           return list
>>>>>>> ff376a21bcaaeeaef6fba457ed5df0e2ca911643
