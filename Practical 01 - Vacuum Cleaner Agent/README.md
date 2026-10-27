# Practical No. 1: Q1. VACCUM CLEANER AGENT

## 📌 Problem Statement / Aim
Implementation of a table-driven reflex vacuum cleaner agent mapping (location, status) percepts to actions (Suck, Left, Right).

## 💻 Source Code
File: [`vacuum_cleaner_agent.py`](./vacuum_cleaner_agent.py)

```python
# ==============================================================================
# Practical No. 1
# Question: Q1. VACCUM CLEANER AGENT
# ==============================================================================

table = {
    ('A', 'Dirty'): 'Suck',
    ('A', 'Clean'): 'Right',
    ('B', 'Dirty'): 'Suck',
    ('B', 'Clean'): 'Left'
}

def vaccum_agent(location, Status):
    return table[(location, Status)]

if __name__ == "__main__":
    location = input("Enter location(A/B): ")
    Status = input("Enter Status (Dirty/Clean): ")
    action = vaccum_agent(location, Status)
    print("Action:", action)
```

## 🖥️ How to Run
```bash
python3 vacuum_cleaner_agent.py
```

## 📊 Expected Output (From Lab Manual)
```text
OUTPUT:

1. Enter location(A/B): B
Enter Status (Dirty/Clean): Clean
Action: Left

2. Enter location(A/B): A
Enter Status (Dirty/Clean): Dirty
Action: Suck
```
