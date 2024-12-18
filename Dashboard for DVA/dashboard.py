import streamlit as st
import plotly.express as px
import pandas as pd
import os

st.set_page_config(page_title="Crop Yield Analysis", page_icon=":bar_chart:", layout="wide")

st.title(" :bar_chart: Crop Yield Analysis")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

# File uploader
fl = st.file_uploader(":file_folder: Upload a file", type=["csv", "txt", "xlsx", "xls"])
if fl is not None:
    df = pd.read_csv(fl)
else:
    # Path to your CSV file
    df = pd.read_csv("/Users/pravinkumar/Documents/DVA/Dashboard for DVA/yield_df.csv")

col1, col2 = st.columns((2))

# Convert 'Year' to datetime format
df['Year'] = pd.to_datetime(df['Year'], format='%Y')

# Get the minimum and maximum years
start_year = df['Year'].min().year
end_year = df['Year'].max().year

with col1:
    year1 = st.slider("Select Start Year", min_value=start_year, max_value=end_year, value=start_year)

with col2:
    year2 = st.slider("Select End Year", min_value=start_year, max_value=end_year, value=end_year)

# Filter the data based on the selected years
df = df[(df['Year'].dt.year >= year1) & (df['Year'].dt.year <= year2)]

# Sidebar filters
st.sidebar.header("Filter Options:")
# Filter by Area (Region)
area = st.sidebar.multiselect("Pick an Area", df['Area'].unique())
if not area:
    df_filtered = df.copy()
else:
    df_filtered = df[df['Area'].isin(area)]

# Filter by Crop Type
item = st.sidebar.multiselect("Pick the Crop Type", df_filtered['Item'].unique())
if not item:
    df_filtered = df_filtered.copy()
else:
    df_filtered = df_filtered[df_filtered['Item'].isin(item)]

# Crop-wise yield (Bar Chart)
crop_df = df_filtered.groupby(by=['Item'], as_index=False)['hg/ha_yield'].sum()

with col1:
    st.subheader("Yield by Crop Type")
    fig = px.bar(crop_df, x='Item', y='hg/ha_yield', text=[f'{x:,.2f}' for x in crop_df['hg/ha_yield']], template='seaborn')
    st.plotly_chart(fig, use_container_width=True)

# Treemap for Region-wise analysis
region_df = df_filtered.groupby(by=['Area'], as_index=False)['hg/ha_yield'].sum()

with col2:
    st.subheader("Yield by Region (Treemap)")
    fig = px.treemap(region_df, path=['Area'], values='hg/ha_yield',
                     color='hg/ha_yield', hover_data=['hg/ha_yield'], title="Treemap for Yield by Region")
    st.plotly_chart(fig, use_container_width=True)

# Time series analysis for yield
df_filtered['year_period'] = df_filtered['Year'].dt.to_period('Y').astype(str)  # Convert Period to string
time_series_df = df_filtered.groupby('year_period')['hg/ha_yield'].sum().reset_index()

st.subheader('Time Series Analysis of Yield')
fig2 = px.line(time_series_df, x='year_period', y='hg/ha_yield', labels={'hg/ha_yield': 'Yield (hg/ha)'}, template='gridon')
st.plotly_chart(fig2, use_container_width=True)

# Hierarchical view of yield (TreeMap for Region and Crop)
st.subheader("Hierarchical View of Yield by Region and Crop")
fig3 = px.treemap(df_filtered, path=['Area', 'Item'], values='hg/ha_yield', hover_data=['hg/ha_yield'], color='Item')
st.plotly_chart(fig3, use_container_width=True)