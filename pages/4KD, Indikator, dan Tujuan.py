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
st.subheader("Berikut merupakan Kompetensi Dasar, Indikator, dan Tujuan Pembelajaran dari pembelajaran ini")
st.write("##")

# Menambahkan CSS untuk mengatur warna latar belakang tab menjadi biru
st.markdown(
    """
    <style>
   .streamlit-tabs.stHorizontal > .tabs {
        background-color: blue;
    }
    .streamlit-tabs.stHorizontal > .tabs .tab[data-baseweb="tab"] {
        background-color: blue;
    }
    </style>
    """,
    unsafe_allow_html=True
)

tab1, tab2, tab3 = st.tabs(["Kompetensi Dasar", "Indikator Pembelajaran", "Tujuan Pembelajaran"])

with tab1:
   st.header("Kompetensi Dasar")
   st.image("https://64.media.tumblr.com/aec7a73cca416ac79af34fe872580733/b572e299a4335b22-57/s1280x1920/595651a51e06ca99ef579740cf0f39dffe904963.png", width=320)
with tab2:
   st.header("Indikator Pembelajaran")
   st.image("https://64.media.tumblr.com/a72601a87694555d7cf6a6969d799354/a85892fee2c556bd-e8/s1280x1920/f086cc9ac5817d6c7a9fd8122071cf73072921af.pnj", width=320)

with tab3:
   st.header("Tujuan Pembelajaran")
   st.image("https://64.media.tumblr.com/5bf8842a73ea2290efd289cc7ad642c6/35f6ada5b3b3d1a9-b4/s1280x1920/1beea0094d5fdc1eb13f5ac972db1e1cb7ed46fc.pnj", width=320)

st.write("---")


# Tulis
#Ganti Page Berdampingan
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

from streamlit_extras.switch_page_button import switch_page

col1, col2= st.columns(2)
with col1:
   want_to_menu = st.button("\u25C0   Menu")
if want_to_menu:
   switch_page("Menu")
 
with col2:
   want_to_pemb = st.button("Next   \u25B6   Pembelajaran 1")
if want_to_pemb:
   switch_page("Pembelajaran 1")
