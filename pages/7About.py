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
st.title("Pengembang Zatacbot")
st.write("---")
st.image("https://lh3.googleusercontent.com/fife/APg5EObm06_cIDY2fkoIXnASFzMjFOspb5vao3ZWtWhyp-zf5yKFGv4RzPgIWhZlZcj6ULmIR5amM6uNCXAWzVvhw1xbpfQzVp1E7aJ5HLt-pdoCpJIS_24gwftKBpgM3C7rBgDl8dPBe8vKSLPNKRkJz4KGjONwpwIbOSPL7UfIblgiTi4y4OiKGWT3WnzKBRA-ZcO0DMp_f-sd8CtFuN7872WmA8Z7XlJ_Wu7PLEm62gzIFpr1hcrIae6ay55-NnYPi4T8X5yAq2CjhFJWKv8gWiPGf2EKymgQ5YB56MCu-gJD1xSd7RxeZ7PK1Te5bRcLQqgmwrsMujHDlQHyN0RUfNIFlS5WCQs9LBivmrvC_7HTp2KoBk_UKehpXSrHH9O-7P60rDhpqzrKU_tBGCFxbitnLpovjs1katSNkyTq7XUla_Zo1LbmGWfxPA296n2AOB1hv14ygmUZF6IOcBgZOML8A0zuS45aeu9ktChIST3Gpw3Dws4X-fKMFDclTWVwTtwNWrvnMr_XSWpjaAlYic9XnljoG8T_ysjoLG64WwbDgCWjdanb6nM2Clx0Q3QcnW9FUJOZ6ZJ9R_nvLSBuQHaRnRt1Jcu-HzjYGRRFMuCWfFz2Gu4ALmWeOFHrdCJtJjI9YF9lkvtgX1QuGW6OyrIBJEVOCHdD-D5dUInIu77xdqNZeS28Ve5B6Ed-8UtJywUe440L2bhulJh73zJotKh3TwNp7I1MzkpKxidGmgIP91o53f28Eg8p8TFOU_0CK35NrVenXGy4satVwkSR-lLPA-wG18yJhz_YSQ0m8JRWNrnPDrDQmrvFRN5YvX7XsM47kSmQrE2vbXky6PLa1vUxVA0ULTWftBsyvO3qWbkBbk0bP7r_lXyfNJbuyN5AQYKAyP1XLW5KNcWsbFgr-f68vsFZUpxlVvQlX8cmmThkTVoRPlATM6nykmygnYB3nyrX5w1BypZa3fhjTkzAyufTp-gjs6KV1bnSvCi6qeE74U3DGToARBr66iOdJEiiXlhcp-Tt1mKJ1eA_Xn9q4RCbsgvmW33y3oivmh_6QqlVLLYkQNEPs9OXfiFeElpBgFIB6A35s_ytYf0LIfCX_reic2ibVOM7VUkUqbeZ9h-WKmZADN_MREVPpWi3W90YPiGUYElDb-08LzFZ7hz3VQydRpfKrmGe0S7BV6BKlCLhyxvVHwKdIGN7iYcrK1mz1W6fJWNyLkFUcSlzfp1BQ0fMER93fLvNeRC1XTNq89fRpplqLxcG4IGaPeNuVIuE2gny6RhvvxaqKt4ViF6qRa4JnZKngP1TGE1xW_womfEJFlB485BCyMPoLWxH8ldvssr4gIAHn2LIHCJyBGNgi39biOtZjPYRz2UzOl6TgAk3c6o9itUQzyYuH2eaOjqU4b-e5iuvlrFv0zGtfLXrctGwjw7qxI6fU1wwIVL3DAKISK7iwfkvP6AICziGrlA9C0BJDoqwTtsEBi2-RjpU-xJA4ExWc_7CBraoB74vUZ-ntFdeJy-Zag7wZRXIIIFWW0CqKndOfjvIa0mXNoQhZaLdOcm4aC8=s600-w450-h600-s-no?authuser=0", width=200)

st.write("---")
st.write("Nama: Wahyuni")
st.write("Alamat: Cilacap, Indonesia")
st.write("Instansi: Universitas Negeri Semarang")
st.write("Fakultas: Ilmu Pendidikan")
st.write("Jurusan: Pendidikan Guru Sekolah Dasar")
st.write("---")
st.write("Untuk saran dan masukan hub: 085758447988")


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

st.write("---")

from streamlit_extras.switch_page_button import switch_page

want_to_menu = st.button("\u25C0   Menu")
if want_to_menu:
   switch_page("Menu")



