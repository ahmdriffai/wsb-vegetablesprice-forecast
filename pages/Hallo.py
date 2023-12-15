import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Hello, Selamat Datang! 👋")

st.markdown(
    """
    Kenali Pasar, Antisipasi Harga!

    Selamat datang di platform terdepan yang membantu Anda merencanakan belanja sayur dengan lebih cerdas dan efisien di Wonosobo. Kami menghadirkan solusi inovatif untuk membantu Anda memprediksi harga sayur di tingkat produsen sehingga Anda dapat membuat keputusan berdasarkan informasi terkini.
    
    **👈 Pilih Menu Prediksi Harga** utuk memprediksi harga sayur di Wonosobo
    ### Mengapa Memilih Kami?
    - Prediksi Akurat
    - Informasi Real-Time
    - Analisis Pasar
    
    ### See more
    - Dataset Time Series [Harga Sayur Jawa Tengah](https://infoharga.agrojowo.biz/grafik/sayuran/produsen/)
    - Repository [Prediksi Harga Sayur Wonosobo](https://github.com/ahmdriffai/wsb-vegetablesprice-forecast)
"""
)