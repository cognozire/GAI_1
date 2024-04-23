# import streamlit as st

# def write_note():
#     note = st.text_area("Write your note here:")
#     return note

# def save_note_to_file(note):
#     with open("notes.txt", "a") as file:
#         file.write(note + "\n")
# def download_file():
#     with open("notes.txt", "r") as file:
#         notes_content = file.read()
#     return notes_content
# def main():
#     st.title("Notes")

#     # Get the note from the user
#     note = write_note()

#     # Save the note to a text file when the user clicks the button
#     if st.button("Save Note"):
#         save_note_to_file(note)
#         st.success("Note saved successfully!")
#     if st.button("Download Notes"):
#         notes_content = download_file()
#         st.download_button(
#             label="Download Notes",
#             data=notes_content,
#             file_name="notes.txt",
#             key="download_notes"
#         )

# if __name__ == "__main__":
#     main()

import streamlit as st
from audio_recorder_streamlit import audio_recorder
import wave
import time

from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# def write_note():
#     note = st.text_area("Write your note here:")
#     return note

# def save_note_to_file(note):
#     with open("notes.txt", "a") as file:
#         file.write(note + "\n")

# def download_file():
#     with open("notes.txt", "r") as file:
#         notes_content = file.read()
#     return notes_content

def notes_main():
    st.title("Notes")

    st.markdown('*Click the icon to add new note.*')
    c1, c2, c3, c4, c5, c6, c7, c8 = st.columns(8)
    with c1:
      audio_bytes = audio_recorder(text="Record", icon_size="0.5x", pause_threshold=10.0)
    try:
      if audio_bytes:
          st.audio(audio_bytes, format="audio/wav")
        
          apiUrl = "https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/5f9e33da-3d8f-4924-9b18-2ef9c3dd288d"
          myKey = st.secrets["key"]
    
          auth = IAMAuthenticator(myKey)
          Speech2Text = SpeechToTextV1(authenticator = auth)
          Speech2Text.set_service_url(apiUrl)
    
          response = Speech2Text.recognize(audio = audio_bytes, content_type = "audio/wav")
          recognized_text = response.result['results'][0]['alternatives'][0]['transcript']
          
          st.markdown(" ")
          st.markdown("*Content Recognized*")
          st.info(recognized_text)
    
          st.markdown(" ")
          time.sleep(2)
          st.success('Note Saved!')
    except:
       st.error('Try speaking for a longer duration.')

#     # Get the note from the user
#     note = write_note()

#     # Save the note to a text file when the user clicks the button
#     if st.button("Save Note"):
#         save_note_to_file(note)
#         st.success("Note saved successfully!")

#     # Download the notes content when the user clicks the button
#     if st.button("Download Notes"):
#         notes_content = download_file()
#         st.download_button(
#             label="Download Notes",
#             data=notes_content,
#             file_name="notes.txt",
#             key="download_notes"
#         )



if __name__ == "__main__":
    notes_main()
