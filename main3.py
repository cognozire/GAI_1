import streamlit as st
from streamlit_option_menu import option_menu
from notes import notes_main
from enter_data import main_data
from app import nearby_hospi
from visualize_data import track_progress_main
from acne import main_acne
from sayantan import sos_main
from login import main_l

def main():

    PAGE_CONFIG = {"page_title": "Geriatrische KI",
               "page_icon": "icon.png", "layout": "centered"}
    st.set_page_config(**PAGE_CONFIG)
    
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://img.freepik.com/premium-photo/green-background-with-bokeh-rays_582451-37.jpg");
    background-size: cover;
    background-position: top left;
    background-repeat: no-repeat;
    }}
    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    st.sidebar.title("Geriatrische KI")
    menu = ["Anmelden", "Gesundheitsdaten aufzeichnen", "Fortschritt verfolgen", "Nahegelegene Krankenhäuser finden",  "Alarm SOS", "Notizen","Akne-Erkennung"]
    with st.sidebar:
        app_selection = option_menu(
        menu_title=None,
        options=menu,
        # icons=['house', 'bullseye', 'card-checklist', 'emoji-smile', 'journal']
    )
    # app_selection = st.sidebar.radio("Wählen Sie eine Option", ["Daten","Medikamentenerinnerung", "Notizen", "Nahegelegene Krankenhäuser finden", "Fortschritt verfolgen", "Alarm SOS"])

    if app_selection == "Medikamentenerinnerung":
        # main()
        pass
    elif app_selection == "Anmelden":
        main_l()
        
    elif app_selection == "Notizen":
        notes_main()
    elif app_selection == "Nahegelegene Krankenhäuser finden":
        nearby_hospi()
        # pass
    elif app_selection == "Fortschritt verfolgen":
        track_progress_main()
        # pass
    elif app_selection == "Alarm SOS":
        sos_main()
        # pass
    elif app_selection == "Gesundheitsdaten aufzeichnen":
        # pass
        main_data()
    elif app_selection == "Akne-Erkennung":
        main_acne()

if __name__ == "__main__":
    main()
