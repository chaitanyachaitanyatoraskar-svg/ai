# Practical 10: Machine Learning Workflow

## 📌 Problem Statement / Aim
End-to-end ML workflow on student dataset: data inspection, null checking, standard scaling, train-test splitting, and KNeighborsClassifier training & evaluation.

## 💻 Source Code
File: [`machine_learning_workflow.py`](./machine_learning_workflow.py)

```python
# ==============================================================================
# Practical 10 Machine Learning Workflow
# Required: pip install pandas scikit-learn
# ==============================================================================

import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Locate student.csv in current directory or script's directory
csv_path = "student.csv"
if not os.path.exists(csv_path):
    csv_path = os.path.join(os.path.dirname(__file__), "student.csv")

# a) load dataset
print("\n Load dataset")
data = pd.read_csv(csv_path)
print(data)

# b) (i) display missing values
print("\n display missing values")
print(data.isnull())

x = data[["Hours", "Attendance"]]
y = data["Result"]

s = StandardScaler()
x = s.fit_transform(x)

# b) (ii) display standard scalar values
print("\nstandard scalar values")
print(x)

# c) Split into training and testing
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.3, random_state=1)
print(X_train, "\n", X_test, "\n", Y_train, "\n", Y_test)

# d) training classifier
model = KNeighborsClassifier()
model.fit(X_train, Y_train)

train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

print("\nTraining Accuracy:", accuracy_score(Y_train, train_pred) * 100)
print("\nTesting Accuracy:", accuracy_score(Y_test, test_pred) * 100)
```

## 🖥️ How to Run
```bash
python3 machine_learning_workflow.py
```

## 📊 Expected Output (From Lab Manual)
```text
Output:

a) Load Dataset
   Hours  Attendance Result
0      2          60   Fail
1      3          65   Fail
2      4          70   Pass
3      5          75   Pass
4      6          80   Pass
5      1          50   Fail
6      7          90   Pass
7      3          55   Fail
8      8          95   Pass
9      5          85   Pass

b) (i) display missing values
   Hours  Attendance  Result
0  False       False   False
...

(ii) display standard scalar values
[[...]]

c) Split into training and testing
...

d) Training and Testing Accuracy
Training Accuracy: 85.71428571428571
Testing Accuracy: 66.66666666666666
```
