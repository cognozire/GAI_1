import streamlit as st
import geocoder
from twilio.rest import Client

# Twilio credentials
TWILIO_ACCOUNT_SID = 'ACd148fb2af53ec122c15271a7a08cd2d0'
TWILIO_AUTH_TOKEN = '0fb00a9eb0407c11841eb6e0f7a13334'
TWILIO_PHONE_NUMBER = '+12018319411'
EMERGENCY_CONTACTS = ['+917869844761']  # Add your emergency contacts' phone numbers

# Function to get current location using the Geocoder library
def get_location():
    location = geocoder.ip('me')
    return location.latlng if location else None

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

