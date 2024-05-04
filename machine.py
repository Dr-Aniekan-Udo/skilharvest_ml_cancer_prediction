import pandas as pd
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
import pickle as pk
import warnings
import streamlit as st
warnings.filterwarnings("ignore")

selected = ['radius_mean', 'texture_mean', 'perimeter_mean',
       'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',
       'concave points_mean', 'symmetry_mean', 'radius_se', 'perimeter_se',
       'area_se', 'concave points_se', 'radius_worst', 'texture_worst',
       'perimeter_worst', 'area_worst', 'smoothness_worst',
       'compactness_worst', 'concavity_worst', 'concave points_worst',
       'symmetry_worst', 'fractal_dimension_worst']

def execute(file):    
    x_scale = sc.fit_transform(file)
    data = pd.DataFrame(x_scale,columns=[file.columns])
    result = model(data)
    if result ==[0]:
        p = 'Benign'
    elif result==[1]:
        p ='Malignant'
    return p

@st.cache_resource
def model(data):
    svm_model=pk.load(open(r'C:\Users\anibr\Desktop\skillharvest\final\cancer_svm.pkl','rb'))
    result=svm_model.predict(data)
    return result


