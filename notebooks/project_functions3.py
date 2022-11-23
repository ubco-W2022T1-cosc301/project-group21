import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
import project_functions3 as p3
import statistics

def load_and_process(url_or_path_to_csv_file):
    df = (
        pd.DataFrame(
            pd.read_csv(url_or_path_to_csv_file)
        )
        .drop(columns=['sex', 'bmi', 'children', 'region'])
        .rename(columns = {'age':'Age', 'smoker':'Smoker','charges':'Total_Charges'})
    )

    df['Total_Charges'] = round(df.Total_Charges,2)
    df.drop_duplicates(inplace=True)
    df['Smoker'] = df['Smoker'].astype('category') #The original type for this column was 'object' which was checked using the code df.info() 
    df.reset_index()
    return df



def describe(df):
    print(f'The age of the people in this dataset range from {df.Age.min()} to {df.Age.max()} with a mean of {round(df.Age.mean(),1)}.')
    print(f'Total charges for these people range from ${round(df.Total_Charges.min(),2)} to ${round(df.Total_Charges.max(),2)} with a mean of ${round(df.Total_Charges.mean(),2)}.') 
    print(f'There are a total of {df.Smoker.value_counts().yes} smokers and {df.Smoker.value_counts().no} non-smokers in this dataset.')

    
    
def null(data):
    if data.isnull().any(axis=None):
        print("\nPreview of data with null values:\nxxxxxxxxxxxxx")
        print(data[data.isnull().any(axis=1)])
        missingno.matrix(data)
        plt.show()
    else: 
        print("There are no null values in this dataset")
        
        

def removeOutliers(data):
    mean = data['Total_Charges'].mean()
    sd = round(statistics.stdev(data['Total_Charges']),2)
    upper = mean + sd * 3
    lower = mean - sd * 3
    new = data[data['Total_Charges'].between(lower,upper)].reset_index().drop(columns = "index")
    return new