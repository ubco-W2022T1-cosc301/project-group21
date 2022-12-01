# Final Group Report 21

## Introduction

All of us have grown up having our parents take care of our insurances, whether it be a medical insurance, life insurance, or home insurance. We have been ignorant about these matters most of our lives because we never had to bear these costs on our own. This changed for us after we came to Canada as International Students. We have since then realised how costly it can be to cover Medical Insurance for just oneself. Insurance is incredibly important to protect one’s family, properties, financial losses and even high medical costs and emergencies. When exploring this dataset, we discovered that there may be various factors such as one's demographic or medical index that correlates to differences in the insurance costs billed to them. We were interested in digging deeper into these data points and analyzing such relationships that may exist between some of these factors and the total charges.

## Exploratory Data Analysis

![Data Description](images/datadescr.png)

This is a visualization of the data analysis of numerical values in the dataset, containing key information such as mean, standard deviation, min and max values of Medical Charges incurred. This provided a general outlook on how numerical data values in the set may be correlated to one another along with the perspective of average values and degree of variance within each numeric category.

![Correlation Matrix](images/corrmatr.png)

The correlation matrix converts all data types to a numeric form and shows how strong the correlations between any two given columns are. This makes it easy to identify potential relationships between categories. As you can see, there is a strong correlation between smoking and charges, somewhat of a correlation between age and charges and bmi and charges.

![Pairplot](images/pairplot.png)

The pairplot visualization further improves our confidence in the correlational strength seen in the matrices by providing a visual aspect to the trend. They can be seen explicitly in the age to charges plot and somewhat in the bmi to charges plot.

## Research Question 1 + Result



## Research Question 2 + Result

Q2: The research question is to establish a relationship between BMI and medical insurance costs for people aged between 20 and 40.

[You can find the full analysis notebook here, along with the code and data here](notebooks/analysis2a.ipynb)

A2: The overall conclusion to the research question stands that **there is no distinguishable relationship solely between BMI and charges**, with random hikes in charges being observed for all ages. This is possibly because many other factors in the original data, such as children, sex, smoker, and region, contribute to fluctuations in the medical insurance costs from person to person.

![graph 1](images/analysis2a_graph1.png)

In general, for the BMI range of 20-45 and age range of 20-40, the charges ranged from $0-10000.

![graph 2](images/analysis2a_graph2.png)

For reasons inconclusive, the BMI range of 25-30 and age range of 20-40 sees a hike in the associated charges, ranging from $10000-20000.

![graph 3](images/analysis2a_graph3.png)

For reasons inconclusive, the BMI range of 30-40 and the age-range of 20-40 sees a hike in the associated charges, ranging from $30000-40000.

## Research Question 3 + Result

## Summary/Conclusion
