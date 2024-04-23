# import streamlit as st
# import subprocess

# # Funktio valitun Python-skriptin suorittamiseen
# def execute_script(script_name):
#     subprocess.run(["streamlit", "run", script_name])

# # Streamlit App
# st.title("Geriatrinen tekoäly")

# selected_option = st.sidebar.radio("Valitse vaihtoehto", [
#     "Lääkemuistutin",
#     "Muistiinpanot",
#     "Paikanna läheiset sairaalat",
#     "Hätä-SOS",
#     "Seuraa edistymistä"
# ])

# options_to_scripts = {
#     "Lääkemuistutin": "main.py",
#     "Muistiinpanot": "notes.py",
#     "Paikanna läheiset sairaalat": "app.py",
#     "Hätä-SOS": "main_s.py",
#     "Seuraa edistymistä": "visualize_data.py"
# }

# # Suorita valittu skripti
# if selected_option in options_to_scripts:
#     script_name = options_to_scripts[selected_option]
#     execute_script(script_name)
# else:
#     st.error("Virheellinen vaihtoehto valittu.")

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

    PAGE_CONFIG = {"page_title": "Geriatrinen tekoäly",
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
    
    st.sidebar.title("Geriatrinen tekoäly")
    menu = ["Kirjaudu", "Tallenna terveystiedot", "Seuraa edistymistä", "Paikanna läheiset sairaalat",  "Hätä-SOS", "Muistiinpanot","Aknen havaitseminen"]
    with st.sidebar:
        app_selection = option_menu(
        menu_title=None,
        options=menu,
        # icons=['house', 'bullseye', 'card-checklist', 'emoji-smile', 'journal']
    )
    # app_selection = st.sidebar.radio("Valitse vaihtoehto", ["Tieto","Lääkeruutu", "Muistiinpanot", "Paikanna läheiset sairaalat", "Seuraa edistymistä", "Hälytä SOS"])

    if app_selection == "Lääkeruutu":
        # main()
        pass
    elif app_selection == "Kirjaudu":
        main_l()
        
    elif app_selection == "Muistiinpanot":
        notes_main()
    elif app_selection == "Paikanna läheiset sairaalat":
        nearby_hospi()
        # pass
    elif app_selection == "Seuraa edistymistä":
        track_progress_main()
        # pass
    elif app_selection == "Hätä-SOS":
        sos_main()
        # pass
    elif app_selection == "Tallenna terveystiedot":
        # pass
        main_data()
    elif app_selection == "Aknen havaitseminen":
        main_acne()

if __name__ == "__main__":
    main()
