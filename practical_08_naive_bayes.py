# ==============================================================================
# Practical No: 08 Naive Bayes classification
# Required: pip install scikit-learn
# ==============================================================================

from sklearn.naive_bayes import GaussianNB

x_train = [
    [15, 0],
    [500, 12],
    [25, 1],
    [600, 15]
]

y_train = [0, 1, 0, 1]

model = GaussianNB()

model.fit(x_train, y_train)

new_email = [[450, 10]]

prediction = model.predict(new_email)

if prediction[0] == 1:
    print("prediction: This email is SPAM!")
else:
    print("prediction: This email is NOT SPAM!")
