
import streamlit as st


from api_calling import note_generator,quiz_generator
from text_to_voice import TTV

#title Part
st.title("Note Summery and Quize Generator")
st.markdown("Upload up to 3 images to generate Note summery and Quizzes")
st.divider()

#Sidbar
with st.sidebar : 
    st.header("Controller")

    images = st.file_uploader("Upload you images for make summery", type=["png","jpg","jpeg"],accept_multiple_files=True)

    if images : 

        if len(images) > 3 :
            st.error("Upload at max 3 images")

        else :
            st.subheader("Your uploaded images")
            col = st.columns(len(images))
         
            for i,img in enumerate(images) :
                with col[i] :
                    st.image(img)

    # set difecaties with select bos
    selected_option = st.selectbox("Select your difficulty of your quiz",("Eesy","Medium","Hard"),index=None)

    is_press = st.button("Click the button to initiate to AI",type="primary")

if is_press :
    if not images : 
        st.error("You have must upload a 1 image")

    elif not selected_option : 
        st.error("You must select a defficulty")

    elif images and selected_option : 
        ## Note 
        with st.container(border=True) :
            st.subheader("Notes Summary")

            with st.spinner("AI is writing you note") : 
                 note_summary = note_generator(images) 
                 st.markdown(note_summary)

        ##Audio transcripts
        with st.container(border=True) :
            st.subheader("Summary of audio")

            # remove markdown 
            note_summary = note_summary.replace("#","")
            note_summary = note_summary.replace("*","")
            note_summary = note_summary.replace("()","")
            note_summary = note_summary.replace("-","")
            note_summary = note_summary.replace("`","")

            with st.spinner("Making audio to note summary") : 
                audio_voice = TTV(note_summary)
                st.audio(audio_voice)

        ##Quizzes
        with st.container(border=True) :
            st.subheader(f"Quiz ({selected_option}) Difficulty")

            with st.spinner(f"AI making quizzes based on label {selected_option}") : 
                quizzes = quiz_generator(images,selected_option)
                st.markdown(quizzes)