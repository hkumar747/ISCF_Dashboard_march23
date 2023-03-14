#


import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import json
import plotly.graph_objects as go

#dfpath1 = 'data/dtr_squares_json'
dfpath2 = 'data/geo_dtr_1day_cons.csv'

#dfjsn = json.load(dfpath1, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None)
df2 = pd.read_csv(dfpath2)


st.title("Map View - Naroda")


s1 = st.selectbox('Variable', options = ['Solar', 'Consumption'])
s3 = st.selectbox('Map type', options = ['Point', 'Heatmap'])

ques = st.radio("Quantities?",('Per capita','Total', 'Mean'))

# Metrics
col1, col2 = st.columns(2)
sol_av = df2.active_energy_exp.mean().round(3)
col1.metric(label="Average Solar Energy Exported", value=sol_av, delta=-0.5)

cons_av = df2.active_energy.mean().round(3)
col2.metric(label="Average electricity consumed", value=cons_av, delta=-0.5,
delta_color="inverse")

if s3=='Point':
   if s1=="Consumption":
        fig = px.scatter_mapbox(df2, lat='latitude', lon='longitude', color='active_energy',
             size="active_energy", color_continuous_scale=px.colors.cyclical.IceFire, mapbox_style="open-street-map")
        st.plotly_chart(fig)
   if s1=="Solar":
        fig = px.scatter_mapbox(df2, lat='latitude', lon='longitude', color='active_energy_exp',
             size="active_energy_exp", color_continuous_scale=px.colors.cyclical.IceFire, mapbox_style="open-street-map")
        st.plotly_chart(fig)

if s3=='Heatmap':
    if s1=="Consumption":
        fig = px.density_mapbox(df2, lat='latitude', lon='longitude', z='active_energy', radius=23,
            center=dict(lat=23, lon=72.5), zoom=8,  color_continuous_scale='inferno',
            mapbox_style="open-street-map")
        st.plotly_chart(fig, width=800)
    if s1=="Solar":
        fig = px.density_mapbox(df2, lat='latitude', lon='longitude', z='active_energy_exp', radius=15,
            center=dict(lat=23, lon=72.5), zoom=8,  color_continuous_scale='inferno',
            mapbox_style="open-street-map")
        st.plotly_chart(fig, width=800)