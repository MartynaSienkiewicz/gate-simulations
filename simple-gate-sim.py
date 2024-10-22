import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

# Constants
grid_size = 100  # 100x100 grid points
x = np.linspace(-50, 50, grid_size)
y = np.linspace(-50, 50, grid_size)
X, Y = np.meshgrid(x, y)

# Initialize the potential field
V = np.zeros((grid_size, grid_size))

# Define gate geometries and assign voltages to each gate
gates = [
    {"region": (-10, 10, 20, 25), "voltage": -0.5},  # A rectangular gate with -0.5V
    {"region": (-30, -25, -10, 10), "voltage": -0.8},  # A left rectangular gate with -0.8V
    {"region": (25, 30, -10, 10), "voltage": -0.3}  # A right rectangular gate with -0.3V
]

# Function to apply the gate potential in specified regions
def apply_gate_potential(V, x_min, x_max, y_min, y_max, voltage):
    """Apply the specified voltage to a rectangular gate region."""
    for i in range(grid_size):
        for j in range(grid_size):
            if x_min <= X[i, j] <= x_max and y_min <= Y[i, j] <= y_max:
                V[i, j] = voltage
    return V

# Apply the potential from each gate
for gate in gates:
    x_min, x_max, y_min, y_max = gate["region"]
    voltage = gate["voltage"]
    V = apply_gate_potential(V, x_min, x_max, y_min, y_max, voltage)

# Smooth the potential to simulate realistic gate influence (Gaussian smoothing)
V_smoothed = gaussian_filter(V, sigma=5)

# Plot the smoothed potential landscape
plt.figure(figsize=(6, 6))
plt.contourf(X, Y, V_smoothed, levels=50, cmap='coolwarm')
plt.colorbar(label='Potential (V)')
# Show the gate locations as red rectangles
for gate in gates:
    x_min, x_max, y_min, y_max = gate["region"]
    plt.plot([x_min, x_max, x_max, x_min, x_min], [y_min, y_min, y_max, y_max, y_min], color='red', lw=2)
plt.title('Electrostatic Potential due to Gate Voltages')
plt.xlabel('x (nm)')
plt.ylabel('y (nm)')
plt.show()
