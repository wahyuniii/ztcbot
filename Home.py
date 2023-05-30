import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_extras.stateful_button import button


# Menghilangkan tombol Menu
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Mengganti Background dengan gambar
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://64.media.tumblr.com/19e325c4db0127cb929c480ab8a6a6be/1a9c54c2177c376d-da/s500x750/748f7658e9c6ef4c0118eaf3494e318b7fe2333f.pnj");
background-size: cover;
}

[data-testid="stHeader"] {
background-color: rgba{0, 0, 0, 0};
}

[data-testid="stToolbar"] {
right: 2rem;
}

[data-testid="stSidebar"] {
background-image: url("https://64.media.tumblr.com/4c02b74ff816cbfb7cd0984e11beb3dc/5d89598f9be0fd33-1c/s2048x3072/b8061c275a1b5d1d564f43ab6433b97927929cdc.pnj");
background-size: cover;
}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Mulai Title
st.title("HAI DENGAN ZATACBOT DISINI :wave:")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://assets2.lottiefiles.com/packages/lf20_3vbOcw.json"
lottie_html = f'<div class="lottie" style="background-color: #FF000;"><lottie-player src="{lottie_url_hello}" background="transparent" speed="1" loop autoplay></lottie-player></div>'
st.markdown(lottie_html, unsafe_allow_html=True)
lottie_hello = load_lottieurl(lottie_url_hello)

st_lottie(lottie_hello, key="hello")

# Menambahkan CSS untuk mengatur teks menjadi rata tengah, besar, dan latar belakang teks
import streamlit as st


if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

st.markdown(
    """
    <style>
    .my-text {
        font-size: 16px;
    }
    .stTextInput input {
        background-color: #B0E0E6;
    }
    .stTextInput label {
        font-size: 20px;
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="my-text">Untuk mulai belajar, tuliskan Namamu pada kolom dibawah ini kemudian tekan Submit  \u2193  \u2193  \u2193</p>', unsafe_allow_html=True)

my_input = st.text_input(st.session_state["my_input"])

submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.markdown(f"Selamat datang **{my_input}**, Zatacbot siap menemani belajarmu")
    st.write("Sebelum memulai belajar, bacalah petunjuk penggunaan Zatacbot terlebih dahulu ya")
    st.image("https://64.media.tumblr.com/77c5c4c51d2ea3df5b71138a19ad63f6/e708fdafee49a5db-7c/s400x600/821765f7145c3ba7b58249eeaf3e2528df374a1d.pnj", width=340)

# Tulis