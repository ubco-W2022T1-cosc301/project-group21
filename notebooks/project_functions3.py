import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

def load_and_process(url_or_path_to_csv_file):
    dfMain = (
        pd.read_csv(url_or_path_to_csv_file)
    )
    print(dfMain)
    return dfMain

def cleaned_df(dfMain) :   
    dfNew = (   
        dfMain
        .drop(columns=['sex', 'bmi', 'children', 'region'])
        .rename(columns = {'age':'Age', 'smoker':'Smoker','charges':'Total Charges'}, inplace = True)
        .dfMain.drop_duplicates(inplace=True)
        .dfMain['Total Charges'].round(decimals = 2)
        .dfMain['Smoker'].astype('category')
        .dfMain.reset_index(drop=True)
    )
    
    dfNew.plot(kind = 'scatter', x = 'Age', y = 'Total Charges')
    
    sns.barplot(data=dfNew, x="Smoker", y="Total Charges", errorbar=("se"))
    
    return dfNew

def RemoveOutliers (data):
    for x in ['Total Charges']:
        q75,q25 = np.percentile(dfNew.loc[:,x],[75,25])
        iqr = q75-q25

        max = q75+(1.5*iqr)
        min = q25-(1.5*iqr)
 
        dfNew.loc[dfNew[x] < min,x] = np.nan
        dfNew.loc[dfNew[x] > max,x] = np.nan
        dfNew.dropna(axis = 0)


