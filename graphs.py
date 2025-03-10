import streamlit as st
import pandas as pd
import numpy as np

st.title('About Project')
st.subheader('Model - Random Forest')
st.markdown('''
Random Forest Regression is a powerful and versatile machine learning algorithm that is often used for predictive modeling tasks. Random Forest Regression builds many different decision trees using random subsets of data and features, then combines their predictions by averaging them to get the final result. This makes the model robust and accurate.
''')
st.image('images/randomforest.png')
st.markdown('''
Reasons to use Random Forest Regression model:
1. Reduces Overfitting:
By averaging the predictions of multiple decision trees (ensemble method), Random Forest reduces the risk of overfitting compared to a single decision tree. The use of bootstrapping and feature randomness further helps in generalizing the model.

2. No Need for Feature Scaling:
Random Forest does not require feature scaling (normalization or standardization) because it is based on decision trees, which are not sensitive to the scale of the input features.

3. Handles High Dimensionality:
Random Forest can handle datasets with a large number of features, even if some of them are irrelevant. It automatically selects a subset of features for each tree, which helps in dealing with high-dimensional data.
''')

st.subheader('Accuracy of Model')
st.markdown('''
This plot helps you assess how well the model's predictions match the actual values. Ideally, the points should be closer to a 45-degree diagonal line, indicating that the predicted values are close to the actual values.

If most of the points are near the diagonal line, the model has performed well.
''')
st.image('images/download.png')

st.subheader('Data Visualization')
data = pd.read_csv('cleanedData.csv')
tab1, tab2, tab3 = st.tabs(["Tourism over Time vs Region", "Tourism over Time vs Prupose", "Tourism over Time vs Mode of Travel"])
with tab1:
    column = ['FromAfrica', 'FromEastAsiaandthePacific', 'FromEurope', 'FromSouthAsia']
    st.line_chart(
        data,
        x="year",
        y=column
    )

with tab2:
    column = ['Personal(Visit)', 'BusinessAndProfessional(Visit)']
    st.line_chart(
        data,
        x="year",
        y=column
    )

with tab3:
    column = ['Air(Travel)', 'Land(Travel)']
    st.line_chart(
        data,
        x="year",
        y=column
    )