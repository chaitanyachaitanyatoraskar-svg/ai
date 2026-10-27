# ==============================================================================
# Practical 12
# Decision tree classifier using iris dataset
# ==============================================================================

# Step 1: Import required libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Step 2: Load the dataset
iris = load_iris()
print(iris)

# Features (input data)
X = iris.data

# Target (flower species)
y = iris.target

# Step 3: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 4: Create the Decision Tree model
model = DecisionTreeClassifier(random_state=42)

# Step 5: Train the model
model.fit(X_train, y_train)

# Step 6: Make predictions
y_pred = model.predict(X_test)

# Step 7: Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Step 8: Display results
print("Predicted Values:", y_pred)
print("Actual Values: ", y_test)
print("Accuracy:", accuracy)
