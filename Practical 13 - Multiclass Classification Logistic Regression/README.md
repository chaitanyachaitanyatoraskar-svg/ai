# Practical 13: Multiclass classification using logistic regression

## 📌 Problem Statement / Aim
Multi-class classification using LogisticRegression (with max_iter=200) on the Iris dataset.

## 💻 Source Code
File: [`multiclass_classification_logistic_regression.py`](./multiclass_classification_logistic_regression.py)

```python
# ==============================================================================
# Practical 13
# Multiclass classification using logistic regression
# ==============================================================================

# Step 1: Import required libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Step 2: Load the Iris dataset
iris = load_iris()

# Features (input)
X = iris.data

# Target (output)
y = iris.target

# Step 3: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 4: Create the Logistic Regression model
model = LogisticRegression(max_iter=200)

# Step 5: Train the model
model.fit(X_train, y_train)

# Step 6: Predict the test data
y_pred = model.predict(X_test)

# Step 7: Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Step 8: Display the results
print("Predicted Values:", y_pred)
print("Actual Values: ", y_test)
print("Accuracy:", accuracy)
```

## 🖥️ How to Run
```bash
python3 multiclass_classification_logistic_regression.py
```

## 📊 Expected Output (From Lab Manual)
```text
Output:
Predicted Values: [1 0 2 1 1 0 1 2 1 1 2 0 0 0 0 1 2 1 1 2 0 2 0 2 2 2 2 2 0 0]
Actual Values:  [1 0 2 1 1 0 1 2 1 1 2 0 0 0 0 1 2 1 1 2 0 2 0 2 2 2 2 2 0 0]
Accuracy: 1.0
```
