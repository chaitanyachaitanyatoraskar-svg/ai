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
        print("Jug B = ", B, "liters")
    else:
        print("\nTarget Not Achieved.")

if __name__ == "__main__":
    water_jug()
