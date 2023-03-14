import streamlit as st
import plotly.express as px
import pandas as pd

dfpath3 = 'data/dtrs_1yr.csv'
dfpath15 = 'data/dtr_15min.csv'

df3 = pd.read_csv(dfpath3)
df15 = pd.read_csv(dfpath15)

df3['ratio'] = df3.totsol * 100 / (df3.totcons + 1)

# Set page layout
st.set_page_config(page_title='Area-level energy consumption', layout='wide')

# Set title and subtitle
st.title('Area-level energy consumption')
st.write('Find out which areas had the best and worst energy usage metrics?')

# Set sidebar
option = st.radio(
    'Select a view',
    ('Annual summary', 'Annual detail'))

if option == 'Annual summary':
    # Show annual summary table
    dfs = df3[['DTR_NAME', 'totcons', 'totsol', 'tot_cons_pc', 'avgcons', 'ratio']]
    dfs['Total p.c consumption'] = df3.tot_cons_pc
    dfs['Total Solar exp.'] = df3.totsol
    dfs['Renewable percent'] = df3.ratio
    dfs = dfs[['DTR_NAME', 'Total p.c consumption', 'Total Solar exp.', 'Renewable percent']]
    st.dataframe(dfs, height=400)
    
else:
    # Show annual detail line graph
    st.write('Active energy usage over time')
    fig = px.line(df15, x='datetime', y='active_energy', color='dtr_name', 
                render_mode="svg", hover_name='dtr_name')
    
    # loop over the traces and update the line color and hoverlabel color
    for trace in fig.data:
        trace.update(line={'color': 'lightcoral'}, 
                 hoverlabel={'bgcolor': 'red'})

# update the layout with hovermode and hoverinfo
    fig.update_layout(width=1000, 
        height=800, plot_bgcolor='white')

# show the figure
    fig.update_layout(showlegend=False)
    graph_box = st.container()
    with graph_box:
        st.plotly_chart(fig)
