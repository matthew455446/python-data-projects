import numpy as np
import matplotlib.pyplot as plt

points = 1000000  # Number of points

x = np.random.rand(points)
y = np.random.rand(points)

distance_squared = x**2 + y**2
inside = distance_squared <= 1

pi_estimate = 4 * np.sum(inside) / points
print(f"Estimated π with {points} points: {pi_estimate:.6f}")

sample_size = 5000
sample_indices = np.random.choice(points, sample_size, replace=False)

plt.figure(figsize=(6,6))
plt.scatter(x[sample_indices][inside[sample_indices]],
            y[sample_indices][inside[sample_indices]],
            color='green', s=1, label='Inside Circle')
plt.scatter(x[sample_indices][~inside[sample_indices]],
            y[sample_indices][~inside[sample_indices]],
            color='red', s=1, label='Outside Circle')
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Monte Carlo π Simulation")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()