import streamlit as st
import image_search

from streamlit_back_camera_input import back_camera_input

st.title("snapjack.io")
#st.header("The World's Best Botanist in the Palm of Your Hand!")
#st.image("home.jpg")
#st.write("What if you could know everything there is to know about any plant you come across from just a simple photo?")

st.header("tap to capture image!")
image = back_camera_input()
loader = st.empty()

st.markdown(
    """
<style>
    .css-10trblm {text-align: center;}
</style>
""",
    unsafe_allow_html=True,
)

if image:
    with open ('test.jpg','wb') as file:
        file.write(image.getbuffer())

    loader.write("Scowering the Internet...")
    response = image_search.scan_plant('test.jpg')
    loader.write("Found a match! The photo you took is one of a species called...")

    st.header(response)
    st.image(image)

