import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
data = pd.read_csv("dataset.csv")

# Features
X = data[['attendance', 'sessional_marks', 'midterm_marks', 'assignments', 'study_hours']]

# Target
y = data['performance']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained successfully!")