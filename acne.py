from utils import get_detection_folder, check_folders
import redirect as rd
from pathlib import Path
import streamlit as st
from PIL import Image
import subprocess
import os
import torch

# Setup session state
if 'session_state' not in st.session_state:
    st.session_state['session_state'] = {}

def main_acne():
    # This will check if we have all the folders to save our files for inference
    check_folders()

    st.title('Acne Detection App')

    source = ("Image", "Video")
    source_index = st.sidebar.selectbox("Select Input type", range(len(source)), format_func=lambda x: source[x])

    if source_index == 0:
        uploaded_file = st.sidebar.file_uploader("Load File", type=['png', 'jpeg', 'jpg'])
        if uploaded_file is not None:
            is_valid = True
            with st.spinner(text='Loading...'):
                st.sidebar.image(uploaded_file)
                picture = Image.open(uploaded_file)
                picture = picture.save(f'data/images/{uploaded_file.name}')
                source = f'data/images/{uploaded_file.name}'
        else:
            is_valid = False
    else:
        uploaded_file = st.sidebar.file_uploader("Upload Video", type=['mp4'])
        if uploaded_file is not None:
            is_valid = True
            with st.spinner(text='Loading...'):
                st.sidebar.video(uploaded_file)
                with open(os.path.join("data", "videos", uploaded_file.name), "wb") as f:
                    f.write(uploaded_file.getbuffer())
                source = f'data/videos/{uploaded_file.name}'
        else:
            is_valid = False

    if is_valid:
        if st.button('Detect'):
            with rd.stderr(format='markdown', to=st.sidebar), st.spinner('Wait for it...'):
                print(subprocess.run(['yolo', 'task=detect', 'mode=predict', 'model=best.pt', 'conf=0.25', 'source={}'.format(source)], capture_output=True, universal_newlines=True).stderr)

            if source_index == 0:
                with st.spinner(text='Preparing Images'):
                    for img in os.listdir(get_detection_folder()):
                        image_path = str(Path(f'{get_detection_folder()}') / img)

                        # Load the image using PIL to check if it's valid
                        try:
                            image = Image.open(image_path)
                            st.image(image_path)
                        except Exception as e:
                            st.error(f"Error loading image {image_path}: {e}")

                    st.write("""Acne is a common skin condition that occurs when hair follicles become clogged with oil and dead skin cells. 
                    It often manifests as pimples, blackheads, whiteheads, or cysts, and can occur on the face, neck, chest, back, shoulders, and upper arms. Symptoms of acne can vary in severity and may include:""")
                    st.write("""1. Pimples: These are raised bumps on the skin that may be red, swollen, and filled with pus. They can appear as whiteheads, which are closed comedones 
                    with a white center, or blackheads, which are open comedones with a dark surface.""")
                    st.write("""2. Cysts: These are large, painful, pus-filled lumps beneath the surface of the skin. 
                    Cysts are a more severe form of acne and can cause scarring if not treated properly.""")
                    st.write("""3. Nodules: Similar to cysts, nodules are large, painful bumps deep within the skin. They develop when clogged pores become infected and inflamed.""")
                    st.write("""4. Papules: These are small, red bumps on the skin that may be tender to the touch.
                    Papules occur when the hair follicles become inflamed due to excess oil and bacteria.""")
                    st.write("""5. Scarring: Severe acne can lead to permanent scarring, which may be depressed or raised. 
                    Scarring occurs when the skin tissue is damaged during the healing process.""")
                    st.write("""6. Oily skin: Excess oil production, known as sebum, is a common symptom of acne. 
                    Oily skin can contribute to clogged pores and the development of acne lesions.""")
                    st.write("""7. Inflammation: Acne is often accompanied by redness and inflammation in the affected areas. 
                    Inflammation occurs as the body's immune response attempts to fight off the bacterial infection within the hair follicles.""")
                    st.write("""8. Itching or burning: Some individuals may experience itching or burning sensations in areas affected by acne, especially when the skin is inflamed or irritated.""")


            else:
                with st.spinner(text='Preparing Video'):
                    for vid in os.listdir(get_detection_folder()):
                        video_path = str(Path(f'{get_detection_folder()}') / vid)

                        # Display video path or any other relevant info
                        st.write(video_path)

                    st.balloons()
if __name__ == "__main__":
    main_acne()
