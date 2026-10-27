# Artificial Intelligence (AI) Lab Practicals

A complete, well-organized repository containing Artificial Intelligence practical implementations in Python. Each practical includes the problem statement, aim/question, full implementation, sample inputs, and verified outputs matching the AI lab manual.

---

## 🗂️ Practical-Wise Directory Structure

The repository is organized practical-wise into dedicated directories as well as direct scripts for convenience:

| Practical No. | Topic / Question | Directory | Code Script | Key Concept |
| :---: | :--- | :--- | :--- | :--- |
| **Practical 1** | **Q1. Vacuum Cleaner Agent** | [`Practical 01 - Vacuum Cleaner Agent`](./Practical%2001%20-%20Vacuum%20Cleaner%20Agent/) | [`vacuum_cleaner_agent.py`](./Practical%2001%20-%20Vacuum%20Cleaner%20Agent/vacuum_cleaner_agent.py) | Table-Driven Reflex Agent |
| **Practical 1(B)** | **Table driven Agent for an Autonomous Taxi** | [`Practical 01B - Autonomous Taxi Agent`](./Practical%2001B%20-%20Autonomous%20Taxi%20Agent/) | [`autonomous_taxi_agent.py`](./Practical%2001B%20-%20Autonomous%20Taxi%20Agent/autonomous_taxi_agent.py) | Percept-Action Mapping |
| **Practical 2** | **Uniform / Uninformed Search (8-Puzzle BFS)** | [`Practical 02 - Uniform Search (8 Puzzle BFS)`](./Practical%2002%20-%20Uniform%20Search%20(8%20Puzzle%20BFS)/) | [`uniform_search.py`](./Practical%2002%20-%20Uniform%20Search%20(8%20Puzzle%20BFS)/uniform_search.py) | Breadth-First Search (BFS) |
| **Practical 3** | **DFS using Water Jug Problem** | [`Practical 03 - Water Jug Problem (DFS)`](./Practical%2003%20-%20Water%20Jug%20Problem%20(DFS)/) | [`water_jug_dfs.py`](./Practical%2003%20-%20Water%20Jug%20Problem%20(DFS)/water_jug_dfs.py) | State Transition / Search |
| **Practical 4** | **Uniform Cost Search (UCS) for Least-Cost Path** | [`Practical 04 - Uniform Cost Search`](./Practical%2004%20-%20Uniform%20Cost%20Search/) | [`uniform_cost_search.py`](./Practical%2004%20-%20Uniform%20Cost%20Search/uniform_cost_search.py) | Dijkstra / Min-Heap Priority Queue |
| **Practical 5** | **A\* for 8-Puzzle using Manhattan Distance** | [`Practical 05 - Astar 8 Puzzle Manhattan Distance`](./Practical%2005%20-%20Astar%208%20Puzzle%20Manhattan%20Distance/) | [`astar_8_puzzle_manhattan.py`](./Practical%2005%20-%20Astar%208%20Puzzle%20Manhattan%20Distance/astar_8_puzzle_manhattan.py) | A* Heuristic Search |
| **Practical 6** | **A\* with Straight Line Heuristic Distance** | [`Practical 06 - Astar Straight Line Heuristic Distance`](./Practical%2006%20-%20Astar%20Straight%20Line%20Heuristic%20Distance/) | [`astar_straight_line_heuristic.py`](./Practical%2006%20-%20Astar%20Straight%20Line%20Heuristic%20Distance/astar_straight_line_heuristic.py) | Route Finding (Romania Map) |
| **Practical 7** | **Bayes' Rule Application** | [`Practical 07 - Bayes Rule Application`](./Practical%2007%20-%20Bayes%20Rule%20Application/) | [`bayes_rule_application.py`](./Practical%2007%20-%20Bayes%20Rule%20Application/bayes_rule_application.py) | Posterior Probability |
| **Practical 8** | **Naive Bayes' Classification** | [`Practical 08 - Naive Bayes Classification`](./Practical%2008%20-%20Naive%20Bayes%20Classification/) | [`naive_bayes_classification.py`](./Practical%2008%20-%20Naive%20Bayes%20Classification/naive_bayes_classification.py) | Gaussian Naive Bayes (Spam Filter) |
| **Practical 9** | **Posterior Probability using Bayesian Networks** | [`Practical 09 - Posterior Probability Bayesian Networks`](./Practical%2009%20-%20Posterior%20Probability%20Bayesian%20Networks/) | [`posterior_probability_bayesian_networks.py`](./Practical%2009%20-%20Posterior%20Probability%20Bayesian%20Networks/posterior_probability_bayesian_networks.py) | `pgmpy`, Variable Elimination |
| **Practical 10** | **Machine Learning Workflow** | [`Practical 10 - Machine Learning Workflow`](./Practical%2010%20-%20Machine%20Learning%20Workflow/) | [`machine_learning_workflow.py`](./Practical%2010%20-%20Machine%20Learning%20Workflow/machine_learning_workflow.py) | `StandardScaler`, KNN Classifier |
| **Practical 11** | **Linear Regression** | [`Practical 11 - Linear Regression`](./Practical%2011%20-%20Linear%20Regression/) | [`linear_regression.py`](./Practical%2011%20-%20Linear%20Regression/linear_regression.py) | Hours vs Marks Prediction |
| **Practical 12** | **Decision Tree Classifier using Iris Dataset** | [`Practical 12 - Decision Tree Classifier Iris`](./Practical%2012%20-%20Decision%20Tree%20Classifier%20Iris/) | [`decision_tree_classifier_iris.py`](./Practical%2012%20-%20Decision%20Tree%20Classifier%20Iris/decision_tree_classifier_iris.py) | Decision Trees |
| **Practical 13** | **Multiclass Classification using Logistic Regression** | [`Practical 13 - Multiclass Classification Logistic Regression`](./Practical%2013%20-%20Multiclass%20Classification%20Logistic%20Regression/) | [`multiclass_classification_logistic_regression.py`](./Practical%2013%20-%20Multiclass%20Classification%20Logistic%20Regression/multiclass_classification_logistic_regression.py) | Multiclass Classification |
| **Practical 14** | **Binary Classifier using MNIST Dataset** | [`Practical 14 - Binary Classifier MNIST`](./Practical%2014%20-%20Binary%20Classifier%20MNIST/) | [`binary_classifier_mnist.py`](./Practical%2014%20-%20Binary%20Classifier%20MNIST/binary_classifier_mnist.py) | Binary Logistic Regression (Digit '5') |

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/chehysh-dev/ai.git
cd ai
```

### 2. Set Up a Virtual Environment (Optional but Recommended)
```bash
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 📖 Practical Details & Running Instructions

