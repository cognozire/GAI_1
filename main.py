# from twilio.rest import Client
# import streamlit as st
# import pandas as pd
# from datetime import datetime, timedelta
# from tabulate import tabulate

# st.markdown("<h1 style='text-align: center; color: black; font-size: 60px; font-weight: bold;'>Medicine Reminder</h1>", unsafe_allow_html=True)

# page_bg_img = f"""
# <style>
# [data-testid="stAppViewContainer"] > .main {{
# background-image: url("https://www.solidbackgrounds.com/images/2880x1800/2880x1800-light-cyan-solid-color-background.jpg");
# background-size: cover;
# background-position: center;
# background-repeat: no-repeat;
# }}
# [data-testid="stHeader"] {{
# background: rgba(0,0,0,0);
# }}
# </style>
# """
# st.markdown(page_bg_img, unsafe_allow_html=True)

# st.markdown('*Add details about all of your medicines here.*')

# st.write()
# st.write()

# def add_field():
#     st.session_state.fields_size += 1

# def delete_field(index):
#     st.session_state.fields_size -= 1
#     del st.session_state.fields[index]
#     del st.session_state.fields_2[index]
#     del st.session_state.deletes[index]

# if "fields_size" not in st.session_state:
#     st.session_state.fields_size = 0
#     st.session_state.fields = []
#     st.session_state.fields_2 = []
#     st.session_state.deletes = []

# for i in range(st.session_state.fields_size):
#     c1, c2, c3 = st.columns(3)
#     with c1:
#         st.session_state.fields.append(st.text_input(f"Medicine {i+1}", key=f"text{i}"))
#     with c2:
#         st.session_state.fields_2.append(st.text_input(f"Time (H::M)", key=f"text_2{i}"))
#     with c3:
#         st.session_state.deletes.append(st.button("❌", key=f"delete{i}", on_click=delete_field, args=(i,)))

# st.button("➕ Add More", on_click=add_field)

# def get_unique_values_in_order(input_list):
#     seen = set()
#     unique_values = []
    
#     for value in input_list:
#         if value not in seen:
#             seen.add(value)
#             unique_values.append(value)
    
#     return unique_values


# if st.button('Submit'):
#     df = pd.DataFrame({"Medicine": get_unique_values_in_order(st.session_state.fields), "Time": get_unique_values_in_order(st.session_state.fields_2)})
#     df.drop(df.index[0], inplace=True)
#     df.dropna(inplace=True)
#     df.drop_duplicates(inplace=True)

#     def calculate_time_difference(current_time, target_time):
#         current_datetime = datetime.strptime(current_time, "%H::%M")
#         target_datetime = datetime.strptime(target_time, "%H::%M")
#         time_difference = target_datetime - current_datetime
#         return time_difference.total_seconds() / 60  # Convert seconds to minutes

#     current_time = datetime.now().strftime("%H::%M")

#     df['TimeDifference'] = df['Time'].apply(lambda x: calculate_time_difference(current_time, x))

#     next_medicine = df.loc[df['TimeDifference'].abs().idxmin()]

#     if next_medicine['TimeDifference'] > 0:
#         body = f"Your next medicine '{next_medicine['Medicine']}' is due to be taken in {int(next_medicine['TimeDifference'])} minutes."
#     else:
#         try:
#             tomorrow_first_medicine = df.loc[df['TimeDifference'].idxmin() % len(df)]
#             body = f"You are done for your medicines for today. Tomorrow, the first medicine scheduled for you is '{tomorrow_first_medicine['Medicine']}' at {tomorrow_first_medicine['Time']}."
#         except:
#             body = f"You've taken all your medicines for today!"

#     account_sid = 'ACcf8cec3487efd20c185335832108a4e1'
#     auth_token = st.secrets["token"]
#     client = Client(account_sid, auth_token)

#     message = client.messages.create(
#     from_='whatsapp:+14155238886',
#     body="Here's your medicine schedule:\n\n" + tabulate(df.iloc[:,:-1], headers='keys', tablefmt='pretty', showindex=False)+ '\n\n' + body,
#     to='whatsapp:+358417259451'
#     )

#     st.success('Reminder set!')

from twilio.rest import Client
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from tabulate import tabulate

def main():
    st.markdown("<h1 style='text-align: center; color: black; font-size: 60px; font-weight: bold;'>Medicine Reminder</h1>", unsafe_allow_html=True)

    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://www.solidbackgrounds.com/images/2880x1800/2880x1800-light-cyan-solid-color-background.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;A
    }}
    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

    st.markdown('*Add details about all of your medicines here.*')

    st.write()
    st.write()

    def add_field():
        st.session_state.fields_size += 1

    def delete_field(index):
        st.session_state.fields_size -= 1
        del st.session_state.fields[index]
        del st.session_state.fields_2[index]
        del st.session_state.deletes[index]

    if "fields_size" not in st.session_state:
        st.session_state.fields_size = 0
        st.session_state.fields = []
        st.session_state.fields_2 = []
        st.session_state.deletes = []

    for i in range(st.session_state.fields_size):
        c1, c2, c3 = st.columns(3)
        with c1:
            st.session_state.fields.append(st.text_input(f"Medicine {i+1}", key=f"text{i}"))
        with c2:
            st.session_state.fields_2.append(st.text_input(f"Time (H::M)", key=f"text_2{i}"))
        with c3:
            st.session_state.deletes.append(st.button("❌", key=f"delete{i}", on_click=delete_field, args=(i,)))

    st.button("➕ Add More", on_click=add_field)

    def get_unique_values_in_order(input_list):
        seen = set()
        unique_values = []

        for value in input_list:
            if value not in seen:
                seen.add(value)
                unique_values.append(value)

        return unique_values

    if st.button('Submit'):
        df = pd.DataFrame({"Medicine": get_unique_values_in_order(st.session_state.fields), "Time": get_unique_values_in_order(st.session_state.fields_2)})
        df.drop(df.index[0], inplace=True)
        df.dropna(inplace=True)
        df.drop_duplicates(inplace=True)

        def calculate_time_difference(current_time, target_time):
            current_datetime = datetime.strptime(current_time, "%H::%M")
            target_datetime = datetime.strptime(target_time, "%H::%M")
            time_difference = target_datetime - current_datetime
            return time_difference.total_seconds() / 60  # Convert seconds to minutes

        current_time = datetime.now().strftime("%H::%M")

        df['TimeDifference'] = df['Time'].apply(lambda x: calculate_time_difference(current_time, x))

        next_medicine = df.loc[df['TimeDifference'].abs().idxmin()]

        if next_medicine['TimeDifference'] > 0:
            body = f"Your next medicine '{next_medicine['Medicine']}' is due to be taken in {int(next_medicine['TimeDifference'])} minutes."
        else:
            try:
                tomorrow_first_medicine = df.loc[df['TimeDifference'].idxmin() % len(df)]
                body = f"You are done for your medicines for today. Tomorrow, the first medicine scheduled for you is '{tomorrow_first_medicine['Medicine']}' at {tomorrow_first_medicine['Time']}."
            except:
                body = f"You've taken all your medicines for today!"

        account_sid = 'ACcf8cec3487efd20c185335832108a4e1'
        auth_token = st.secrets["token"]  # Ensure that you have set up the secret "token" in your Streamlit sharing settings
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body="Here's your medicine schedule:\n\n" + tabulate(df.iloc[:,:-1], headers='keys', tablefmt='pretty', showindex=False) + '\n\n' + body,
            to='whatsapp:+358417259451'
        )

        st.success('Reminder set!')

if __name__ == "__main__":
    main()

