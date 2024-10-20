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

    st.header("Welcome to our Weather App!")

    #gets city and state from user
    state = st.selectbox("Enter a state", us_states_and_dc)
    county = st.selectbox("Enter a county:", ui.cities_in_states(ui.get_shorthand(state.upper())))

    st.write(f"The county you chose is {county}, {state}")

    draw_map(state, county)#renders map

    cords = ui.get_cords(county, state)
    draw_today_data(cords)

def draw_map(state, county):

    #adjust zoom for lower 48, Alaska, Hawaii
    if(state == "Alaska"):
        location_cord = [63.5888, -154.4931]
        zoom = 3.2
    elif(state == "Hawaii"):
        location_cord = [20.7417, -157.7444]
        zoom = 7
    else:
        location_cord = [38,-96.5]
        zoom = 4

    #defines the map
    home_map = folium.Map(location_cord, zoom_start=zoom, 
                   scrollWheelZoom = True)
    
    #adds fire marker
    folium.Marker(location = [40, -100], 
                  icon=folium.Icon(color='red',
                                   icon='fire',
                                   prefix='fa')
                  ).add_to(home_map)
    
    #adds ping on county
    folium.Marker(
        location = ui.get_cords(county, state),
        popup = f"{county}, {state}"      
    ).add_to(home_map)
    
    st_folium(home_map, width=700, height=450) #displays map

def draw_today_data(cords):
    w_data = ui.get_forecast(cords)

    col1, col2, col3 = st.columns(3, gap="small", vertical_alignment="top")

    st.metric("Forecast", w_data[2])

    with col1:
        st.metric("Temperature", f"{w_data[1]}°F")
    with col2:
        st.metric("Percipitation", f"{w_data[3]}%")
    with col3:
        st.metric("Wind Speed", w_data[4])
    

if __name__ == "__main__":
    main()