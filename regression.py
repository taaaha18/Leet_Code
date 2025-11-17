# 0. Imports and settings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Display options
pd.set_option("display.max_columns", None)
sns.set(style="whitegrid")
RANDOM_STATE = 42
MOD = 10**9 + 7


# 1.1 Replace filename if it differs
file_path = "advertising.csv"
df = pd.read_csv(file_path)

# 1.2 Quick look
print("Shape:", df.shape)
print(df.head())
print("\nInfo:")
print(df.info())
print("\nSummary statistics (numeric cols):")
print(df.describe())
print("\nColumn types:")
print(df.dtypes)

print('##################################')

print (df.isnull().sum())
missing_rows = df[df.isnull().any(axis=1)]
print('the missing rows are',missing_rows.head())

print('##################################')
numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
print("Numeric columns:", numeric_cols)

fig, axes = plt.subplots(len(numeric_cols), 1, figsize=(8, 4*len(numeric_cols)))
if len(numeric_cols) == 1:
    axes = [axes]
for ax, col in zip(axes, numeric_cols):
    sns.boxplot(x=df[col], ax=ax)
    ax.set_title(f"Boxplot for {col}")
plt.tight_layout()
plt.show()

# 3.2 IQR method to find outliers for each numeric column
def detect_outliers_iqr(series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5*iqr
    upper = q3 + 1.5*iqr
    return series[(series < lower) | (series > upper)]


for col in numeric_cols:
    out = detect_outliers_iqr(df[col])
    print(f"{col}: {len(out)} outliers")

print('##################################')
# 4.1 Pairwise scatter plots — how Sales relate to others
target = "Sales"  # check the actual column name in df; adjust if different
features = [c for c in numeric_cols if c != target]

# Scatter plots
fig, axes = plt.subplots(len(features), 1, figsize=(8, 4*len(features)))
if len(features) == 1:
    axes = [axes]
for ax, feat in zip(axes, features):
    ax.scatter(df[feat], df[target], alpha=0.6)
    ax.set_xlabel(feat)
    ax.set_ylabel(target)
    ax.set_title(f"{feat} vs {target}")
plt.tight_layout()
plt.show()

# 4.2 Correlation heatmap
corr = df[numeric_cols].corr()
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", square=True)
plt.title("Correlation matrix")
plt.show()

