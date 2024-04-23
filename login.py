# import streamlit as st
# import pandas as pd
# import pygsheets

# if 'session_state' not in st.session_state:
#     st.session_state['session_state'] = {}   
# gc = pygsheets.authorize(service_file='creds.json')
   
# try:
#     sheet = gc.open('Credentials')
# except pygsheets.SpreadsheetNotFound:
#     sheet = gc.create('Credentials')
# wks = sheet.worksheet_by_title("Sheet1")
# # df = wks.get_as_df()
    
# st.title("Login Page")
# all_worksheets = sheet.worksheets()

# # df['Email'] = pd.Series(dtype='str')
# # df['Password'] = pd.Series(dtype='str')
# # print(df)

# st.subheader("Login")
# login_email = st.text_input("Email:")
# login_password = st.text_input("Password:", type="password")

# if st.button("Login"):
#     # print(type(login_password))
#     df = wks.get_as_df()
#     st.write(df)
#     if login_email!='' and login_password!='':
#         if not df[df['Email'] == login_email].empty and not df[df['Password'] == login_password].empty:
#             # st.session_state['session_state']['email'] = login_email
#             # st.session_state['session_state']['password'] = login_password
#             st.success("Login Successful!")
#         else:
#             st.error("Invalid Login. Please try again.")

# st.subheader("New User Registration")
# new_user_option = st.checkbox("New User?")

# if new_user_option:
#     new_email = st.text_input("Enter Email: ")
#     new_password = st.text_input("Enter Password:", type="password")

#     if st.button("Register"):
#        df = wks.get_as_df()     
#        if new_email!='' and new_password!='': 
#                 # wks.set_dataframe(df, start='Email')
#             if df[df['Email'] == new_email].empty and df[df['Password'] == new_password].empty:
#                 st.session_state['session_state']['Email'] = new_email
#                 st.session_state['session_state']['Password'] = new_password
#                 # df.loc[len(df)] = [new_email, new_password]
#                 email = st.session_state['session_state'].get('Email')
#                 password = st.session_state['session_state'].get('Password')
#                 data = {"Email": email,"Password":password}
#                 # df = wks.get_as_df()
#                 df = df._append(data,ignore_index=True)
#                 print("File Saved")
#                 print(df)
#                 st.success("Registration Successful! You can now login.")
#             else:
#                 st.error("User already exists. Try a different email.")
#        else:
#            print("Please enter the details")
#        wks.set_dataframe(df,(1,1))
      



# # if not df.empty:
#     # if (df['A'] == 'foo').any():
#         # print("Found 'foo'")
import streamlit as st
import pandas as pd
import pygsheets

def main_l():
    if 'session_state' not in st.session_state:
        st.session_state['session_state'] = {}   
    gc = pygsheets.authorize(service_file='creds.json')
       
    try:
        sheet = gc.open('GAI')
    except pygsheets.SpreadsheetNotFound:
        sheet = gc.create('GAI')
    wks = sheet.worksheet_by_title("Credentials")
    
    # st.title("Login/ SignUp")
    all_worksheets = sheet.worksheets()
    
    st.title("Login")
    login_email = st.text_input("Email:")
    login_password = st.text_input("Password:", type="password")
    
    if st.button("Login"):
        df = wks.get_as_df()
        # st.write(df)
        if login_email!='' and login_password!='':
            if not df[df['Email'] == login_email].empty and not df[df['Password'] == login_password].empty:
                st.success("Login Successful!")
            else:
                st.error("Invalid Login. Please try again.")
    
    st.title("New User Registration")
    new_user_option = st.checkbox("New User?")
    
    if new_user_option:
        new_email = st.text_input("Enter Email: ")
        new_password = st.text_input("Enter Password:", type="password")
    
        if st.button("Register"):
            df = wks.get_as_df()     
            if new_email!='' and new_password!='': 
                if df[df['Email'] == new_email].empty and df[df['Password'] == new_password].empty:
                    st.session_state['session_state']['Email'] = new_email
                    st.session_state['session_state']['Password'] = new_password
                    email = st.session_state['session_state'].get('Email')
                    password = st.session_state['session_state'].get('Password')
                    data = {"Email": email, "Password": password}
                    df = df._append(data, ignore_index=True)
                    print("File Saved")
                    print(df)
                    st.success("Registration Successful! You can now login.")
                else:
                    st.error("User already exists. Try a different email.")
            else:
                print("Please enter the details")
            wks.set_dataframe(df, (1, 1))

# Invoke the main_l function
if __name__ == "__main__":
   main_l()
