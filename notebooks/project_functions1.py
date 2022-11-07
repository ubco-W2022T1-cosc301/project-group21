import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

#Processing Data
def load_and_process(path):


    # Method Chain 1 (Load data and remove null values, if any)

    df1 = (
        pd.DataFrame(
            pd.read_csv(path)
        )
        .dropna(axis=0)
        #.drop_duplicates(inplace=true)
    )

    return df1

#These are sub methods to replace specific types of categorical data into numeric ones, so that it can be put into a correlation matrix
def clean(x):
    x = x.replace("female","0").replace("male","1")
    return int(x)
def clean2(x):
    x = x.replace("yes","0").replace("no","1")
    return int(x)
def clean3(x):
    x = x.replace("southwest","0").replace("southeast","1").replace("northwest","2").replace("northeast","3")
    return int(x)
#This method makes a copy of the given dataframe, converts categorical data into relevant numerical data and returns the df copy
def convert_catdata(data):
    df2 = data.copy()
    df2['sex'] = df2['sex'].apply(clean) 
    df2['smoker'] = df2['smoker'].apply(clean2)
    df2['region'] = df2['region'].apply(clean3)
    return df2


#This method finds and prints the number of outliers in a data set using the Z-score method and produces a graph highlighting where the outliers are.
#The Z-score method was used to find the outliers as it is a more appropriate method for a skewed data set.
zscore = []
def find_outliers(data):
    threshold = 3 #99% confidence interval
    outliers = []
    mean = np.mean(data)
    std = np.std(data)
    for i in data:
        z_score= (i - mean)/std 
        zscore.append(z_score)
        if np.abs(z_score) > threshold:
            outliers.append(i)
            
    plt.figure(figsize = (10,5))
    sns.histplot(zscore)
    plt.axvspan(xmin = 3 ,xmax= max(zscore),alpha=0.2, color='red')
    plt.xlabel("Z-score")
    return print("Total number of outliers are",len(outliers))



#This method produces the ranges and unique values of the attributes in the dataset
def rng_and_unqval(data):
    print(f'Age Range: {data.age.min()}','to',data.age.max()) #Values are appropriate (no negative/impossible values)
    print(f'BMI Range: {data.bmi.min()}','to',data.bmi.max()) #Values are appropriate (no negative/impossible values)
    print(f'Unique values in "Children": {data.children.unique()}') #Values are appropriate (no negative/impossible values)
    print(f'Unique values in "Sex": {data.sex.unique()}') #Values are appropriate
    print(f'Unique values in "Smoker": {data.smoker.unique()}') #Values are a little ambiguous; yes = smoker, no = non-smoker
    print(f'Unique values in "Region": {data.region.unique()}') #Values are clear and understandable
