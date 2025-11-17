import numpy as np
import matplotlib.pyplot as plt

# Step (Activation) Function
def step_function(z):
    if z >= 0:
        return 1
    else:
        return 0

# Perceptron Learning Algorithm
def train_perceptron(X, y, epochs=10, learning_rate=0.1):
    # Initialize weights and bias
    weights = np.zeros(X.shape[1])
    bias = 0

    # Training loop
    for epoch in range(epochs):
        for i in range(len(X)):
            # Linear combination
            z = np.dot(X[i], weights) + bias
            # Apply step activation
            y_pred = step_function(z)
            # Compute error
            error = y[i] - y_pred
            # Update weights and bias
            weights += learning_rate * error * X[i]
            bias += learning_rate * error

    return weights, bias

# Predict function
def predict(X, weights, bias):
    predictions = []
    for i in range(len(X)):
        z = np.dot(X[i], weights) + bias
        predictions.append(step_function(z))
    return np.array(predictions)

# Plot decision boundary
def plot_decision_boundary(X, y, weights, bias, title):
    x1 = np.linspace(-0.5, 1.5, 100)
    x2 = -(weights[0] * x1 + bias) / weights[1]
    plt.plot(x1, x2, label='Decision Boundary')
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
    plt.xlabel("Input 1")
    plt.ylabel("Input 2")
    plt.title(title)
    plt.legend()
    plt.show()

# -------------------------------
# AND Gate Data
# -------------------------------
X_and = np.array([[0,0], [0,1], [1,0], [1,1]])
y_and = np.array([0, 0, 0, 1])

weights_and, bias_and = train_perceptron(X_and, y_and, epochs=10, learning_rate=0.1)
print("AND Gate Weights:", weights_and)
print("AND Gate Bias:", bias_and)
pred_and = predict(X_and, weights_and, bias_and)
print("Predictions for AND Gate:", pred_and)
plot_decision_boundary(X_and, y_and, weights_and, bias_and, "AND Gate Decision Boundary")

# -------------------------------
# OR Gate Data
# -------------------------------
X_or = np.array([[0,0], [0,1], [1,0], [1,1]])
y_or = np.array([0, 1, 1, 1])

weights_or, bias_or = train_perceptron(X_or, y_or, epochs=10, learning_rate=0.1)
print("OR Gate Weights:", weights_or)
print("OR Gate Bias:", bias_or)
pred_or = predict(X_or, weights_or, bias_or)
print("Predictions for OR Gate:", pred_or)
plot_decision_boundary(X_or, y_or, weights_or, bias_or, "OR Gate Decision Boundary")
