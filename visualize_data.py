# import streamlit as st
# import pygsheets
# import plotly.express as px

# gc = pygsheets.authorize(service_file='creds.json')

# sh = gc.open('GAI')

# existing_worksheets = []

# st.title('Health Dashboard')

# user_name = st.text_input('Enter your name: ')

# if st.button('Submit'):
#     all_worksheets = sh.worksheets()

#     for worksheet in all_worksheets:
#         existing_worksheets.append(worksheet.title)

#     if user_name in existing_worksheets:
#         wks = sh.worksheet_by_title(user_name)
#         df = wks.get_as_df()

#         # Scatter Plot
#         scatter_fig = px.scatter(df, x='Sleep Hours', y='Weight', title='Sleep Hours vs Weight')

#         # Bar Chart
#         bar_fig = px.bar(df, x='Sleep Hours', y='Blood Pressure', title='Blood Pressure by Sleep Hours')

#         # Box Plot
#         box_fig = px.box(df, x='Sleep Hours', y='Sugar Level', title='Sugar Level by Sleep Hours')

#         # 3D Scatter Plot
#         scatter_3d_fig = px.scatter_3d(df, x='Sleep Hours', y='Weight', z='Blood Pressure', title='Sleep Hours vs Weight vs Blood Pressure')

#         # Display plots in Streamlit app
#         st.title('Health progress for ' + user_name)

#         # Scatter Plot
#         st.plotly_chart(scatter_fig)

#         # Bar Chart
#         st.plotly_chart(bar_fig)

#         # Box Plot
#         st.plotly_chart(box_fig)

#         # 3D Scatter Plot
#         st.plotly_chart(scatter_3d_fig)

#     else:
#         st.warning('No entry found for you.')


import streamlit as st
import pygsheets
import plotly.express as px

def track_progress_main():
    gc = pygsheets.authorize(service_file='creds.json')

    sh = gc.open('GAI')

    existing_worksheets = []

    st.title('Health Dashboard')

    user_name = st.text_input('Enter your name: ')

    if st.button('Submit'):
        all_worksheets = sh.worksheets()

        for worksheet in all_worksheets:
            existing_worksheets.append(worksheet.title)

        if user_name in existing_worksheets:
            wks = sh.worksheet_by_title(user_name)
            df = wks.get_as_df()

            # Scatter Plot
            scatter_fig = px.scatter(df, x='Sleep Hours', y='Weight', title='Sleep Hours vs Weight')

            # Bar Chart
            bar_fig = px.bar(df, x='Sleep Hours', y='Blood Pressure', title='Blood Pressure by Sleep Hours')

            # Box Plot
            box_fig = px.box(df, x='Sleep Hours', y='Sugar Level', title='Sugar Level by Sleep Hours')

            # 3D Scatter Plot
            scatter_3d_fig = px.scatter_3d(df, x='Sleep Hours', y='Weight', z='Blood Pressure', title='Sleep Hours vs Weight vs Blood Pressure')

            # Display plots in Streamlit app
            st.title('Health progress for ' + user_name)

            # Scatter Plot
            st.plotly_chart(scatter_fig)

            # Bar Chart
            st.plotly_chart(bar_fig)

            # Box Plot
            st.plotly_chart(box_fig)

            # 3D Scatter Plot
            st.plotly_chart(scatter_3d_fig)

        else:
            st.warning('No entry found for you.')

if __name__ == "__main__":
    track_progress_main()
