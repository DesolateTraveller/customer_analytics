#---------------------------------------------------------------------------------------------------------------------------------
### Import Libraries
#---------------------------------------------------------------------------------------------------------------------------------
import streamlit as st
#import streamlit_authenticator as stauth
#----------------------------------------
import pickle
import os
import time
from random import randint
import warnings
warnings.filterwarnings("ignore")
#from PIL import Image
import json
import holidays
import altair as alt
import base64
import itertools
from datetime import datetime, timedelta, date
#from __future__ import division
from itertools import cycle
from pathlib import Path
#----------------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#----------------------------------------
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import plotly.offline as pyoff
#----------------------------------------
import sweetviz as sv
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
#----------------------------------------
from sklearn.cluster import KMeans
#----------------------------------------
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.model_selection import KFold, cross_val_score, train_test_split
import xgboost as xgb
from sklearn import tree
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from xgboost import XGBClassifier
from xgboost import plot_importance
import optuna.integration.lightgbm as lgb
from sklearn.preprocessing import label_binarize
#----------------------------------------
# Model Performance
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.metrics import roc_auc_score,roc_curve,classification_report,confusion_matrix,accuracy_score,auc
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, RocCurveDisplay, PrecisionRecallDisplay
import shap
from sklearn.feature_selection import SelectKBest, mutual_info_classif, f_classif, f_regression, chi2
#----------------------------------------
# Model Validation
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, cross_val_score
#----------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------
### Title and description for your Streamlit app
#---------------------------------------------------------------------------------------------------------------------------------
#import custom_style()
st.set_page_config(page_title="Customer Lifecycle Management (CLM)",
                   layout="wide",
                   #page_icon=               
                   initial_sidebar_state="collapsed")
