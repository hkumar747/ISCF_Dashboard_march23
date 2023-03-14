
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from datetime import date, datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import seaborn as sns

st.header("Time View")

st.markdown('Investigate energy patterns through time')

dfpath = 'data/cons28_temp_may_apr.csv'
dfm = pd.read_csv(dfpath)

checkvar = st.selectbox('Select variable', options = ['Total Consumption', 'Avg. Consumption', 'Solar', 'Total Emissions'])
ems_factor = st.number_input('Insert emissions factor (kg of CO2 per kWH)')
gen_loss = st.number_input('Insert T&D losses (percent of generation)')

dfm['date'] = pd.to_datetime(dfm.date, format='%d-%m-%Y')
dfm['ems'] = dfm.imp*ems_factor*(1+gen_loss/100)

dfm_d = dfm.groupby(['date_elec']).agg(totcons=('imp', np.sum),
                                                avgcons=('imp', np.mean), 
                                                wind=('wspd', np.mean),
                                                avt=('tavg', np.mean), mint=('tmin', np.mean),
                                                maxt=('tmax', np.mean)).reset_index()

#dfm_d["date2"] = pd.to_datetime(dfm_d['date_elec'])
ind = st.radio("View?",('Individual','Cumulative'))

#
st.write('Default emissions factor is 0.7 kg/kwH. Your factor is', ems_factor)
st.write('Default T&D losses are 20%. Your factor is', gen_loss)

dfm_d['ems'] = dfm_d.totcons*ems_factor*(1+gen_loss/100)

if ind=='Cumulative':
    if checkvar == 'Total Consumption':
        fig = go.Figure([go.Scatter(x=dfm_d['date_elec'], y=dfm_d['totcons'])])
        fig.update_layout(
        title="Total consumption, sum (28 consumers)",
        xaxis_title="Date",
        yaxis_title="Total Consumption (kWh)",
        legend_title="Legend Title")
    if checkvar == 'Avg. Consumption':
        fig = go.Figure([go.Scatter(x=dfm_d['date_elec'], y=dfm_d['avgcons'])])
        fig.update_layout(
        title="Total consumption, average (28 consumers)",
        xaxis_title="Date",
        yaxis_title="Consumption (kWh)",
        legend_title="Legend Title")    
    if checkvar == 'Total Emissions':
        fig = go.Figure([go.Scatter(x=dfm_d['date_elec'], y=dfm_d['ems'])])
        fig.update_layout(
        title="Emissions, total (28 consumers)",
        xaxis_title="Date",
        yaxis_title="Emissions (kg)",
        legend_title="Legend Title") 
    st.plotly_chart(fig)

#dfm.sort_values(by='date_elec', ascending=True, inplace=True)