### Practical 1: Vacuum Cleaner Agent
- **Question**: Q1. VACCUM CLEANER AGENT
- **Run**:
  ```bash
  cd "Practical 01 - Vacuum Cleaner Agent"
  python3 vacuum_cleaner_agent.py
  ```
- **Sample Input**: Location: `B`, Status: `Clean`
- **Output**: `Action: Left`

### Practical 1(B): Autonomous Taxi Agent
- **Question**: Table driven Agent for an Autonomous Taxi (Percept_Action table)
- **Run**:
  ```bash
  cd "Practical 01B - Autonomous Taxi Agent"
  python3 autonomous_taxi_agent.py
  ```
- **Sample Input**: Signal: `Yellow`, Situation: `Clear`
- **Output**: `Action: Slow Down`

### Practical 2: Problem Solving by Searching (Uniform / Uninformed Search)
- **Question**: Given an initial configuration of 8-puzzle and a goal configuration, find shortest sequence of moves to reach goal state using BFS.
- **Run**:
  ```bash
  cd "Practical 02 - Uniform Search (8 Puzzle BFS)"
  python3 uniform_search.py
  ```
- **Output**:
  ```text
  Shortest Path:
  Right
  Number of Moves: 1
  ```

### Practical 3: Water Jug Problem (DFS)
- **Question**: DFS using Water jug problem (4L and 3L jugs to get 2L)
- **Run**:
  ```bash
  cd "Practical 03 - Water Jug Problem (DFS)"
  python3 water_jug_dfs.py
  ```
