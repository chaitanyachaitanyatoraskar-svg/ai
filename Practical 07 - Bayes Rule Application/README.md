# Practical 7: Bayes' Rule Application

## 📌 Problem Statement / Aim
Calculating posterior probability P(Disease|Positive Test) using Bayes' Theorem given prior probability and conditional likelihoods.

## 💻 Source Code
File: [`bayes_rule_application.py`](./bayes_rule_application.py)

```python
# ==============================================================================
# Practical 7 Bayes' Rule Application
# ==============================================================================

if __name__ == "__main__":
    # p(d)
    d = float(input("Enter the probability of person having a disease: "))

    # p(pos|d)
    pos_d = float(input("\nEnter the probability of positive test if a person has a disease: "))

    # p(pos|^d)
    pos_not_d = float(input("\nEnter the probability of positive test if a person does not have a disease: "))

    # p(^d)
    not_d = 1 - d

    # p(d|pos)
    d_pos = (pos_d * d) / ((pos_d * d) + (pos_not_d * not_d))

    # Converting to percentage
    res = d_pos * 100

    ans = round(res, 2)

    print("\nThe probability of a person having disease given that the test result is positive is: ", ans, "%")
```

## 🖥️ How to Run
```bash
python3 bayes_rule_application.py
```

## 📊 Expected Output (From Lab Manual)
```text
Output:

Enter the probability of person having a disease: 0.01

Enter the probability of positive test if a person has a disease: 0.99

Enter the probability of positive test if a person does not have a disease: 0.05

The probability of a person having disease given that the test result is positive is:  16.67 %
```
