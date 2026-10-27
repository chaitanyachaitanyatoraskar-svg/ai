# Artificial Intelligence (AI) Lab Practicals

A complete collection of Artificial Intelligence lab practical implementations in Python, covering search algorithms, intelligent agents, probabilistic reasoning, Bayesian networks, and machine learning models.

---

## 📋 Table of Contents

| Practical | Title / Topic | File | Key Concepts |
| :---: | :--- | :--- | :--- |
| **1** | Vacuum Cleaner Agent | [`practical_01_vacuum_cleaner.py`](./practical_01_vacuum_cleaner.py) | Table-Driven Reflex Agent |
| **1(B)** | Autonomous Taxi Agent | [`practical_01b_autonomous_taxi.py`](./practical_01b_autonomous_taxi.py) | Table-Driven Percept-Action Mapping |
| **2** | 8-Puzzle Problem using BFS | [`practical_02_8_puzzle_bfs.py`](./practical_02_8_puzzle_bfs.py) | Breadth-First Search, State-Space Search |
| **3** | Water Jug Problem | [`practical_03_water_jug.py`](./practical_03_water_jug.py) | Production Rules / State Transition |
| **4** | Uniform Cost Search (UCS) | [`practical_04_uniform_cost_search.py`](./practical_04_uniform_cost_search.py) | Priority Queue, Dijkstra / Least-Cost Path |
| **5** | A* for 8-Puzzle (Manhattan Distance) | [`practical_05_astar_8_puzzle.py`](./practical_05_astar_8_puzzle.py) | A* Search, Admissible Heuristics |
| **6** | A* Search on Romania Map | [`practical_06_astar_romania.py`](./practical_06_astar_romania.py) | Straight-Line Distance Heuristic |
| **7** | Bayes' Rule Application | [`practical_07_bayes_rule.py`](./practical_07_bayes_rule.py) | Conditional Probability, Posterior Inference |
| **8** | Naive Bayes Classification | [`practical_08_naive_bayes.py`](./practical_08_naive_bayes.py) | Gaussian Naive Bayes, Spam Detection |
| **9** | Bayesian Networks (Posterior Probability) | [`practical_09_bayesian_network.py`](./practical_09_bayesian_network.py) | `pgmpy`, Tabular CPDs, Variable Elimination |
| **10** | Machine Learning Workflow | [`practical_10_ml_workflow.py`](./practical_10_ml_workflow.py) | StandardScaler, KNN Classifier, train_test_split |
| **11** | Linear Regression | [`practical_11_linear_regression.py`](./practical_11_linear_regression.py) | Simple Linear Regression, Hours vs Marks |
| **12** | Decision Tree Classifier (Iris) | [`practical_12_decision_tree_iris.py`](./practical_12_decision_tree_iris.py) | Decision Trees, Multi-class Classification |
| **13** | Multiclass Logistic Regression (Iris) | [`practical_13_multiclass_logistic_regression.py`](./practical_13_multiclass_logistic_regression.py) | Logistic Regression, Softmax / One-vs-Rest |
| **14** | Binary Classifier on MNIST / Digits | [`practical_14_binary_classifier_mnist.py`](./practical_14_binary_classifier_mnist.py) | Logistic Regression, Binary Classification |

---

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/chaitanyachaitanyatoraskar-svg/ai.git
cd ai
```

### 2. Set Up a Virtual Environment (Recommended)
```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Practicals

### Practical 1: Vacuum Cleaner Agent
```bash
python3 practical_01_vacuum_cleaner.py
```
**Sample Input / Output:**
```text
Enter location(A/B): A
Enter Status (Dirty/Clean): Dirty
Action: Suck
```

---

### Practical 1(B): Table-Driven Autonomous Taxi Agent
```bash
python3 practical_01b_autonomous_taxi.py
```
**Sample Input / Output:**
```text
Enter signal(Red/Yellow/Speed limit exceeded/Passenger/Obstacle/Destination): Red
Enter Situation(Obstacle,Clear,Clear,Moving,Waiting,Moving,Reached): Obstacle
Action: Stop
```

