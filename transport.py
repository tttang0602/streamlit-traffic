# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 16:04:09 2022

@author: ttang
"""
import streamlit as st
import seaborn as sns

import pandas as pd
from pandas.api.types import is_numeric_dtype
import numpy as np
import matplotlib.pyplot as plt
app_mode = st.sidebar.radio('Select Page',['Home','Crash information','Driver','Victims']) #two pages


    
if app_mode=='Home':
    st.title('Traffic Accident Data Analyze :')  
    st.image('CorRplot.jpeg')
    st.markdown('Dataset :')
    data=pd.read_csv("datacrash.csv",na_values=['NA'], usecols=[0,1, 5,8,10,14,22,23,36,37,38,39,40,42,45,46,47,49,50,52,60,74,75,77,78,79
])
    
    data.rename(columns={"POINT_X": "lon", "POINT_Y": "lat"},inplace = True)

    st.write(data.head())
    st.markdown('Accident by time of the day ')
    nbins=st.slider('Pick your bin size', 10,50)
    fig, ax = plt.subplots()
    ax.hist(data['COLLISION_TIME'], bins=nbins)
    st.pyplot(fig)
    st.bar_chart(data[['CHP_BEAT_TYPE']])
    map_data = pd.DataFrame(data[['lat','lon']])
    #st.write(map_data['lat'].dtypes,np.sum(map_data['lat'].isna()))
    #map_data[map_data[0]==""] = np.NaN
    map_data = map_data.ffill()
    #st.write(map_data['lat'].dtypes,np.sum(map_data['lat'].isna()))

    #st.write(map_data.head())
    st.map(map_data)
elif app_mode == 'Crash information':
    st.image('CorRplot.jpeg')
    dataname = st.selectbox('Pick the data of your interest',['ACCIDENT_YEAR','COLLISION_TIME','NUMBER_KILLED','COLLISION_SEVERITY','DAY_OF_WEEK','PARTY_COUNT','NUMBER_INJURED','PCF_VIOL_CATEGORY'])
    data=pd.read_csv("datacrash.csv",na_values=['NA'], usecols=[0,1, 5,8,10,14,22,23,36,37,38,39,40,42,45,46,47,49,50,52,60,74,75,77,78,79
])
    nbins=st.slider('Pick your bin size', 10,50)
    fig, ax = plt.subplots()
    ax.hist(data[dataname], bins=nbins)
    st.pyplot(fig)
elif app_mode == 'Driver':
    st.image('CorRplot.jpeg')
    data=pd.read_csv("parties.csv",na_values=['NA'])
    dataname = st.selectbox('Pick the data of your interest',['PARTY_AGE','PARTY_SEX','PARTY_SOBRIETY','VEHICLE_YEAR','VEHICLE_MAKE'])
    st.write(data['PARTY_AGE'].dtype)
    data.loc[data['PARTY_AGE']>200,'PARTY_AGE']=np.NaN
    if is_numeric_dtype(data[dataname]):
        nbins=st.slider('Pick your bin size', 10,50)
        fig, ax = plt.subplots()
        ax.hist(data[dataname], bins=nbins)
        st.pyplot(fig)
    else:
        val_count  = data[dataname].value_counts()
        fig = plt.figure(figsize=(10,5))
        sns.barplot(val_count.index, val_count.values, alpha=0.8)
        st.pyplot(fig)        
elif app_mode == 'Victims':
    st.image('CorRplot.jpeg')
    data=pd.read_csv("victims.csv",na_values=['NA'])
    dataname = st.selectbox('Pick the data of your interest',['VICTIM_AGE','VICTIM_SEX','VICTIM_SEATING_POSITION'])
    data.loc[data['VICTIM_AGE']>200,'VICTIM_AGE']=np.NaN
    if is_numeric_dtype(data[dataname]):
        nbins=st.slider('Pick your bin size', 10,50)
        fig, ax = plt.subplots()
        ax.hist(data[dataname], bins=nbins)
        st.pyplot(fig)
    else:
        val_count  = data[dataname].value_counts()
        fig = plt.figure(figsize=(10,5))
        sns.barplot(val_count.index, val_count.values, alpha=0.8)
        #fig.title(dataname)
        #fig.ylabel('y label', fontsize=12)
        #fig.xlabel('x label', fontsize=12)
        # Add figure in streamlit app
        st.pyplot(fig)


