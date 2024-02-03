import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

logo = Image.open("assets/Philippine_Statistics_Authority.png")
st.set_page_config(page_title="2020 Philippines Population Census", page_icon=logo, layout="wide")

st.markdown("<h1 style='text-align: center;'>Philippines Total Population by Province, City, and Municipality as of 2020</h1>", unsafe_allow_html=True)

#Map
def display_map(location_data: pd.DataFrame):
    fig = px.scatter_mapbox(
        location_data, lat="Latitude", lon="Longitude", zoom=4.2,
        hover_name='Name', hover_data=['Population']
    )
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig


#PH Regions
Region_4A = 'data\Region 4A.csv'


#Filter by Region
st.header('Select a Region')
selected_region = st.selectbox('Regions:', ('Region I – Ilocos Region', 'Region IV‑A – CALABARZON'))


if selected_region == 'Region IV‑A – CALABARZON':
    df = pd.read_csv(Region_4A, 
                     usecols=['Name', 'Population', 'Latitude', 'Longitude'])
    df.columns = ['Name', 'Population', 'Latitude', 'Longitude']
    px_map = display_map(df)
    st.plotly_chart(px_map, use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>CALABARZON</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>(Region IV‑A)</h3>", unsafe_allow_html=True)
    st.write(
        """
        CALABARZON, officially designated as Region IV‑A, is an administrative region in the Philippines occupying the central section of Luzon. 
        It covers 5 provinces, namely, Batangas, Cavite, Laguna, Quezon, and Rizal, as well as 1 highly urbanized city. 
        The regional center is the City of Calamba.

        Its population as determined by the 2020 Census was 16,195,042. This represented 26.04% of the overall population of the Luzon island group, or 14.85% of the 
        entire population of the Philippines. Based on these figures, the population density is computed at 977 inhabitants per square kilometer or 2,530 inhabitants per 
        square mile.
        """
    )