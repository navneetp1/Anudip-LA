import pandas as pd
import numpy as np
import os

path = r"C:\Users\navne\OneDrive - GN Group Of Institutes\Desktop\Anudip github\Anudip-LA\Python\PandasDataAnalysis\customer_data.csv"
# path = os.path.abspath("customer_data.csv")

df = pd.read_csv(path)

value_stats = df.describe().T
print(value_stats) # T for transpose

stats = df.describe(include=object).T
print(stats) # T for transpose
print(type(stats))

#######################################################################

mean = df["Age"].mean().round(3)
print("Mean: ", mean)

median = df['Age'].median().round(3)
print("Median: ", median)

mode = df['Age'].mode().iloc[0]
print("Mode: ", mode)

std = df['Age'].std().round(3)
print("Standard Deviation: ", std)

minimum = df['Age'].min()
print("Minimum Age: ", minimum)

maximum = df["Age"].max()
print("Maximum Age: ", maximum)

#######################################################################

# Sample data
data = {
'Hours Studied': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
'Exam Scores': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
}

df = pd.DataFrame(data)

correlation = df['Hours Studied'].corr(df['Exam Scores'])
print("Correlation between Hours Studied and Exam Scores:", correlation)


