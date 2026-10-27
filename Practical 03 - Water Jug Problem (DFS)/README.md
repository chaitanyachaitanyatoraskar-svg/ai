# Practical 3: DFS using Water jug problem

## 📌 Problem Statement / Aim
Simulation of production rules and state space transitions to solve the classic 4-liter and 3-liter water jug problem reaching 2 liters.

## 💻 Source Code
File: [`water_jug_dfs.py`](./water_jug_dfs.py)

```python
# ==============================================================================
# Practical 3: DFS using Water jug problem
# ==============================================================================

def water_jug():
    A = 0
    B = 0
    capacityA = 4
    capacityB = 3

    print("Initial State")
    print("A =", A, "B =", B)

    # Step 1: Fill Jug B
    B = capacityB
    print("\nFill Jug B")
    print("A =", A, "B =", B)

    # Step 2: Pour B -> A
    transfer = min(B, capacityA - A)
    A += transfer
    B -= transfer
    print("\nPour B -> A")
    print("A =", A, "B =", B)

    # Step 3: Fill Jug B again
    B = capacityB
    print("\nFill Jug B")
    print("A =", A, "B =", B)

    # Step 4: Pour B -> A
    transfer = min(B, capacityA - A)
    A += transfer
    B -= transfer
    print("\nPour B -> A")
    print("A =", A, "B =", B)

    if B == 2:
        print("\nTarget Achieved!")
        print("Jug B =", B, "liters")
    else:
        print("\nTarget Not Achieved.")

if __name__ == "__main__":
    water_jug()
```

## 🖥️ How to Run
```bash
python3 water_jug_dfs.py
```

## 📊 Expected Output (From Lab Manual)
```text
Output:

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
Jug B = 2 liters
```
