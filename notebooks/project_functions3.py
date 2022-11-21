import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

def load_and_process(url_or_path_to_csv_file):
    df = (
        pd.DataFrame(
            pd.read_csv(url_or_path_to_csv_file)
        )
        .drop(columns=['sex', 'bmi', 'children', 'region'])
        .rename(columns = {'age':'Age', 'smoker':'Smoker','charges':'Total_Charges'})
    )

    df.drop_duplicates(inplace=True)
    df['Smoker'] = df['Smoker'].astype('category') #The original type for this column was 'object' which was checked using the code df.info() 
    df.reset_index()
    return df

def describe(df):
    print(f'The age of the people in this dataset range from {df.Age.min()} to {df.Age.max()} with a mean of {round(df.Age.mean(),1)}.')
    print(f'Total charges for these people range from ${round(df.Total_Charges.min(),2)} to ${round(df.Total_Charges.max(),2)} with a mean of ${round(df.Total_Charges.mean(),2)}.') 
    print(f'There are a total of {df.Smoker.value_counts().yes} smokers and {df.Smoker.value_counts().no} non-smokers in this dataset.')

def removeOutliers(data):
    for x in ['Total Charges']:
        q75,q25 = np.percentile(data.loc[:,x],[75,25])
        iqr = q75-q25

        max = q75+(1.5*iqr)
        min = q25-(1.5*iqr)
 
        lower = data.loc[data[x] < min,x] = np.nan
        lower
        upper = data.loc[data[x] > max,x] = np.nan
        upper
        data.dropna(axis = 0)
    return print(f'Removed all outliers')

