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
        location_data, lat="Latitude", lon="Longitude", zoom=6.5,
        hover_name='Name', hover_data=['Population']
    )
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig


#PH Regions
Region_1 = 'data/Region 1.csv'
Region_2 = 'data/Region 2.csv'
Region_3 = 'data/Region 3.csv'
Region_4A = 'data/Region 4A.csv'

NCR = 'data/NCR.csv'
CAR = 'data/CAR.csv'

#Filter by Region
st.header('Select a Region')
selected_region = st.selectbox('Regions:', 
                               ('Region I – Ilocos Region', 'Region II – Cagayan Valley', 'Region III – Central Luzon', 
                                'Region IV‑A – CALABARZON', 
                                'NCR – National Capital Region', 'CAR – Cordillera Administrative Region'))

if selected_region == 'Region I – Ilocos Region':
    df = pd.read_csv(Region_1, 
                     usecols=['Name', 'Population', 'Latitude', 'Longitude'])
    df.columns = ['Name', 'Population', 'Latitude', 'Longitude']
    px_map = display_map(df)
    st.plotly_chart(px_map, use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>Ilocos Region</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>(Region I)</h3>", unsafe_allow_html=True)
    st.write(
        """
        Ilocos Region, officially designated as Region I, is an administrative region in the Philippines occupying the northwestern section of Luzon. 
        It covers 4 provinces, namely, Ilocos Norte, Ilocos Sur, La Union, and Pangasinan. The regional center is the City of San Fernando.

        Its :blue[population] as determined by the 2020 Census was :blue[5,301,139]. This represented 8.52% of the overall population of the Luzon island group, or 4.86% of the 
        entire population of the Philippines. Based on these figures, the population density is computed at 409 inhabitants per square kilometer or 1,059 inhabitants 
        per square mile.
        """
    )

elif selected_region == 'Region II – Cagayan Valley':
    df = pd.read_csv(Region_2, 
                     usecols=['Name', 'Population', 'Latitude', 'Longitude'])
    df.columns = ['Name', 'Population', 'Latitude', 'Longitude']
    px_map = display_map(df)
    st.plotly_chart(px_map, use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>Ilocos Region</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>(Region I)</h3>", unsafe_allow_html=True)
    st.write(
        """
        Cagayan Valley, officially designated as Region II, is an administrative region in the Philippines occupying the northeastern section of Luzon. 
        It covers 5 provinces, namely, Batanes, Cagayan, Isabela, Nueva Vizcaya, and Quirino. The regional center is the City of Tuguegarao.

        Its :blue[population] as determined by the 2020 Census was :blue[3,685,744]. This represented 5.93% of the overall population of the Luzon island group, or 3.38% of the 
        entire population of the Philippines. Based on these figures, the population density is computed at 124 inhabitants per square kilometer or 320 inhabitants per 
        square mile.
        """
    )

elif selected_region == 'Region III – Central Luzon':
    df = pd.read_csv(Region_3, 
                     usecols=['Name', 'Population', 'Latitude', 'Longitude'])
    df.columns = ['Name', 'Population', 'Latitude', 'Longitude']
    px_map = display_map(df)
    st.plotly_chart(px_map, use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>Central Luzon</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>(Region III)</h3>", unsafe_allow_html=True)
    st.write(
        """
        Central Luzon, officially designated as Region III, is an administrative region in the Philippines occupying the central section of Luzon. It covers 7 provinces, 
        namely, Aurora, Bataan, Bulacan, Nueva Ecija, Pampanga, Tarlac, and Zambales, as well as 2 highly urbanized cities. The regional center is the City of San Fernando.

        Its :blue[population] as determined by the 2020 Census was :blue[12,422,172]. This represented 19.97% of the overall population of the Luzon island group, or 11.39% of the 
        entire population of the Philippines. Based on these figures, the population density is computed at 567 inhabitants per square kilometer or 1,469 inhabitants 
        per square mile.
        """
    )

elif selected_region == 'Region IV‑A – CALABARZON':
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

        Its :blue[population] as determined by the 2020 Census was :blue[16,195,042]. This represented 26.04% of the overall population of the Luzon island group, or 14.85% of the 
        entire population of the Philippines. Based on these figures, the population density is computed at 977 inhabitants per square kilometer or 2,530 inhabitants per 
        square mile.
        """
    )

elif selected_region == 'NCR – National Capital Region':
    df = pd.read_csv(NCR, 
                     usecols=['Name', 'Population', 'Latitude', 'Longitude'])
    df.columns = ['Name', 'Population', 'Latitude', 'Longitude']
    px_map = display_map(df)
    st.plotly_chart(px_map, use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>National Capital Region</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>(NCR)</h3>", unsafe_allow_html=True)
    st.write(
        """
        The National Capital Region, officially designated as NCR, is an administrative region in the Philippines occupying the central 
        section of Luzon. It covers 1 municipality, as well as 16 highly urbanized cities. The regional center is the City of Manila.

        Its :blue[population] as determined by the 2020 Census was :blue[13,484,462]. This represented 21.68% of the overall population of the Luzon island group, or 
        12.37% of the entire population of the Philippines. Based on these figures, the population density is computed at 21,765 inhabitants per square kilometer 
        or 56,371 inhabitants per square mile.
        """
    )

elif selected_region == 'CAR – Cordillera Administrative Region':
    df = pd.read_csv(CAR, 
                     usecols=['Name', 'Population', 'Latitude', 'Longitude'])
    df.columns = ['Name', 'Population', 'Latitude', 'Longitude']
    px_map = display_map(df)
    st.plotly_chart(px_map, use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>Cordillera Administrative Region</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>(CAR)</h3>", unsafe_allow_html=True)
    st.write(
        """
        Cordillera Administrative Region, officially designated as CAR, is an administrative region in the Philippines occupying the northern-central 
        section of Luzon. It covers 6 provinces, namely, Abra, Apayao, Benguet, Ifugao, Kalinga, and Mountain Province, as well as 1 highly urbanized city. 
        The regional center is the City of Baguio.

        Its :blue[population] as determined by the 2020 Census was :blue[1,797,660]. This represented 2.89% of the overall population of the Luzon island group, or 1.65% of 
        the entire population of the Philippines. Based on these figures, the population density is computed at 91 inhabitants per square kilometer or 235 inhabitants 
        per square mile.
        """
    )

