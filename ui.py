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


def load_csv_with_header(file_path):
    """
    This function loads a CSV file and treats the first line as the header.
    
    Parameters:
        file_path (str): Path to the CSV file.
    
    Returns:
        pd.DataFrame: The loaded DataFrame with the first row as header.
    """
    df = pandas.read_csv(file_path, header=0)
    
    return df

csv_file_path = "/Users/benelster/Documents/Hackathon fall 2024/UOHackathon/UOHackathon/cityData.csv"
df = load_csv_with_header(csv_file_path)
def get_shorthand(state_str):
    state_str = state_str.upper()
    shorthand = us_states[state_str]
    return shorthand

def get_zoneID(county):
    list = []
    for index, row in df.iterrows():
        rowDict=row.to_dict()
        if rowDict['city'] == county:
            citiesInState = (rowDict['stateID'])
            return citiesInState

def cities_in_states(shorthand):
    list = []
    for index, row in df.iterrows():
        rowDict=row.to_dict()
        if rowDict['abbr'] == shorthand:
            citiesInState = (row.to_dict()['city'])
            if citiesInState not in list:
                list.append(citiesInState)
    return list

def get_cords(city, state):
   list = []
   for index, row in df.iterrows():
       rowDict=row.to_dict()
       state_code = get_shorthand(state)
       if rowDict['city'] == city and rowDict['abbr'] == state_code:
           if state_code == 'AK' or state_code == 'HI':
               list.append(row.to_dict()['dir'])
               list.append(row.to_dict()['lat'])
           else:
               list.append(row.to_dict()['lat'])
               list.append(row.to_dict()['long'])

           return list 

def get_forecast(city_cords):
    response = requests.get(f'https://api.weather.gov/points/{city_cords[0]},{city_cords[1]}')
    data = response.json()
    forecast_urls = data['properties']['forecast']
    forecast_res = requests.get(forecast_urls)

    forecast_data = forecast_res.json()

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


def get_alerts(zoneID):
    zoneId_let = zoneID[:2]
    zoneId_num = zoneID[-3:]

    modified_zoneID = zoneId_let + "Z" + zoneId_num
    
    response = requests.get(f'https://api.weather.gov/alerts/active/zone/{modified_zoneID}')
    data = response.json()
    if data['features'] == []:
        return "No active alerts in county"
    else:
        for x in data['features']:
            return x['properties']['description']




