# import streamlit as st
# import pandas as pd
# import plotly.express as px
# # Function to save entered data to a CSV file
# def save_data_to_csv(data):
#     data.to_csv('health_data.csv', index=False)
# # Function to load data from CSV file
# def load_data_from_csv():
#     try:
#         data = pd.read_csv('health_data.csv')
#     except FileNotFoundError:
#         data = pd.DataFrame(columns=['Date', 'Sleep Hours', 'Weight', 'Blood Pressure', 'Sugar Level'])
#     return data
# # Function to plot graphs
# def plot_graphs(data):
#     fig_sleep = px.line(data, x='Date', y='Sleep Hours', title='Sleep Hours Over Time')
#     fig_weight = px.line(data, x='Date', y='Weight', title='Weight Over Time')
#     fig_blood_pressure = px.line(data, x='Date', y='Blood Pressure', title='Blood Pressure Over Time')
#     fig_sugar_level = px.line(data, x='Date', y='Sugar Level', title='Sugar Level Over Time')
#     return fig_sleep, fig_weight, fig_blood_pressure, fig_sugar_level
# # Streamlit app
# st.set_page_config(page_title="Health Vitals Tracker", layout="wide")
# # Page 1: Form to enter health vitals
# st.title("Page 1: Enter Health Vitals")
# date = st.date_input("Date", pd.to_datetime('today'))
# sleep_hours = st.number_input("Sleep Hours", min_value=0.0, max_value=24.0, step=0.5, value=8.0)
# weight = st.number_input("Weight (kg)", min_value=0.0, max_value=300.0, step=0.1, value=70.0)
# blood_pressure = st.number_input("Blood Pressure (mmHg)", min_value=0, max_value=300, step=1, value=120)
# sugar_level = st.number_input("Sugar Level (mg/dL)", min_value=0, max_value=1000, step=1, value=90)
# if st.button("Submit"):
#     data_entry = {'Date': date, 'Sleep Hours': sleep_hours, 'Weight': weight,
#                   'Blood Pressure': blood_pressure, 'Sugar Level': sugar_level}
#     df = load_data_from_csv()
#     df = pd.concat([df, pd.DataFrame([data_entry])], ignore_index=True)
#     save_data_to_csv(df)
#     st.success("Data submitted successfully!")
# # Page 2: Display graphs
# st.title("Page 2: View Health Vitals Graphs")
# data = load_data_from_csv()
# if not data.empty:
#     fig_sleep, fig_weight, fig_blood_pressure, fig_sugar_level = plot_graphs(data)
#     col1, col2 = st.beta_columns(2)
#     with col1:
#         st.plotly_chart(fig_sleep)
#         st.plotly_chart(fig_blood_pressure)
#     with col2:
#         st.plotly_chart(fig_weight)
#         st.plotly_chart(fig_sugar_level)
# else:
#     st.warning("No data available. Please enter health vitals on Page 1.")


import streamlit as st
import geocoder
from twilio.rest import Client
from streamlit_js_eval import streamlit_js_eval, copy_to_clipboard, create_share_link, get_geolocation

# Twilio credentials
TWILIO_ACCOUNT_SID = 'ACfb09735781fc39700a6def11ae615bfa'
TWILIO_AUTH_TOKEN = st.secrets["db_password"]
TWILIO_PHONE_NUMBER = '+15203574586'
EMERGENCY_CONTACTS = ['+917869844761']  # Add your emergency contacts' phone numbers

# Function to get current location using the Geocoder library
def get_location():
    loc = get_geolocation()
    loc1 = loc['coords']
    location = geocoder.ip('me')
    return loc1['latitude'], loc1['longitude'] if loc1 else None

# Function to send SMS notifications using Twilio
def send_sms(message, to):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    try:
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=to
        )
        st.success(f"SMS sent to {to}")
    except Exception as e:
        st.error(f"Failed to send SMS. Error: {e}")

def sos_main():
    # Streamlit app
    st.title("Emergency Location Sharing App")

    # Get current location
    current_location = get_location()

    if current_location:
        st.write(f"Current Location: {current_location}")

        # Button to share location with emergency contacts
        if st.button("Share Location with Emergency Contacts"):
            message = f"Emergency! I need your help. My current location is {current_location}. Please reach me ASAP."
            
            # Send SMS to each emergency contact
            for contact in EMERGENCY_CONTACTS:
                send_sms(message, contact)
    else:
        st.error("Unable to retrieve current location. Please check your internet connection.")

if __name__ == "__main__":
    sos_main()
