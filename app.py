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
        location_data, lat="Latitude", lon="Longitude", zoom=4,
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
MIMAROPA = 'data/MIMAROPA.csv'
Region_5 = 'data/Region 5.csv'
Region_6 = 'data/Region 6.csv'
Region_7 = 'data/Region 7.csv'
Region_8 = 'data/Region 8.csv'
Region_9 = 'data/Region 9.csv'
Region_10 = 'data/Region 10.csv'
Region_11 = 'data/Region 11.csv'
Region_12 = 'data/Region 12.csv'
Region_13 = 'data/Region 13.csv'
NCR = 'data/NCR.csv'
CAR = 'data/CAR.csv'
BARMM = 'data/BARMM.csv'
All = 'data/All.csv'

#Filter by Region
st.header('Select a Region')
selected_region = st.selectbox('Regions:', 
                               ('All','Region I – Ilocos Region', 'Region II – Cagayan Valley', 'Region III – Central Luzon', 
                                'Region IV‑A – CALABARZON', 'MIMAROPA Region', 'Region V – Bicol Region',
                                'Region VI – Western Visayas', 'Region VII – Central Visayas', 'Region VIII – Eastern Visayas',
                                'Region IX – Zamboanga Peninsula', 'Region X – Northern Mindanao', 'Region XI – Davao Region',
                                'Region XII – SOCCSKSARGEN', 'Region XIII – Caraga', 'NCR – National Capital Region', 
                                'CAR – Cordillera Administrative Region', 'BARMM – Bangsamoro Autonomous Region in Muslim Mindanao'))


