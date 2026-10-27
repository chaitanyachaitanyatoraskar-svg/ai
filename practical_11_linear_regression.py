# ==============================================================================
# Practical 11 Linear Regression
# Required: pip install pandas scikit-learn
# ==============================================================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv("stu.csv")

x = data[['Hours']]
y = data['Marks']

X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.3, random_state=1)

model = LinearRegression()
model.fit(X_train, Y_train)

print("\nTraining Accuracy:", round(model.score(X_train, Y_train) * 100, 2))
print("\nTesting Accuracy:", round(model.score(X_test, Y_test) * 100, 2))

new_d = pd.DataFrame([[11]], columns=['Hours'])
pred = model.predict(new_d)

print("Predicted Marks for 11 hours:", round(pred[0], 2))
