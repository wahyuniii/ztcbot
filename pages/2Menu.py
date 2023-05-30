import streamlit as st



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
st.header("Hai teman-teman, Perkenalkan Aku Zatacbot :wave:")
st.subheader("Mari kita belajar bersama pelajaran IPA Materi Zat Tunggal dan Campuran")
st.subheader ("Silahkan pilih salah satu menu dibawah ini")

st.write("---")

from streamlit_extras.switch_page_button import switch_page
import streamlit as st

# Tambahkan CSS untuk mengubah warna latar belakang tombol menjadi warna coklat pastel
st.markdown(
    """
    <style>
    .stButton button {
        font-size: 18px;
        background-color: #ff8c00; /* Ubah dengan kode warna coklat pastel yang diinginkan */
        color: white;
        width:100%
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Tombol KD, Indikator, dan Tujuan Pembelajaran
want_to_kd = st.button("KD, Indikator, dan Tujuan Pembelajaran")
if want_to_kd:
    switch_page("KD, Indikator, dan Tujuan")

# Tombol Pembelajaran 1
want_to_pemb1 = st.button("Pembelajaran 1")
if want_to_pemb1:
    switch_page("Pembelajaran 1")

# Tombol Pembelajaran 2
want_to_pemb2 = st.button("Pembelajaran 2")
if want_to_pemb2:
    switch_page("Pembelajaran 2")

# Tombol About
want_to_about = st.button("About")
if want_to_about:
    switch_page("About")
