# ==============================================================================
# Practical 14 Binary Classifier using MNIST dataset
# ==============================================================================

# Step 1: Import required libraries
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Step 2: Load the dataset
digits = load_digits()

# Features (input data)
X = digits.data

# Target (binary classification: whether digit is 5)
y = digits.target
y = (y == 5)

# Step 3: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

# Step 4: Train the model
model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

# Step 5: Accuracy
print("Training Accuracy:", model.score(X_train, y_train) * 100)
print("Testing Accuracy:", model.score(X_test, y_test) * 100)

# Step 6: Make predictions
prediction = model.predict([X_test[0]])

if prediction[0]:
    print("Digit is 5")
else:
    print("Digit is not 5")
