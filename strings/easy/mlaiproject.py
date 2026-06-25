# Import libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# -------------------------------
# 1. Load Dataset
# -------------------------------
# Replace with your dataset file
data = pd.read_csv("aircraft_conflict_data.csv")

# Example columns:
# x1, y1, z1, vx1, vy1, vz1,
# x2, y2, z2, vx2, vy2, vz2,
# label (0 = safe, 1 = conflict)

X = data.drop("label", axis=1)
y = data["label"]

# -------------------------------
# 2. Train-Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# 3. Feature Scaling
# -------------------------------
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# -------------------------------
# 4. Build Neural Network
# -------------------------------
model = Sequential()

# Input layer + Hidden layers
model.add(Dense(32, activation='relu', input_shape=(X_train.shape[1],)))
model.add(Dense(16, activation='relu'))

# Output layer
model.add(Dense(1, activation='sigmoid'))

# -------------------------------
# 5. Compile Model
# -------------------------------
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# -------------------------------
# 6. Train Model
# -------------------------------
history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=8,
    validation_split=0.1
)

# -------------------------------
# 7. Predictions
# -------------------------------
y_pred = model.predict(X_test)
y_pred = (y_pred > 0.5).astype(int)

# -------------------------------
# 8. Evaluation Metrics
# -------------------------------
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("Confusion Matrix:\n", cm)