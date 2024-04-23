import streamlit as st
from streamlit_js_eval import streamlit_js_eval, copy_to_clipboard, create_share_link, get_geolocation
import json
import math
import pandas as pd
from geopy.geocoders import Nominatim

def nearby_hospi():
    st.title('Find Hospitals Near You')
    if st.checkbox("Get my  location"):
        geoLoc = Nominatim(user_agent="GetLoc")
        df = pd.read_csv("hospital_directory.csv")
        loc = get_geolocation()
        print(type(loc["coords"]))
        loc1 = loc['coords']
        print(loc1.keys())
        print(loc1['latitude'])
        print(loc1['longitude'])
        locname = geoLoc.reverse(f"{loc1['latitude']}, {loc1['longitude']}")
        st.write(f"Your coordinates are {loc1['latitude']},{loc1['longitude']}")
        st.write(f"You are at {locname.address}")

        longitude =  float(loc1['longitude'])
        latitude =float(loc1['latitude'])

        distances = []
        time = []
        student_x =latitude
        student_y = longitude
        i = 0
        for value in df['Location_Coordinates']:
    
            R = 6371.0
            try:
                tutor_x, tutor_y = map(str, value.split(','))
        
                tutor_x, tutor_y = float(tutor_x), float(tutor_y)    
            
                lat1_rad = math.radians(student_x)
                lon1_rad = math.radians(student_y)
                lat2_rad = math.radians(tutor_x)
                lon2_rad = math.radians(tutor_y)
        
                dlat = abs(lat2_rad - lat1_rad)
                dlon = abs(lon2_rad - lon1_rad)
            
                a = math.sin(dlat / 2)*2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)*2
                c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
                distance = R * c
        
            # distance = math.sqrt((tutor_x - student_x)*2 + (tutor_y - student_y)*2)
        
                distances.append(distance)
                speed = 50
                # time = round(distance/speed, 2)
                time.append(round(distance/speed, 2))
                i = i+1
            
            except:
                pass
                distances.append(a)
                time.append(i)
                i = i+1
    
        cord = df["Location_Coordinates"].values
        loca = df["Location"].values
        hos = df['Hospital_Name'].values
        sta = df["State"].values
        dis = df["District"].values
        print(len(df['Hospital_Name']))
        print(len(df['State']))
        print(len(distances))
        print(len(time))
        print(len(dis))
        print(len(loca))
        result_df = pd.DataFrame({
            'Hospital_Name': df['Hospital_Name'],
            'State': df['State'],
            'Distance': distances,
            'Time(hrs)': time,
            'District':dis,
            'Address': loca
    })
    
        top_5_hospitals = result_df.nsmallest(5, 'Distance')

        if st.button("Get Nearby Hospitals"):
            st.write(top_5_hospitals)

if __name__ == "__main__":
   nearby_hospi()

