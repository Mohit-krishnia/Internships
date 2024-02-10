import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

# Load the training data
train_data = pd.read_excel('train.xlsx')  # Replace 'training_data.csv' with the actual filename of your training data

# Separate features and target column for classification
X_train = train_data.iloc[:, :-1]
y_train = train_data.iloc[:, -1]

# Standardize the data (if needed)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Train a RandomForestClassifier
classifier = RandomForestClassifier(random_state=42)
classifier.fit(X_train_scaled, y_train)

# Load the testing data
test_data = pd.read_excel('test.xlsx')  # Replace 'testing_data.csv' with the actual filename of your testing data

# Separate features in the testing data
X_test = test_data.iloc[:, :]

# Standardize the testing data using the same scaler from training
X_test_scaled = scaler.transform(X_test)

# Make predictions on the test set
y_pred = classifier.predict(X_test_scaled)

# Create a DataFrame with the predicted labels
predicted_labels_df = pd.DataFrame({'Predicted Labels': y_pred})

# Save the DataFrame to an Excel file
predicted_labels_df.to_excel('predicted_labels.xlsx', index=False)
if 'predicted_labels.xlsx':
    print('File has been developed . Thank you')
else:
    print('File has not developed. Some issues there.')
