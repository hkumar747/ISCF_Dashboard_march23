
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

dfpath3 = 'data/dtrs_1yr.csv'

df3 = pd.read_csv(dfpath3)


df3['ratio'] = df3.totsol*100/(df3.totcons+1)

st.title('DTR-level summaries')
st.write('Find out which areas had the best and worst energy usage metrics?')
dfs = df3[['DTR_NAME','totcons','totsol','tot_cons_pc', 'avgcons', 'ratio']]
dfs['Total p.c consumption']  = df3.tot_cons_pc
dfs['Total Solar exp.']  = df3.totsol
dfs['Renewable percent']  = df3.ratio

dfs = dfs[['DTR_NAME', 'Total p.c consumption',  'Total Solar exp.', 'Renewable percent']]
st.dataframe(dfs, 1000, 400) 