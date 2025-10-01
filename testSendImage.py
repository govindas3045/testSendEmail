import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime  # Add this import

image_save_path = "./images/plots"
os.makedirs(image_save_path, exist_ok=True)  # Creates both images and plots folders

# Define the polynomial coefficients (example: x^3 - 2x^2 + 3x - 5)
coeffs = [1, -2, 3, -5]

# Create a polynomial object
p = np.poly1d(coeffs)

# Generate x values
x = np.linspace(-10, 10, 400)

# Compute y values
y = p(x)

# Plot the polynomial
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=f"Polynomial: {p}", color="blue")
plt.axhline(0, color="black", linewidth=0.7)  # x-axis
plt.axvline(0, color="black", linewidth=0.7)  # y-axis
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.title("Polynomial Graph")
plt.xlabel("x")
plt.ylabel("P(x)")

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"plot_{timestamp}.png"

plt.savefig(os.path.join(image_save_path, filename), format='png')
# plt.show()

# print('hello')