#----------------------------------------
st.title("f""":rainbow[Customer Lifecycle Management (CLM) | v1.0]""")
st.markdown('Created by | <a href="mailto:avijit.mba18@gmail.com">Avijit Chakraborty</a>', 
            unsafe_allow_html=True)
st.info('**Disclaimer : :blue[Thank you for visiting the app] | This app is created for internal use, unauthorized uses or copying is strictly prohibited | Please expand the below :blue[Project Description] to know more and click the :blue[sidebar] to follow the instructions to start the applications.**', icon="ℹ️")
#----------------------------------------
# Set the background image
st.divider()
#---------------------------------------------------------------------------------------------------------------------------------
### User Authentication
#---------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------
### Feature Import
#---------------------------------------------------------------------------------------------------------------------------------
st.sidebar.info('Please upload the data to start the application.', icon="ℹ️")
# Upload a CSV file
df = pd.DataFrame()
#----------------------------------------
st.sidebar.header("**1. Data (Customer)**", divider='blue')
data_source = st.sidebar.radio("**1.1 Select Data Source**", ["Upload", "Server Path"],key='1.1')

if data_source == "Upload":
    file1 = st.sidebar.file_uploader("**1.2 Choose a file**",
                                type=["xlsx","csv"],
                                accept_multiple_files=True,
                                key=0)
    for file1 in file1:
        df = pd.read_csv(file1)
        df_npd = df.copy()

#----------------------------------------
st.sidebar.header("**2. Data (Churn)**", divider='blue')
data_source = st.sidebar.radio("**2.1 Select Data Source**", ["Upload", "Server Path"],key='2.1')

if data_source == "Upload":
    file2 = st.sidebar.file_uploader("**2.2 Choose a file**",
                                type=["xlsx","csv"],
                                accept_multiple_files=True,
                                key=1)
    for file2 in file2:
        #if file2 is not None:
        df1 = pd.read_csv(file2)

#----------------------------------------
st.sidebar.header("**3. Data (Sales)**", divider='blue')
data_source = st.sidebar.radio("**3.1 Select Data Source**", ["Upload", "Server Path"],key='3.1')

if data_source == "Upload":
    file3 = st.sidebar.file_uploader("**3.2 Choose a file**",
                                type=["xlsx","csv"],
                                accept_multiple_files=True,
                                key=2)
    for file3 in file3:
        #if file3 is not None:
            df2 = pd.read_csv(file3) 

#----------------------------------------
st.sidebar.header("**4. Data (Market Response)**", divider='blue')
data_source = st.sidebar.radio("**4.1 Select Data Source**", ["Upload", "Server Path"],key='4.1')

if data_source == "Upload":
    file4 = st.sidebar.file_uploader("**4.2 Choose a file**",
                                type=["xlsx","csv"],
                                accept_multiple_files=True,
                                key=3)
    for file4 in file4:
        #if file4 is not None:
        df3 = pd.read_csv(file4) 
        df3_um = df3.copy()

#---------------------------------------------------------------------------------------------------------------------------------
        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12 = st.tabs(["**Information**",
                                                                       "**Input**",
                                                                       "**KPI & Metrices**",
                                                                       "**Segmentation**",
                                                                       "**Customer Lifetime Value (CLV)**", 
                                                                       "**Churn**", 
                                                                       "**Next Purchase Day**",
                                                                       "**Sales**",
                                                                       "**Market Response Models**", 
                                                                       "**Uplift Modelling**",
                                                                       "**A/B Testing**", 
                                                                       "**Result**" ])

#---------------------------------------------------------------------------------------------------------------------------------
### Informations
#---------------------------------------------------------------------------------------------------------------------------------
        with tab1:

            st.subheader("**1. Basic Project Information**", divider='blue')
            st.warning('''
                    '**Data Driven Growth**' 
                    - It makes a strategic decisions based on predictive analysis of data and its interpretation. 
                    - It is designed to explain how to use Python in a simplistic way to fuel the growth by applying the predictive approach to all your actions. 
                ''')
            
            st.divider()
            #------------------------------------------------------------------------------------------------------------------------------------------
            st.subheader("**2. Projcet KPI & Metrices**", divider='blue')
            st.warning('''
                        '**North Star Metric**' | A North Star metric is the one measurement that’s most predictive of a company’s long-term success by capturing the core values. 
                    ''')
            
            col1, col2, col3 = st.columns(3)
            with col1:

                st.write('''
                        To qualify as a “**North Star**” a metric must do three things: 

                        1. **Lead to revenue**
                        2. **Reflect customer value** and
                        3. **Measure progress**
                        ''')

            with col2:
                st.write('''
                        Major and Important Metrics which can generate from ‘**North Star metrics**’ :

                        - **New Customer Ratio :** It shows the customer trend based out of the services/products (Indication of growth/decline).
                        - **Retention Rate :** 	   It shows customer's stickiness about the services/product related to trend and also shows the **PMF(Product Market Fit)**.   
                        - **Cohort Retention Rate :** 	   It shows percentage(%) of customer's stickiness after first purchase.                 
                        ''')

            with col3:
                    st.write('''
                            We have all the crucial information we need:

                            1. **Customer ID**
                            2. **Unit Price**
                            3. **Quantity**
                            4. **Invoice Date**
 
                            With all these features, we can build our **North Star Metric** equation: 
                            ''')
                    st.info('''
                            **Revenue = Active Customer Count x Order Count x Average Revenue per Order**
                            ''')
            st.divider()
            #------------------------------------------------------------------------------------------------------------------------------------------
            st.subheader("**3. Segmentation**", divider='blue')
            st.warning('''
                **Customer Segmentation – “R (recency) – F (Frequency) – M (Monetary)” Value** | To increase the retention rate of the customer, do segment the customer based on churn probability and took actions accordingly.
                ''')

            col1, col2 = st.columns(2)
            with col1:
                st.write('''
                        **RFM** stands for **Recency - Frequency - Monetary Value**. 

                        - **R – Recency :** -     How recent customer was purchased.
                        - **F – Frequency :** -   How frequent customer was purchased. 
                        - **M – Monetary :** -    How much amount was spent by customer.
                        ''')

            with col2:
                st.write('''
                        Theoretically we will have segments like below:

                        - **Low Value:** Customers who are less active than others, not very frequent buyer/visitor and generates very low - zero - maybe negative revenue.
                        - **Mid Value:** In the middle of everything. Often using our platform (but not as much as our High Values), fairly frequent and generates moderate revenue.
                        - **High Value:** The group we don’t want to lose. High Revenue, Frequency and low Inactivity.
                        ''')

            st.divider()
            #------------------------------------------------------------------------------------------------------------------------------------------
            st.subheader("**4. Customer Lifetime Value (CLV)**", divider='blue')
            st.warning('''
                    **Customer Lifetime Value (CLV)** | One of the most important metric & it segment the customers and found out who are the best ones.
                    ''')
            col1, col2 = st.columns(2)

            with col1:

                st.write('''
                        - We invest in customers to generate revenue and be profitable. 
                        - Naturally, these actions make some customers super valuable in terms of lifetime value but there are always some customers who pull down the profitability. 
                        - We need to identify these behavior patterns, segment customers and act accordingly.
                        ''')

            with col2:

                st.info('''
                    - **Lifetime Value (LTV)            = Avg. Value of Sales (A) x No. of Transactions (T) x Retention Period (R)**
                    - **Customer Lifetime Value (CLV)   = Lifetime Value (LTV) x Profit Margin (M)** 
                    - **Lifetime Value OverallScore     = Recency Cluster + Frequency Cluster + Monetary Cluster**
                
                    **Lifetime Value Cluster (LTVCluster):** 
                    - **OverallScore <2 - Low (0)** 
                    - **2> OverallScore <4 - Mid (1)** 
                    - **OverallScore >4 - High (2)** 
                    ''')

            st.divider()
            #------------------------------------------------------------------------------------------------------------------------------------------
            st.subheader("**5. Customer Churn**", divider='blue')
            st.warning('''
                    '**Churn(Retention Rate)**' | Indicatior of the **PMF (Product Market Fit)**
                    ''')
            col1, col2 = st.columns(2)
            with col1:

                st.write('''
                        - It increase retention rate & **PMF (Product Market Fit)**.
                        - It Chanellize the customers based on its LTV. 
                        - It is the primary growth pillars for products with a subscription-based business model.
                        - It is the health indicator for businesses whose customers are subscribers and paying for services on a recurring basis     
                        ''')

            with col2:

                    st.info('''
                        Consider for this analysis :
 
                        - **1. 'Churn' customer       - '1'**
                        - **2. 'Non-Churn' customer   - '0'**
                        ''')

            st.divider()
            #------------------------------------------------------------------------------------------------------------------------------------------
            st.subheader("**6. Next Purchase Day**", divider='blue')
            st.warning('''
                        '**Next Purchase Day**' | Based on customer's CLV, need to find the next purchase day.
                    ''')
            col1, col2 = st.columns(2)
            with col1:

                st.info('''
            
                        **Next Purchase Day Range:** 
                        - **0–20: Customers that will purchase in 0–20 days — Class name: 2** 
                        - **21–49: Customers that will purchase in 21–49 days — Class name: 1** 
                        - **≥ 50: Customers that will purchase in more than 50 days — Class name: 0** 
                        ''')

            with col2 :

                st.info('''
        
                        **Next Purchase Day Segment:** 
                
                        **Segment OverallScore = Recency Cluster + Frequency Cluster + Monetary Cluster**
                
                        - **OverallScore <2 - Low (0)** 
                        - **2> OverallScore <4 - Mid (1)** 
                        - **OverallScore >4 - High (2)** 
                        ''')
    
            st.divider()
            #----------------------------------------------------------------------
            st.subheader("**7. Sales**", divider='blue')
            st.warning('''
                        '**Prediction of Sales**' | Predict the broader picture of the sales considering all of our effects from customer side.
                        ''')            
#--------------------------------