- **Output**: State transitions leading to `Jug B = 2 liters`.

### Practical 4: Uniform Cost Search
- **Question**: Uniform Cost Search to find least-cost path between cities
- **Run**:
  ```bash
  cd "Practical 04 - Uniform Cost Search"
  python3 uniform_cost_search.py
  ```
- **Input**: Start: `A`, Goal: `G`
- **Output**: `Least-cost path: A -> B -> D -> G`, `Total cost: 7`

### Practical 5: A* Search for 8-Puzzle
- **Question**: Astar for 8 puzzle using Manhattan Distance
- **Run**:
  ```bash
  cd "Practical 05 - Astar 8 Puzzle Manhattan Distance"
  python3 astar_8_puzzle_manhattan.py
  ```
- **Output**: Steps 0, 1, 2 board states and `Total Distance = 2`.

### Practical 6: A* on Romania Map
- **Question**: A* with straight line heuristic distance
- **Run**:
  ```bash
  cd "Practical 06 - Astar Straight Line Heuristic Distance"
  python3 astar_straight_line_heuristic.py
  ```
- **Output**: `Path: Arad -> Sibiu -> Rimnicu -> Pitesti -> Bucharest`, `Distance: 418`

### Practical 7: Bayes' Rule Application
- **Question**: Probability calculation using Bayes' Theorem
- **Run**:
  ```bash
  cd "Practical 07 - Bayes Rule Application"
  python3 bayes_rule_application.py
  ```
- **Output**: `The probability of a person having disease given that the test result is positive is: 16.67 %`

### Practical 8: Naive Bayes' Classification
- **Question**: Naive Bayes' Classification for Email Spam Detection
- **Run**:
  ```bash
  cd "Practical 08 - Naive Bayes Classification"
  python3 naive_bayes_classification.py
  ```
- **Output**: `prediction: This email is SPAM!`

### Practical 9: Bayesian Networks
- **Question**: Posterior probability using Bayesian Networks (Burglar|Alarm=True)
- **Run**:
  ```bash
  cd "Practical 09 - Posterior Probability Bayesian Networks"
  python3 posterior_probability_bayesian_networks.py
  ```
- **Output**: Marginal CPD table for Burglary given Alarm=True.

### Practical 10: Machine Learning Workflow
- **Question**: ML workflow with StandardScaler, KNN classifier, and train-test evaluation on `student.csv`
- **Run**:
  ```bash
  cd "Practical 10 - Machine Learning Workflow"
  python3 machine_learning_workflow.py
  ```
- **Output**: `Training Accuracy: 85.71%`, `Testing Accuracy: 66.67%`

### Practical 11: Linear Regression
- **Question**: Linear regression predicting marks based on study hours using `stu.csv`
- **Run**:
  ```bash
  cd "Practical 11 - Linear Regression"
  python3 linear_regression.py
  ```
- **Output**: `Training Accuracy: 99.64`, `Testing Accuracy: 98.71`, `Predicted Marks for 11 hours: 93.57`

### Practical 12: Decision Tree Classifier
- **Question**: Decision tree classifier using iris dataset
- **Run**:
  ```bash
  cd "Practical 12 - Decision Tree Classifier Iris"
  python3 decision_tree_classifier_iris.py
  ```
- **Output**: `Accuracy: 1.0`

### Practical 13: Multiclass Classification (Logistic Regression)
- **Question**: Multiclass classification using logistic regression on iris dataset
- **Run**:
  ```bash
  cd "Practical 13 - Multiclass Classification Logistic Regression"
  python3 multiclass_classification_logistic_regression.py
  ```
- **Output**: `Accuracy: 1.0`

### Practical 14: Binary Classifier using MNIST
- **Question**: Binary Classifier using MNIST / load_digits dataset (Detecting digit '5')
- **Run**:
  ```bash
  cd "Practical 14 - Binary Classifier MNIST"
  python3 binary_classifier_mnist.py
  ```
- **Output**: `Training Accuracy: 100.0`, `Testing Accuracy: 96.85`, `Digit is 5`
