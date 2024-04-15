import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv("C:\\Users\\91905\\Downloads\\india.csv")

list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Overall India')

st.sidebar.title("India's Data ")
selected_state = st.sidebar.selectbox('Select a state',list_of_states)
primary = st.sidebar.selectbox('Select a primary parameter',sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Select a secondary parameter',sorted(df.columns[5:]))

plot = st.sidebar.button('Plot graph')

if plot:
  st.text('Size represents primary parameter')
  st.text('Color represents secondary parameter')
  if selected_state == 'Overall India':
    # plot for India
    fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=4,size_max=35,
     mapbox_style="carto-positron",width=1200,height=700,hover_name='District')
    st.plotly_chart(fig,use_container_width=True)
  else:
    # plot for the states
    state_df = df[df['State'] == selected_state]

    fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=6,
                            size_max=35,
                            mapbox_style="carto-positron", width=1200, height=700, hover_name='District')

    st.plotly_chart(fig, use_container_width=True)


india = pd.read_csv('india.csv')
print(india.head())
