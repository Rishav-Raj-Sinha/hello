from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.title("Hello Kitty")
st.header(":3")

st.image("7a1f6135d4e10c92dd51ab5531a7c8f0.jpg")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    
    return r.json()

lottie_hello = load_lottieurl("https://lottie.host/15ddaaf6-71a9-4458-9f21-31e965ded5ac/49cQNEerWz.json")

st_lottie(lottie_hello, key="hello")
