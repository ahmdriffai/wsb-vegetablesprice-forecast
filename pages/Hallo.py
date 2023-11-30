import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Hello, Selamat Datang! 👋")

st.markdown(
    """
    Kenali Pasar, Antisipasi Harga!

    Selamat datang di platform terdepan yang membantu Anda merencanakan belanja sayur dengan lebih cerdas dan efisien di Wonosobo. Kami menghadirkan solusi inovatif untuk membantu Anda memprediksi harga sayur sehingga Anda dapat membuat keputusan berdasarkan informasi terkini.
    
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Mengapa Memilih Kami?
    - Prediksi Akurat
    - Informasi Real-Time
    - Analisis Pasar
    
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)