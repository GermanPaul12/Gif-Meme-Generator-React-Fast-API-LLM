import streamlit as st
from streamlit_extras.badges import badge
from get_giphy_image import get_gif
from get_joke import get_joke
from llm_connection import get_important_word

# PageConfig
st.set_page_config(page_title='Meme Generator',page_icon='😂')

joke = get_joke()
important_word = get_important_word(joke)
gif_url = get_gif(important_word)

if type(joke) == "tuple": "\n".join(joke)

st.header(joke)
st.write(important_word)
st.write(type(joke))
st.write(gif_url)
st.markdown(f"![Joke Gif]({gif_url})")
badge(type="github", name="GermanPaul12")