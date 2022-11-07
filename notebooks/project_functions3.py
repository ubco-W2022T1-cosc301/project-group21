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
        .rename(columns = {'age':'Age', 'smoker':'Smoker','charges':'Total Charges'})
    )

    df.drop_duplicates
    df['Total Charges'] = df['Total Charges'].round(decimals = 2)
    df['Smoker'] = df['Smoker'].astype('category')
    df.reset_index(drop=True)
    
    return df


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


def final_graphs (data):
    
    plot1 = sns.barplot(data=data, x="Smoker", y="Total Charges", errorbar=("se"))
    plt.title('Medical Insurance Bills for Smokers and Non-Smokers')

    plot2 = data.plot(kind = 'scatter', x = 'Age', y = 'Total Charges')
    plt.title('Increasing Age and Medical Insurance Bills')
    
    return plot1, plot2