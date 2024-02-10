import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the outputs of the three tasks
clustering_visualization = plt.imread('clustering_visualization.png')
predicted_labels = pd.read_excel('predicted_labels.xlsx')
output_result = pd.read_excel('output_result.xlsx')

# Task 1: Clustering Visualization
st.header("Task 1: Clustering Visualization")
st.image(clustering_visualization, use_column_width=True, caption="Clustering Visualization")

# Task 2: Predicted Labels
st.header("Task 2: Predicted Labels")
st.write("Predicted Labels:")
st.write(predicted_labels)

# Task 3: Output Result
st.header("Task 3: Output Result")
st.write("Output Result:")
st.write(output_result)

# Run the app with streamlit run app.py in the terminal
