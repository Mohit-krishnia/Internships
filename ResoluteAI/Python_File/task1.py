import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load the data
train_data = pd.read_excel('train.xlsx')

# Extract features (excluding the target column)
X = train_data.iloc[:, :-1]

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Reduce dimensionality for visualization (using PCA)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
train_data[['PC1', 'PC2']] = X_pca

# Apply K-Means clustering
num_clusters = 3  # You can adjust this based on your preference
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
train_data['Cluster'] = kmeans.fit_predict(X_scaled)

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(15, 6))

# Plot original data
axs[0].scatter(train_data['PC1'], train_data['PC2'], label='Original Data', alpha=0.5)
axs[0].set_title('Original Data and Clusters Visualization')
axs[0].set_xlabel('Principal Component 1')
axs[0].set_ylabel('Principal Component 2')

# Plot clusters and cluster centers
for cluster in range(num_clusters):
    cluster_data = train_data[train_data['Cluster'] == cluster]
    axs[1].scatter(cluster_data['PC1'], cluster_data['PC2'], label=f'Cluster {cluster + 1}')

# Plot cluster centers
cluster_centers = kmeans.cluster_centers_
axs[1].scatter(cluster_centers[:, 0], cluster_centers[:, 1], marker='X', s=200, color='red', label='Cluster Centers')

axs[1].set_title('Clustering Visualization')
axs[1].set_xlabel('Principal Component 1')
axs[1].set_ylabel('Principal Component 2')

# Add legends
axs[0].legend()
axs[1].legend()


plt.savefig('clustering_visualization.png')
plt.show()