# Data collection and analysisimport numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Data collection and analysis
data = pd.read_csv("KMeans-Clustering\Mall_Customers.csv")
data

# data.head()

# finding no of rows and colums and some information of the dataset
data.shape
# data.info()

# checking for any null values
data.isnull().sum()

# selecting the columns annual income and spending score
X = data.iloc[:,[3,4]].values
# print(X)

# finding the wcss values for different number of clusters - wcss should be minimum
wcss = []

for i in range(1,11): # upto 11 clusters
    kmeans = KMeans(n_clusters=i, init="k-means++", random_state=42)
    kmeans.fit(X)

    # https://scikit-learn.org/1.5/modules/generated/sklearn.cluster.KMeans.html
    wcss.append(kmeans.inertia_)

# making an elbow plot to check the cluster that gives minimum value

sns.set()
plt.plot(range(1,11), wcss)
plt.title("Elbow Point Graph")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

# Training the k means clustering model with k = 5
kmeans = KMeans(n_clusters=5, init="k-means++", random_state = 0)

# return a label for each data point based on their cluster
Y = kmeans.fit_predict(X) # names the cluster
print(Y)

# visualizing all the clusters
# plotting clusters with their centroids

plt.figure(figsize=(8,8))
plt.scatter(X[Y==0,0], X[Y==0,1], s=50, c = "green", label="Cluster 1")
plt.scatter(X[Y==1,0], X[Y==1,1], s=50, c = "red", label="Cluster 2")
plt.scatter(X[Y==2,0], X[Y==2,1], s=50, c = "blue", label="Cluster 3")
plt.scatter(X[Y==3,0], X[Y==3,1], s=50, c = "indigo", label="Cluster 4")
plt.scatter(X[Y==4,0], X[Y==4,1], s=50, c = "violet", label="Cluster 5")

# plot the centroids
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=100, c="yellow", label="Centroids")

plt.title("Customer Clusters")
plt.xlabel("Annual Income")
plt.ylabel("Spending Scores(1-100)")

plt.show()
