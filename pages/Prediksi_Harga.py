import streamlit as st
from datetime import date
import pandas as pd
from plotly import graph_objs as go
from prophet import Prophet
from prophet.plot import plot_plotly
import datetime
from streamlit_card import card
from st_card_component import card_component

START = "2022-08-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title("Prediksi Harga Sayur")

stock = ("KTG", "CRM", "CMK", "BMK")

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



# st.subheader(f"Data harga {selected_stocks} 5 hari terakhir")
# st.table(data[['tanggal', 'harga']].tail(5))

def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['tanggal'], y=data['harga'], name='harga_kentang'))
    fig.layout.update(title_text=f"Grafik Harga {selected_stocks}", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data()


# n_year = st.slider(F"Prediksi perhari ke-", 1, 360)
tanggal = st.date_input("Pilih tanggal prediksi ", datetime.date(2023, 12, 20))
print(tanggal)
period = 360

df_train = data[['tanggal', 'harga']]
df_train = df_train.rename(columns={"tanggal": "ds", "harga": "y"})

m = Prophet()
m.fit(df_train)

future = m.make_future_dataframe(period)

forecast = m.predict(future)
print(forecast)
# print(forecast)
forecast = forecast.rename(columns={"ds": "tanggal", "yhat": "prediksi"})

filtered_df = forecast.loc[(forecast['tanggal'] == f'{tanggal} 00:00:00')]

# hasClicked = card(
#   title=f"Rp. {format(int(filtered_df['prediksi'].values[0]), ',')}",
#   text="Some description",
# )
# st.card(f"Prerdiksi harga {selected_stocks} per tanggal {tanggal}: Rp. {format(int(filtered_df['prediksi'].values[0]), ',')}")

kpi1, kpi2 = st.columns(2)
kpi1.metric(label=f"Harga {selected_stocks} per tanggal {tanggal}", value=format(int(filtered_df['prediksi'].values[0]), ','))
# res = card(
#     title=f"Rp. {format(int(filtered_df['prediksi'].values[0]), ',')}",
#     text=f"Harga {selected_stocks} per {tanggal}",
#     image="https://unsplash.com/photos/brown-round-food-in-stainless-steel-container-52DMHPBAvXY"
# )
def plot_raw_data2():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=forecast['tanggal'].tail(period), y=forecast['prediksi'].tail(period), name='harga_kentang'))
    fig.layout.update(title_text=f"Grafik Prediksi Harga {selected_stocks} 1 Tahun Kedepan", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

st.subheader(f"Prediksi harga {selected_stocks} {period} hari kedepan")
st.table(forecast[['tanggal','prediksi']].tail(period))

plot_raw_data2()

# pkl
import streamlit as st
import pickle

# Muat model dari file pickle
# with open('../model/model.pkl', 'rb') as file:
#     model = pickle.load(file)

# Prediksi menggunakan model

# data_awal_predict = df_train[:-20]
# predict = []

# for i in range(period):
#     predict.append(model.predict([[]]))
# prediction = model.predict([[input_value]])