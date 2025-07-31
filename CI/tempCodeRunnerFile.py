import numpy as np
import matplotlib.pyplot as plt

# --- Parameters ---
n_features = 2
n_samples = 1000

# --- Generate Data ---
np.random.seed(0)
X_class1 = np.random.randn(n_samples // 2, n_features) + 1
X_class2 = np.random.randn(n_samples // 2, n_features) - 1

X_combined = np.vstack((X_class1, X_class2))
y_combined = np.array([1] * (n_samples // 2) + [-1] * (n_samples // 2))

# Shuffle data
shuffled_indices = np.arange(n_samples)
np.random.shuffle(shuffled_indices)
X = X_combined[shuffled_indices]
y = y_combined[shuffled_indices]

# Add bias
X_bias = np.hstack((np.ones((n_samples, 1)), X))

# --- Hebbian Learning ---
weights = np.zeros(X_bias.shape[1])
for xi, yi in zip(X_bias, y):
    weights += xi * yi

# --- Predictions ---
def predict(X_input):
    X_input_bias = np.hstack((np.ones((X_input.shape[0], 1)), X_input))
    return np.sign(X_input_bias @ weights)

y_pred = predict(X_combined)
accuracy = np.mean(y_pred == y_combined)
misclassified_indices = np.where(y_pred != y_combined)[0]
misclassified_points = X_combined[misclassified_indices]
misclassified_count = len(misclassified_indices)

# --- Plotting ---
plt.figure(figsize=(9, 7))

# Class +1 (Purple) and Class -1 (Orange)
plt.scatter(X_class1[:, 0], X_class1[:, 1], color='purple', label='Class +1 (Purple)', alpha=0.7)
plt.scatter(X_class2[:, 0], X_class2[:, 1], color='orange', label='Class -1 (Orange)', alpha=0.7)

# Misclassified points (Red X)
plt.scatter(misclassified_points[:, 0], misclassified_points[:, 1], 
            marker='x', color='red', label='Misclassified', s=60, linewidths=2)

# Decision boundary
if weights[2] != 0:
    x_vals = np.linspace(X[:, 0].min() - 1, X[:, 0].max() + 1, 100)
    y_vals = -(weights[0] + weights[1] * x_vals) / weights[2]
    plt.plot(x_vals, y_vals, 'k--', linewidth=2, label='Decision Boundary')

# Labels, accuracy box
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Hebbian Learning Result')
plt.axhline(0, color='grey', linewidth=0.5)
plt.axvline(0, color='grey', linewidth=0.5)
plt.xlim(X[:, 0].min() - 0.5, X[:, 0].max() + 0.5)
plt.ylim(X[:, 1].min() - 0.5, X[:, 1].max() + 0.5)

# Accuracy text
plt.text(0.98, 0.98, f'Accuracy: {accuracy*100:.2f}%\nMisclassified: {misclassified_count}',
         transform=plt.gca().transAxes,
         fontsize=12,
         verticalalignment='top',
         horizontalalignment='right',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='black'))


plt.legend(loc='upper left')
plt.show()
