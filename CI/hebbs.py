import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Parameters ---
n_features = 2
n_samples = 1000
update_interval = 20  # update the decision boundary every 20 samples

# --- Generate Data ---
np.random.seed(42)
X_class1 = np.random.randn(n_samples // 2, n_features) + 1
X_class2 = np.random.randn(n_samples // 2, n_features) - 1
X = np.vstack((X_class1, X_class2))
y = np.array([1] * (n_samples // 2) + [-1] * (n_samples // 2))
X_bias = np.hstack((np.ones((n_samples, 1)), X))

# --- Initialize weights ---
weights = np.zeros(X_bias.shape[1])

# --- Set up plot ---
fig, ax = plt.subplots(figsize=(8, 6))
sc1 = ax.scatter(X_class1[:, 0], X_class1[:, 1], color='#1f77b4', alpha=0.6, s=30, label='Class +1')
sc2 = ax.scatter(X_class2[:, 0], X_class2[:, 1], color='#ff7f0e', alpha=0.6, s=30, label='Class -1')
decision_line, = ax.plot([], [], 'k--', linewidth=2, label='Decision Boundary')

ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.set_title('Hebbian Learning – Decision Boundary Animation')
ax.legend()
ax.grid(True)

# --- Animation update function ---
def update(frame):
    global weights
    for i in range(frame * update_interval, min((frame + 1) * update_interval, n_samples)):
        weights += X_bias[i] * y[i]

    x_vals = np.linspace(-4, 4, 100)
    if weights[2] != 0:
        y_vals = -(weights[0] + weights[1] * x_vals) / weights[2]
    else:
        y_vals = np.zeros_like(x_vals)
    decision_line.set_data(x_vals, y_vals)
    return decision_line,

# --- Animation setup ---
n_frames = (n_samples + update_interval - 1) // update_interval
ani = FuncAnimation(fig, update, frames=n_frames, interval=100, blit=True)

plt.tight_layout()
plt.show()
