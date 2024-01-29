import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# import seaborn as sns


# Extracting the VC datasets

fundingSeries = ['Series C', 'Venture - Series Unknown', 'Debt Financing', 'Series B',
                 'Initial Coin Offering', 'Series A', 'Undisclosed', 'Seed',
                 'Convertible Note', 'Angel', 'Post-IPO Secondary', 'Series D', 'Corporate Round', 'Grant',
                 'Product Crowdfunding', 'Private Equity',
                 'Post-IPO Equity', 'Equity Crowdfunding', 'Non-equity Assistance',
                 'Pre-Seed', 'nan', 'Series E', 'Secondary Market', 'Post-IPO Debt', 'Series F',
                 'Series G']


for i in fundingSeries:
    i = pd.read_csv(f'./{i}.csv')

st.set_page_config(page_title='Startup Deal Sourcing', page_icon=':bar_chart:', layout='wide')

st.title('Startup Data Analysis')

# Setting the sidebar for the project

with st.sidebar:
    add_selection_box = st.selectbox('Funding Type',
                                     (i for i in fundingSeries))


