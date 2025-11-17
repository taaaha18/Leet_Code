import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns


data = pd.read_csv("mnist_test.csv")

print("the shape of the data is ",data.shape)
print("The head of the data is ",data.head())


X = data.drop("label", axis=1)
y = data["label"]

plt.figure(figsize=(10,4))
for digit in range(10):
    # Pick first image of each digit
    sample = X[y == digit].iloc[0].values.reshape(28, 28)
    plt.subplot(2, 5, digit + 1)
    plt.imshow(sample, cmap="gray")
    plt.title(f"Digit: {digit}")
    plt.axis("off")
plt.tight_layout()
plt.show()