---

### Practical 2: 8-Puzzle Problem using BFS
```bash
python3 practical_02_8_puzzle_bfs.py
```
**Expected Output:**
```text
Shortest Path:
Right
Number of Moves: 1
```

---

### Practical 3: Water Jug Problem Simulation
```bash
python3 practical_03_water_jug.py
```
**Expected Output:**
```text
Initial State
A = 0 B = 0

Fill Jug B
A = 0 B = 3

Pour B -> A
A = 3 B = 0

Fill Jug B
A = 3 B = 3

Pour B -> A
A = 4 B = 2

Target Achieved!
Jug B =  2 liters
```

---

### Practical 4: Uniform Cost Search (Least-Cost Path)
```bash
python3 practical_04_uniform_cost_search.py
```
**Sample Input / Output:**
```text
Enter start city: A
Enter goal city: G
Least-cost path: A -> B -> D -> G
Total cost: 7
```

---

### Practical 5: A* for 8-Puzzle using Manhattan Distance
```bash
python3 practical_05_astar_8_puzzle.py
```
**Expected Output:**
```text
Step 0
(1, 2, 3)
(4, 0, 6)
(7, 5, 8)

Step 1
(1, 2, 3)
(4, 5, 6)
(7, 0, 8)

Step 2
(1, 2, 3)
(4, 5, 6)
(7, 8, 0)

Total Distance = 2
```

---

### Practical 6: A* Search with Straight-Line Distance Heuristic
```bash
python3 practical_06_astar_romania.py
```
**Expected Output:**
```text
Path: Arad -> Sibiu -> Rimnicu -> Pitesti -> Bucharest
Distance: 418
```

---

### Practical 7: Bayes' Rule Application
```bash
python3 practical_07_bayes_rule.py
```
**Sample Input / Output:**
```text
Enter the probability of person having a disease: 0.01

Enter the probability of positive test if a person has a disease: 0.99

Enter the probability of positive test if a person does not have a disease: 0.05

The probability of a person having disease given that the test result is positive is:  16.67 %
```

---

### Practical 8: Naive Bayes Classification (Spam Detection)
```bash
python3 practical_08_naive_bayes.py
```
**Expected Output:**
```text
prediction: This email is SPAM!
```

---

### Practical 9: Bayesian Network Posterior Probability
```bash
python3 practical_09_bayesian_network.py
```
**Expected Output:**
```text
+---------------+---------------------+
| Burglary      | phi(Burglary)       |
+===============+=====================+
| Burglary(0)   | 0.5238              |
+---------------+---------------------+
| Burglary(1)   | 0.4762              |
+---------------+---------------------+
```

---

### Practical 10: Machine Learning Workflow
```bash
python3 practical_10_ml_workflow.py
```
Uses [`student.csv`](./student.csv) containing `Hours`, `Attendance`, and `Result`.

---

### Practical 11: Linear Regression
```bash
python3 practical_11_linear_regression.py
```
Uses [`stu.csv`](./stu.csv) containing `Hours` and `Marks`.
**Expected Output:**
```text
Training Accuracy: 99.64
Testing Accuracy: 98.71
Predicted Marks for 11 hours: 93.57
```

---

### Practical 12: Decision Tree Classifier (Iris Dataset)
```bash
python3 practical_12_decision_tree_iris.py
```
**Expected Output:**
```text
Accuracy: 1.0
```

---

### Practical 13: Multiclass Classification using Logistic Regression
```bash
python3 practical_13_multiclass_logistic_regression.py
```
**Expected Output:**
```text
Accuracy: 1.0
```

---

### Practical 14: Binary Classifier using MNIST / Digits Dataset
```bash
python3 practical_14_binary_classifier_mnist.py
```
**Expected Output:**
```text
Training Accuracy: 100.0
Testing Accuracy: 96.85185185185186
Digit is 5
```
