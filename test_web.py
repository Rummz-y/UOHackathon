import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import ui



#some random data
data = {
    "month" : ["Jan","Feb","Mar","Apr","May","Jun","Jul"
               ,"Aug","Sep","Oct","Nov","Dec"],
    
    "temp" : [1,4,5,10,15,23,32,33,25,16,5,-3]
}

#list of states + DC
us_states_and_dc = [
    'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 
    'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 
    'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 
    'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 
    'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 
    'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 
    'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 
    'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 
    'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 
    'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'District of Columbia'
]


def main():
    test_df = pd.DataFrame(data) #data in the chart atm

    map_point_data = pd.DataFrame({ #map data
        'lon' : [-77.0369, -123.0867, -118.2436],
        'lat' : [38.9072, 44.0521, 34.0522],
        'name' : ['Washington', 'Eugene', 'Los Angeles']
    }, dtype=str)

    st.header("Welcome to our Weather App!")
    state = st.selectbox("Enter a state", us_states_and_dc)
    city = st.selectbox("Enter a city:", ui.cities_in_states(ui.get_shorthand(state.upper())))



    st.write(f"The city you chose is {city}, {state}")

    #defines the map
    home_map = folium.Map(location=[38,-96.5], zoom_start=4, 
                   scrollWheelZoom = True)
    
    #adds fire marker
    folium.Marker(location = [40, -100], 
                  icon=folium.Icon(color='red',
                                   icon='fire',
                                   prefix='fa')
                  ).add_to(home_map)
    
    #adds markers
    for i in range(0,len(map_point_data)): 
        folium.Marker(
            location = [map_point_data.iloc[i]['lat'],
                        map_point_data.iloc[i]['lon']],

            popup = map_point_data.iloc[i]['name'],
            
        ).add_to(home_map)
    
    st_folium(home_map, width=700, height=450) #displays map

    st.bar_chart(test_df, x="month", y="temp") #displays graph



if __name__ == "__main__":
    main()