if selected_region == 'All':
    df = pd.read_csv(All, 
                     usecols=['Name', 'Population', 'Latitude', 'Longitude'])
    df.columns = ['Name', 'Population', 'Latitude', 'Longitude']
    px_map = display_map(df)
    st.plotly_chart(px_map, use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>Regions of the Philippines</h2>", unsafe_allow_html=True)
    st.write(
        """
        The Philippines is subdivided into seventeen (17) regions – eight (8) in Luzon, three (3) in the Visayas, and six (6) in Mindanao. These regions are not local 
        government units but their existence is primarily for administrative purposes. Thus in each region, a city is designated as the center where each of the 
        national government agencies have a regional office.

        Based on the 2020 census, the regions with the highest population are, in descending order, :violet[_CALABARZON_] (16,195,042), the :violet[_National Capital Region_] (13,484,462), 
        and :violet[_Central Luzon_] (12,422,172). Almost 40 percent of the national population are found in these three (3) regions alone. The least populated regions are, :violet[_Cordillera 
        Administrative Region_] (1,797,660), :violet[_Caraga_] (2,804,788), and :violet[_MIMAROPA Region_] (3,228,558) whose combined populations account for less than 10 percent of the national count.
        """
    )
    data = [
    ["Region", "Population (2020)", "Province count", "City count", "Mun. count", "Bgy. count", "Border type", "Island group"],
    ["Ilocos Region (Region I)", 5301139, 4, 9, 116, 3267, "coastal", "Luzon"],
    ["Cagayan Valley (Region II)", 3685744, 5, 4, 89, 2311, "coastal", "Luzon"],
    ["Central Luzon (Region III)", 12422172, 7, 14, 116, 3102, "coastal", "Luzon"],
    ["CALABARZON (Region IV-A)", 16195042, 5, 20, 122, 4019, "coastal", "Luzon"],
    ["Bicol Region (Region V)", 6082165, 6, 7, 107, 3471, "coastal", "Luzon"],
    ["Western Visayas (Region VI)", 7954723, 6, 16, 117, 4051, "coastal", "Visayas"],
    ["Central Visayas (Region VII)", 8081988, 4, 16, 116, 3003, "coastal", "Visayas"],
    ["Eastern Visayas (Region VIII)", 4547150, 6, 7, 136, 4390, "coastal", "Visayas"],
    ["Zamboanga Peninsula (Region IX)", 3875576, 3, 5, 67, 1904, "coastal", "Mindanao"],
    ["Northern Mindanao (Region X)", 5022768, 5, 9, 84, 2022, "coastal", "Mindanao"],
    ["Davao Region (Region XI)", 5243536, 5, 6, 43, 1162, "coastal", "Mindanao"],
    ["SOCCSKSARGEN (Region XII)", 4901486, 4, 5, 45, 1195, "coastal", "Mindanao"],
    ["National Capital Region (NCR)", 13484462, 0, 16, 1, 1710, "coastal", "Luzon"],
    ["Cordillera Administrative Region (CAR)", 1797660, 6, 2, 75, 1178, "landlocked", "Luzon"],
    ["Bangsamoro Autonomous Region in Muslim Mindanao (BARMM)", 4404288, 5, 2, 116, 2490, "coastal", "Mindanao"],
    ["Caraga (Region XIII)", 2804788, 5, 6, 67, 1311, "coastal", "Mindanao"],
    ["MIMAROPA Region", 3228558, 5, 2, 71, 1460, "coastal", "Luzon"]
    ]
    
    region_stats = "|".join(data[0]) + "\n" + "|".join(["---"] * len(data[0])) + "\n"
    region_stats += "\n".join("|".join(map(str, row)) for row in data[1:])

    st.markdown(region_stats)

elif selected_region == 'Region I – Ilocos Region':
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

elif selected_region == 'MIMAROPA Region':
    df = pd.read_csv(MIMAROPA, 
                     usecols=['Name', 'Population', 'Latitude', 'Longitude'])
    df.columns = ['Name', 'Population', 'Latitude', 'Longitude']
    px_map = display_map(df)
    st.plotly_chart(px_map, use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>MIMAROPA Region</h2>", unsafe_allow_html=True)
    #st.markdown("<h3 style='text-align: center;'>MIMAROPA</h3>", unsafe_allow_html=True)
    st.write(
        """
        MIMAROPA Region is an administrative region in the Philippines grouped under the Luzon island group. It covers 5 provinces, namely, Marinduque, Occidental Mindoro, 
        Oriental Mindoro, Palawan, and Romblon, as well as 1 highly urbanized city. The regional center is the City of Calapan.

        Its :blue[population] as determined by the 2020 Census was :blue[3,228,558]. This represented 5.19% of the overall population of the Luzon island group, or 2.96% of the entire 
        population of the Philippines. Based on these figures, the population density is computed at 109 inhabitants per square kilometer or 282 inhabitants per square mile.
        """
    )

elif selected_region == 'Region V – Bicol Region':
    df = pd.read_csv(Region_5, 
                     usecols=['Name', 'Population', 'Latitude', 'Longitude'])
    df.columns = ['Name', 'Population', 'Latitude', 'Longitude']
    px_map = display_map(df)
    st.plotly_chart(px_map, use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>Bicol Region</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Region V</h3>", unsafe_allow_html=True)
    st.write(
        """
        Bicol Region, officially designated as Region V, is an administrative region in the Philippines grouped under the Luzon island group. It covers 6 provinces, 
        namely, Albay, Camarines Norte, Camarines Sur, Catanduanes, Masbate, and Sorsogon. The regional center is the City of Legazpi.

        Its :blue[population] as determined by the 2020 Census was :blue[6,082,165]. This represented 9.78% of the overall population of the Luzon island group, or 5.58% of the entire 
        population of the Philippines. Based on these figures, the population density is computed at 336 inhabitants per square kilometer or 870 inhabitants per square mile.
        """
    )

elif selected_region == 'Region VI – Western Visayas':
    df = pd.read_csv(Region_6, 
                     usecols=['Name', 'Population', 'Latitude', 'Longitude'])
    df.columns = ['Name', 'Population', 'Latitude', 'Longitude']
    px_map = display_map(df)
    st.plotly_chart(px_map, use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>Western Visayas</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Region VI</h3>", unsafe_allow_html=True)
    st.write(
        """
        Western Visayas, officially designated as Region VI, is an administrative region in the Philippines occupying the western section of the Visayas. It covers 6 provinces, 
        namely, Aklan, Antique, Capiz, Guimaras, Iloilo, and Negros Occidental, as well as 2 highly urbanized cities. The regional center is the City of Iloilo.

        Its :blue[population] as determined by the 2020 Census was :blue[7,954,723]. This represented 38.65% of the overall population of the Visayas island group, or 7.30% of the entire 
        population of the Philippines. Based on these figures, the population density is computed at 383 inhabitants per square kilometer or 992 inhabitants per square mile.
        """
    )

elif selected_region == 'Region VII – Central Visayas':
    df = pd.read_csv(Region_7, 
                     usecols=['Name', 'Population', 'Latitude', 'Longitude'])
    df.columns = ['Name', 'Population', 'Latitude', 'Longitude']
    px_map = display_map(df)
    st.plotly_chart(px_map, use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>Central Visayas</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Region VII</h3>", unsafe_allow_html=True)
    st.write(
        """
        Central Visayas, officially designated as Region VII, is an administrative region in the Philippines occupying the central section of the Visayas. It covers 4 provinces, 
        namely, Bohol, Cebu, Negros Oriental, and Siquijor, as well as 3 highly urbanized cities. The regional center is the City of Cebu.

        Its :blue[population] as determined by the 2020 Census was :blue[8,081,988]. This represented 39.26% of the overall population of the Visayas island group, or 7.41% of the entire 
        population of the Philippines. Based on these figures, the population density is computed at 509 inhabitants per square kilometer or 1,319 inhabitants per square mile.
        """
    )

elif selected_region == 'Region VIII – Eastern Visayas':
    df = pd.read_csv(Region_8, 
                     usecols=['Name', 'Population', 'Latitude', 'Longitude'])
    df.columns = ['Name', 'Population', 'Latitude', 'Longitude']
    px_map = display_map(df)
    st.plotly_chart(px_map, use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>Eastern Visayas</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Region VIII</h3>", unsafe_allow_html=True)
    st.write(
        """
        Eastern Visayas, officially designated as Region VIII, is an administrative region in the Philippines occupying the eastern section of the Visayas. It covers 6 provinces, 
        namely, Biliran, Eastern Samar, Leyte, Northern Samar, Samar, and Southern Leyte, as well as 1 highly urbanized city. The regional center is the City of Tacloban.

        Its :blue[population] as determined by the 2020 Census was :blue[4,547,150]. This represented 22.09% of the overall population of the Visayas island group, or 4.17% of the entire 
        population of the Philippines. Based on these figures, the population density is computed at 196 inhabitants per square kilometer or 507 inhabitants per square mile.
        """
    )

elif selected_region == 'Region IX – Zamboanga Peninsula':
    df = pd.read_csv(Region_9, 
                     usecols=['Name', 'Population', 'Latitude', 'Longitude'])
    df.columns = ['Name', 'Population', 'Latitude', 'Longitude']
    px_map = display_map(df)
    st.plotly_chart(px_map, use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>Zamboanga Peninsula</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Region IX</h3>", unsafe_allow_html=True)
    st.write(
        """
        Zamboanga Peninsula, officially designated as Region IX, is an administrative region in the Philippines occupying the western section of Mindanao. It covers 3 provinces, 
        namely, Zamboanga del Norte, Zamboanga del Sur, and Zamboanga Sibugay, as well as 1 highly urbanized city (Zamboanga City) and the component city of Isabela. 
        The regional center is the City of Pagadian.

        Its :blue[population] as determined by the 2020 Census was :blue[3,875,576]. This represented 14.76% of the overall population of the Mindanao island group, or 3.55% of the 
        entire population of the Philippines. Based on these figures, the population density is computed at 229 inhabitants per square kilometer or 594 inhabitants 
        per square mile.
        """
    )

elif selected_region == 'Region X – Northern Mindanao':
    df = pd.read_csv(Region_10, 
                     usecols=['Name', 'Population', 'Latitude', 'Longitude'])
    df.columns = ['Name', 'Population', 'Latitude', 'Longitude']
    px_map = display_map(df)
    st.plotly_chart(px_map, use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>Northern Mindanao</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Region X</h3>", unsafe_allow_html=True)
    st.write(
        """
        Northern Mindanao, officially designated as Region X, is an administrative region in the Philippines occupying the northern-central section of Mindanao. 
        It covers 5 provinces, namely, Bukidnon, Camiguin, Lanao del Norte, Misamis Occidental, and Misamis Oriental, as well as 2 highly urbanized cities. 
        The regional center is the City of Cagayan de Oro.

        Its :blue[population] as determined by the 2020 Census was :blue[5,022,768]. This represented 19.13% of the overall population of the Mindanao island group, or 
        4.61% of the entire population of the Philippines. Based on these figures, the population density is computed at 246 inhabitants per square kilometer or 
        636 inhabitants per square mile.
        """
    )

elif selected_region == 'Region XI – Davao Region':
    df = pd.read_csv(Region_11, 
                     usecols=['Name', 'Population', 'Latitude', 'Longitude'])
    df.columns = ['Name', 'Population', 'Latitude', 'Longitude']
    px_map = display_map(df)
    st.plotly_chart(px_map, use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>Davao Region</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Region XI</h3>", unsafe_allow_html=True)
    st.write(
        """
        Davao Region, officially designated as Region XI, is an administrative region in the Philippines occupying the southeastern section of Mindanao. It covers 5 provinces, 
        namely, Davao de Oro (Compostela Valley), Davao del Norte, Davao del Sur, Davao Occidental, and Davao Oriental, as well as 1 highly urbanized city. 
        The regional center is the City of Davao.

        Its :blue[population] as determined by the 2020 Census was :blue[5,243,536]. This represented 19.97% of the overall population of the Mindanao island group, or 
        4.81% of the entire population of the Philippines. Based on these figures, the population density is computed at 257 inhabitants per square kilometer 
        or 665 inhabitants per square mile.
        """
    )

elif selected_region == 'Region XII – SOCCSKSARGEN':
    df = pd.read_csv(Region_12, 
                     usecols=['Name', 'Population', 'Latitude', 'Longitude'])
    df.columns = ['Name', 'Population', 'Latitude', 'Longitude']
    px_map = display_map(df)
    st.plotly_chart(px_map, use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>SOCCSKSARGEN</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Region XII</h3>", unsafe_allow_html=True)
    st.write(
        """
        SOCCSKSARGEN, officially designated as Region XII, is an administrative region in the Philippines occupying the southern-central section of Mindanao. 
        It covers 4 provinces, namely, Cotabato, Sarangani, South Cotabato, and Sultan Kudarat, as well as 1 highly urbanized city (General Santos) and 
        the independent component city of Cotabato. The regional center is the City of Koronadal.

        Its :blue[population] as determined by the 2020 Census was :blue[4,901,486]. This represented 18.67% of the overall population of the Mindanao island group, 
        or 4.50% of the entire population of the Philippines. Based on these figures, the population density is computed at 215 inhabitants per square kilometer or
        557 inhabitants per square mile.
        """
    )

elif selected_region == 'Region XIII – Caraga':
    df = pd.read_csv(Region_13, 
                     usecols=['Name', 'Population', 'Latitude', 'Longitude'])
    df.columns = ['Name', 'Population', 'Latitude', 'Longitude']
    px_map = display_map(df)
    st.plotly_chart(px_map, use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>Caraga</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Region XIII</h3>", unsafe_allow_html=True)
    st.write(
        """
        Caraga, officially designated as Region XIII, is an administrative region in the Philippines occupying the northeastern section of Mindanao. It covers 5 
        provinces, namely, Agusan del Norte, Agusan del Sur, Dinagat Islands, Surigao del Norte, and Surigao del Sur, as well as 1 highly urbanized city. 
        The regional center is the City of Butuan.

        Its :blue[population] as determined by the 2020 Census was :blue[2,804,788]. This represented 10.68% of the overall population of the Mindanao island group, 
        or 2.57% of the entire population of the Philippines. Based on these figures, the population density is computed at 133 inhabitants per square kilometer 
        or 344 inhabitants per square mile.
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

elif selected_region == 'BARMM – Bangsamoro Autonomous Region in Muslim Mindanao':
    df = pd.read_csv(BARMM, 
                     usecols=['Name', 'Population', 'Latitude', 'Longitude'])
    df.columns = ['Name', 'Population', 'Latitude', 'Longitude']
    px_map = display_map(df)
    st.plotly_chart(px_map, use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>Bangsamoro Autonomous Region in Muslim Mindanao</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>(CAR)</h3>", unsafe_allow_html=True)
    st.write(
        """
        Bangsamoro Autonomous Region in Muslim Mindanao, officially designated as BARMM, is an administrative region in the Philippines grouped under the Mindanao island group. 
        It covers 5 provinces, namely, Basilan, Lanao del Sur, Maguindanao, Sulu, and Tawi‑Tawi. The regional center is the City of Cotabato.

        Its :blue[population] as determined by the 2020 Census was :blue[4,404,288]. This represented 16.78% of the overall population of the Mindanao island group, 
        or 4.04% of the entire population of the Philippines. Based on these figures, the population density is computed at 120 inhabitants per square kilometer or 311 
        inhabitants per square mile.
        """
    )