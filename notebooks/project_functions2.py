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
        .loc[lambda x: x['age']>19]
        .loc[lambda x: x['age']<41]
        .sort_values(by='age')
    )
    
    print(f"This is the required data that I would like to analyse for my research question.")
    
    return df1