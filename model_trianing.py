from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import numpy as np # Import numpy for np.unique

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Shape of X_train: {X_train.shape}")
print(f"Shape of X_test: {X_test.shape}")
print(f"Shape of y_train: {y_train.shape}")
print(f"Shape of y_test: {y_test.shape}")

# Instantiate the classification model (Logistic Regression)
model = LogisticRegression(max_iter=1000, random_state=42)

# Train the model
model.fit(X_train, y_train)

print("\nModel training complete.")

# Make predictions on the test set
y_pred = model.predict(X_test)

# Get the unique labels present in the test set
unique_test_labels = np.unique(y_test)

# Get the corresponding target names for these labels
target_fnames_for_report = label_encoder.inverse_transform(unique_test_labels)

# Evaluate the model's performance
print("\nClassification Report:")
print(classification_report(y_test, y_pred, labels=unique_test_labels, target_names=target_names_for_report))

print("\nAccuracy Score:")
print(accuracy_score(y_test, y_pred))

# The trained model is stored in the 'model' variable for later use.
