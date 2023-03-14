import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px #install plotly
import plotly.figure_factory as ff
import statsmodels.api as sm

st.header("Climate impact analysis")

st.markdown("This page shows the impact of climatic factors on electricity consumption in the city area. \n If a city administrator wishes to know by how much electricity consumption rises with \n variation in temperature, they can run pre-specified regression and ML models and even forecast future cases.")
dfpath = 'data/cons28_temp_may_apr.csv'

dfm = pd.read_csv(dfpath)

dfm['date'] = pd.to_datetime(dfm.date, format='%d-%m-%Y')


### slider for IMP 
dfm2=dfm[dfm.imp>50].copy()

#Select arguments from dropdown
var1 = st.radio("Energy variable",('Consumption','Solar'))
model1 = st.radio("Model",('OLS(Linear)','LOWESS(Polynomial)'))

#st.sidebar.checkbox("Temp vars", True, key = 1)
selected_status = st.selectbox('Select climate variable',
                                       options = ['Avg. temperature', 
                                                  'Min. temperature', 'Max. Temperature', 'Wind Speed'])

st.markdown('The effect of a 1 unit rise in the chosen variable = ')
st.metric(label="Heating energy factor", value="3.3 %", delta=0.33)
   
if model1=="OLS(Linear)":  
  if selected_status == 'Avg. temperature':
    fig = px.scatter(dfm2, x='tavg', y='imp', color='tavg', opacity = .65, trendline="ols", trendline_scope="overall")
    model = px.get_trendline_results(fig)
    results = model.iloc[0]["px_fit_results"]
    alpha = results.params[0]
    beta = results.params[1]
    p_beta = results.pvalues[1]
    line1 = 'Coefficient = ' + str(round(beta, 4))
    line2 = 'p-value = ' + '{:.5f}'.format(p_beta)
    summary = line1 + '<br>' + line2
    fig.add_annotation(
          x=20,
          y=350,
          xref="x",
          yref="y",
          text=summary,
          font=dict(
              family="Courier New, monospace",
              size=16,
              color="#ffffff"
              ),
          align="left",
          arrowhead=2,
          arrowsize=1,
          arrowwidth=2,
          arrowcolor="#636363",
          ax=20,
          ay=-30,
          borderwidth=2,
          borderpad=4,
          bgcolor="rgba(100,100,100, 0.6)",
          opacity=0.8)
  if selected_status == 'Min. temperature':
    fig = px.scatter(dfm2, x='tavg', y='imp', color='tavg', opacity = .65, trendline="ols", trendline_scope="overall")
    model = px.get_trendline_results(fig)
    results = model.iloc[0]["px_fit_results"]
    alpha = results.params[0]
    beta = results.params[1]
    p_beta = results.pvalues[1]
    line1 = 'Coefficient = ' + str(round(beta, 4))
    line2 = 'p-value = ' + '{:.5f}'.format(p_beta)
    summary = line1 + '<br>' + line2
    fig.add_annotation(
          x=20,
          y=350,
          xref="x",
          yref="y",
          text=summary,
          font=dict(
              family="Courier New, monospace",
              size=16,
              color="#ffffff"
              ),
          align="left",
          arrowhead=2,
          arrowsize=1,
          arrowwidth=2,
          arrowcolor="#636363",
          ax=20,
          ay=-30,
          borderwidth=2,
          borderpad=4,
          bgcolor="rgba(100,100,100, 0.6)",
          opacity=0.8)
  if selected_status == 'Max. Temperature':
    fig = px.scatter(dfm2, x='tmax', y='imp', color='tavg', opacity = .65, trendline="ols", trendline_scope="overall")
    model = px.get_trendline_results(fig)
    results = model.iloc[0]["px_fit_results"]
    alpha = results.params[0]
    beta = results.params[1]
    p_beta = results.pvalues[1]
    line1 = 'Coefficient = ' + str(round(beta, 4))
    line2 = 'p-value = ' + '{:.5f}'.format(p_beta)
    summary = line1 + '<br>' + line2
    fig.add_annotation(
          x=20,
          y=350,
          xref="x",
          yref="y",
          text=summary,
          font=dict(
              family="Courier New, monospace",
              size=16,
              color="#ffffff"
              ),
          align="left",
          arrowhead=2,
          arrowsize=1,
          arrowwidth=2,
          arrowcolor="#636363",
          ax=20,
          ay=-30,
          borderwidth=2,
          borderpad=4,
          bgcolor="rgba(100,100,100, 0.6)",
          opacity=0.8)   
  if selected_status == 'Wind Speed':
    fig = px.scatter(dfm2, x='wspd', y='imp', color='tavg', opacity = .65, trendline="ols", trendline_scope="overall")
    model = px.get_trendline_results(fig)
    results = model.iloc[0]["px_fit_results"]
    alpha = results.params[0]
    beta = results.params[1]
    p_beta = results.pvalues[1]
    line1 = 'Coefficient = ' + str(round(beta, 4))
    line2 = 'p-value = ' + '{:.5f}'.format(p_beta)
    summary = line1 + '<br>' + line2
    fig.add_annotation(
          x=20,
          y=350,
          xref="x",
          yref="y",
          text=summary,
          font=dict(
              family="Courier New, monospace",
              size=16,
              color="#ffffff"
              ),
          align="left",
          arrowhead=2,
          arrowsize=1,
          arrowwidth=2,
          arrowcolor="#636363",
          ax=20,
          ay=-30,
          borderwidth=2,
          borderpad=4,
          bgcolor="rgba(100,100,100, 0.6)",
          opacity=0.8)   

  st.plotly_chart(fig)

# example taken here: https://alanjones.hashnode.dev/create-a-multi-page-interactive-dashboard-with-streamlit-and-plotly
if model1=="LOWESS(Polynomial)":
  if selected_status == 'Avg. temperature':
    fig = px.scatter(dfm2, x='tavg', y='imp', color='tavg', opacity = .65, trendline="lowess", trendline_scope="overall")
  if selected_status == 'Max. Temperature':
    fig = px.scatter(dfm2, x='tmax', y='imp', color='tmax', opacity = .65, trendline="lowess", trendline_scope="overall")
  if selected_status == 'Min. temperature':
    fig = px.scatter(dfm2, x='tmin', y='imp', color='tmin', opacity = .65, trendline="lowess", trendline_scope="overall")
  if selected_status == 'Wind Speed':
    fig = px.scatter(dfm2, x='wspd', y='imp', color='wspd', opacity = .65, trendline="lowess", trendline_scope="overall")
  st.plotly_chart(fig)
# example taken here: https://alanjones.hashnode.dev/create-a-multi-page-interactive-dashboard-with-streamlit-and-plotly





