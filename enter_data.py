# import streamlit as st
# import pygsheets
# import pandas as pd

# gc = pygsheets.authorize(service_file='creds.json')

# sh = gc.open('GAI')

# existing_worksheets = []

# st.title('Health Data Recorder')

# # entering the data
# user_name = st.text_input('Enter your name: ')
# sleep_hrs = st.text_input('Enter total sleep hours: ')
# weight = st.text_input('Enter weight: ')
# bp = st.text_input('Enter blood pressure: ')
# sugar_level = st.text_input('Enter sugar level: ')

# new_data = {'Sleep Hours': sleep_hrs,
#                     'Weight': weight,
#                     'Blood Pressure': bp,
#                     'Sugar Level': sugar_level}

# data = {'Sleep Hours': [sleep_hrs],
#                     'Weight': [weight],
#                     'Blood Pressure': [bp],
#                     'Sugar Level': [sugar_level]}

# all_worksheets = sh.worksheets()

# for worksheet in all_worksheets:
#     existing_worksheets.append(worksheet.title)

# if st.button('Submit'):

#     if user_name!= '' and sleep_hrs!= '' and weight!= '' and bp!= '' and sugar_level!= '':

#         if user_name in existing_worksheets:
#             wks = sh.worksheet_by_title(user_name)
#             df_fetched = wks.get_as_df()
#             df = df_fetched.append(new_data, ignore_index=True)

#         else:
#             new_worksheet = sh.add_worksheet(title=user_name, rows=100, cols=20)
#             columns = ['Sleep Hours', 'Weight', 'Blood Pressure', 'Sugar Level']
#             df = pd.DataFrame(data, columns=columns)
#             wks = sh.worksheet_by_title(user_name)
            
#         wks.set_dataframe(df,(1,1))
#         st.success('Data saved!')

#     else:
#         st.warning('Enter all values.')


import streamlit as st
import pygsheets
import pandas as pd

# Setup session state
st.session_state['session_state'] = {}
if 'session_state' not in st.session_state:
    st.session_state['session_state'] = {}

def main_data():
    gc = pygsheets.authorize(service_file='creds.json')

    sh = gc.open('GAI')

    existing_worksheets = []

    st.title('Health Data Recorder')

    # entering the data
    user_name = st.text_input('Enter your name: ')
    sleep_hrs = st.text_input('Enter total sleep hours: ')
    weight = st.text_input('Enter weight: ')
    bp = st.text_input('Enter blood pressure: ')
    sugar_level = st.text_input('Enter sugar level: ')

    new_data = {'Sleep Hours': sleep_hrs,
                'Weight': weight,
                'Blood Pressure': bp,
                'Sugar Level': sugar_level}

    data = {'Sleep Hours': [sleep_hrs],
            'Weight': [weight],
            'Blood Pressure': [bp],
            'Sugar Level': [sugar_level]}

    all_worksheets = sh.worksheets()

    for worksheet in all_worksheets:
        existing_worksheets.append(worksheet.title)

    if st.button('Submit'):
        if user_name != '' and sleep_hrs != '' and weight != '' and bp != '' and sugar_level != '':
            if user_name in existing_worksheets:
                wks = sh.worksheet_by_title(user_name)
                df_fetched = wks.get_as_df()
                df = df_fetched._append(new_data, ignore_index=True)
            else:
                new_worksheet = sh.add_worksheet(title=user_name, rows=100, cols=20)
                columns = ['Sleep Hours', 'Weight', 'Blood Pressure', 'Sugar Level']
                df = pd.DataFrame(data, columns=columns)
                wks = sh.worksheet_by_title(user_name)

            wks.set_dataframe(df, (1, 1))
            st.success('Data saved!')

            # Store data in session_state
            st.session_state['user_name'] = user_name
            st.session_state['sleep_hrs'] = sleep_hrs
            st.session_state['weight'] = weight
            st.session_state['bp'] = bp
            st.session_state['sugar_level'] = sugar_level

        else:
            st.warning('Enter all values.')

# Access stored data in session_state
if 'session_state' in st.session_state:
    user_name = st.session_state['session_state'].get('user_name','')
    sleep_hrs = st.session_state['session_state'].get('sleep_hrs','')
    weight = st.session_state['session_state'].get('weight','')
    bp = st.session_state['session_state'].get('bp','')
    sugar_level = st.session_state['session_state'].get('sugar_level','')
    st.write(f"Stored Data: {user_name}, {sleep_hrs}, {weight}, {bp}, {sugar_level}")


if __name__ == "__main__":
    main_data()
