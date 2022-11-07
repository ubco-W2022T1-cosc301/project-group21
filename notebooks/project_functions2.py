import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_process(url_or_path_to_csv_file):
    
    # Method Chain 1 (load data and drop unwanted columns)
    
    df1 = (
        pd.DataFrame(
            pd.read_csv(url_or_path_to_csv_file)
        )
        .copy().drop(['sex','children','smoker','region'],axis=1)
    )
    
    # Method Chain 2 (localise data)
    
    df2 = (
        pd.DataFrame(df1)
        .loc[lambda x: x['age']>19]
        .loc[lambda x: x['age']<41]
    )
    
    # Method Chain 3 (sorting data)
    
    df3 = (
        pd.DataFrame(df2)
        .sort_values(by='age')
    )
    
    print(f"This is the required data that I would like to analyse for my research question.")
    
    return df3

def final_plots(data):
    
    # A few plots to help visualise the data better.
    
    plot1 = sns.relplot(data=data,x='bmi',y='charges',hue='age')
    plt.title('Plot 1')
    print(f"Plot 1: The plot here shows that charges remain constant even with increase in BMI, in most cases.")
    
    plot2 = sns.relplot(data=data,x='bmi',y='age',hue='charges')
    plt.title('Plot 2')
    print(f"Plot 2: The plot here shows that charges remain constant with increase in age, regardless of any changes in BMI.")
    
    plot3 = sns.relplot(data=data,x='age',y='charges',hue='bmi')
    plt.title('Plot 3')
    print(f"Plot 3: The plot here shows that BMI remains constant with increase in age, although increase in BMI does not necessarily increase charges.")
    
    return plot1, plot2, plot3