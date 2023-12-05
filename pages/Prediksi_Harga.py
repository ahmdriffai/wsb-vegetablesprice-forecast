import streamlit as st
from datetime import date
import pandas as pd
from plotly import graph_objs as go
from prophet import Prophet
from prophet.plot import plot_plotly

START = "2022-08-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title("Prediksi Harga Sayur")


stock = ("KTG", "CRM", "CMK")

selected_stocks = st.selectbox("Selecet", stock)

@st.cache_data
def load_data(pick_harga):
    data = pd.read_csv(f"data/timeseries-{pick_harga}-wonosobo.csv")
    data.reset_index(inplace=True)
    return data

data_load_state = st.text("Loading data...")
data = load_data(selected_stocks)
data_load_state.text("Loading data.. done")
data_load_state.text("")



st.subheader(f"Data harga {selected_stocks} 5 hari terakhir")
st.table(data[['tanggal', 'harga']].tail(5))

def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['tanggal'], y=data['harga'], name='harga_kentang'))
    fig.layout.update(title_text=f"Grafik Harga {selected_stocks}", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data()

# forecasting
n_year = st.slider(F"Prediksi perhari ke-", 1, 30)
period = n_year

df_train = data[['tanggal', 'harga']]
df_train = df_train.rename(columns={"tanggal": "ds", "harga": "y"})

m = Prophet()
m.fit(df_train)

future = m.make_future_dataframe(period)

forecast = m.predict(future)
forecast = forecast.rename(columns={"ds": "tanggal", "yhat_upper": "prediksi"})

def plot_raw_data2():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=forecast['tanggal'].tail(period), y=forecast['prediksi'].tail(period), name='harga_kentang'))
    fig.layout.update(title_text=f"Grafik Prediksi Harga {selected_stocks}", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

st.subheader(f"Prediksi harga {selected_stocks} {period} hari kedepan")
st.table(forecast[['tanggal', 'prediksi']].tail(period))

plot_raw_data2()