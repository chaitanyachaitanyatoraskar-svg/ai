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
