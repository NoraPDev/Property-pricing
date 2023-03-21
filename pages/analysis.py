import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

def OnChange(actual:st.checkbox,other:st.checkbox):
    if actual:
        other.value(False)

st.title('Data Analysis')

data_state=st.text('loading data...')
data=pd.read_pickle('../data/house_prices.pkl')
clean_data = pd.read_pickle('../data/clean_housing_data.pkl')
data_state.text('')


st.header('Correlations')

st.subheader('Correlation matrix')
corelation = pd.read_pickle('../data/correlation_matrix.pkl')
corelation

st.subheader('Correlation heatmap')
corelation['SalePrice']+=1
corelation_hm=px.imshow(corelation,color_continuous_scale=px.colors.diverging.Portland)
corelation_hm

st.subheader('Scatter plots of features with high correlation')

st.set_option('deprecation.showPyplotGlobalUse', False)


fig_1stFlrSF, ax_1stFlrSF = plt.subplots(1, 1)
ax_1stFlrSF.scatter(data['1stFlrSF'],data['SalePrice'],s=1,)
ax_1stFlrSF.set_xlabel('1stFlrSF')
ax_1stFlrSF.set_ylabel('SalePrice')
ax_1stFlrSF.set_title('1stFlrSF')
st.pyplot(fig_1stFlrSF)

fig_GarageArea, ax_GarageArea = plt.subplots(1, 1)
ax_GarageArea.scatter(data['GarageArea'],data['SalePrice'],s=1,)
ax_GarageArea.set_xlabel('GarageArea')
ax_GarageArea.set_ylabel('SalePrice')
ax_GarageArea.set_title('GarageArea')
st.pyplot(fig_GarageArea)

fig_GarageYrBlt, ax_GarageYrBlt = plt.subplots(1, 1)
ax_GarageYrBlt.scatter(data['GarageYrBlt'],data['SalePrice'],s=1,)
ax_GarageYrBlt.set_xlabel('GarageYrBlt')
ax_GarageYrBlt.set_ylabel('SalePrice')
ax_GarageYrBlt.set_title('GarageYrBlt')
st.pyplot(fig_GarageYrBlt)

fig_GrLivArea, ax_GrLivArea = plt.subplots(1, 1)
ax_GrLivArea.scatter(data['GrLivArea'],data['SalePrice'],s=1,)
ax_GrLivArea.set_xlabel('GrLivArea')
ax_GrLivArea.set_ylabel('SalePrice')
ax_GrLivArea.set_title('GrLivArea')
st.pyplot(fig_GrLivArea)

fig_LotArea, ax_LotArea = plt.subplots(1, 1)
ax_LotArea.scatter(data['LotArea'],data['SalePrice'],s=1,)
ax_LotArea.set_xlabel('LotArea')
ax_LotArea.set_ylabel('SalePrice')
ax_LotArea.set_title('LotArea')
st.pyplot(fig_LotArea)

fig_LotFrontage, ax_LotFrontage = plt.subplots(1, 1)
ax_LotFrontage.scatter(data['LotFrontage'],data['SalePrice'],s=1,)
ax_LotFrontage.set_xlabel('LotFrontage')
ax_LotFrontage.set_ylabel('SalePrice')
ax_LotFrontage.set_title('LotFrontage')
st.pyplot(fig_LotFrontage)

fig_MasVnrArea, ax_MasVnrArea = plt.subplots(1, 1)
ax_MasVnrArea.scatter(data['MasVnrArea'],data['SalePrice'],s=1,)
ax_MasVnrArea.set_xlabel('MasVnrArea')
ax_MasVnrArea.set_ylabel('SalePrice')
ax_MasVnrArea.set_title('MasVnrArea')
st.pyplot(fig_MasVnrArea)

fig_OpenPorchSF, ax_OpenPorchSF = plt.subplots(1, 1)
ax_OpenPorchSF.scatter(data['OpenPorchSF'],data['SalePrice'],s=1,)
ax_OpenPorchSF.set_xlabel('OpenPorchSF')
ax_OpenPorchSF.set_ylabel('SalePrice')
ax_OpenPorchSF.set_title('OpenPorchSF')
st.pyplot(fig_OpenPorchSF)

fig_OverallQual, ax_OverallQual = plt.subplots(1, 1)
ax_OverallQual.scatter(data['OverallQual'],data['SalePrice'],s=1,)
ax_OverallQual.set_xlabel('OverallQual')
ax_OverallQual.set_ylabel('SalePrice')
ax_OverallQual.set_title('OverallQual')
st.pyplot(fig_OverallQual)

fig_TotalBsmtSF, ax_TotalBsmtSF = plt.subplots(1, 1)
ax_TotalBsmtSF.scatter(data['TotalBsmtSF'],data['SalePrice'],s=1,)
ax_TotalBsmtSF.set_xlabel('TotalBsmtSF')
ax_TotalBsmtSF.set_ylabel('SalePrice')
ax_TotalBsmtSF.set_title('TotalBsmtSF')
st.pyplot(fig_TotalBsmtSF)

fig_YearBuilt, ax_YearBuilt = plt.subplots(1, 1)
ax_YearBuilt.scatter(data['YearBuilt'],data['SalePrice'],s=1,)
ax_YearBuilt.set_xlabel('YearBuilt')
ax_YearBuilt.set_ylabel('SalePrice')
ax_YearBuilt.set_title('YearBuilt')
st.pyplot(fig_YearBuilt)

fig_YearRemodAdd, ax_YearRemodAdd = plt.subplots(1, 1)
ax_YearRemodAdd.scatter(data['YearRemodAdd'],data['SalePrice'],s=1,)
ax_YearRemodAdd.set_xlabel('YearRemodAdd')
ax_YearRemodAdd.set_ylabel('SalePrice')
ax_YearRemodAdd.set_title('YearRemodAdd')
st.pyplot(fig_YearRemodAdd)

fig_KitchenQual, ax_KitchenQual = plt.subplots(1, 1)
ax_KitchenQual.scatter(data['KitchenQual'],data['SalePrice'],s=1,)
ax_KitchenQual.set_xlabel('KitchenQual')
ax_KitchenQual.set_ylabel('SalePrice')
ax_KitchenQual.set_title('KitchenQual')
st.pyplot(fig_KitchenQual)