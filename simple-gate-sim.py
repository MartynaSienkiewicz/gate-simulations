import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as plt

# Define the grid for the device (2D simulation)
grid_size = 100  # 100x100 grid points
x = np.linspace(-50, 50, grid_size)
y = np.linspace(-50, 50, grid_size)
X, Y = np.meshgrid(x, y)

# Define positions of the gates (3/4 working)
gate_positions = [(0, 20), (-20, 0), (20, 0)]  # Coordinates of gates (adjust based on your setup)
gate_charges = [1.0, 1.0, -1.0]  # Charges at the gates (positive or negative)

# Define potential function (Coulomb potential)
def potential(x, y, x_g, y_g, q):
    """ Calculate the potential at (x, y) due to charge q at (x_g, y_g). """
    return q / np.sqrt((x - x_g)**2 + (y - y_g)**2 + 1e-9)  # Small term to avoid division by zero

# Initialize the total potential field
V_total = np.zeros((grid_size, grid_size))

# Add contributions from each gate
for (x_g, y_g), q in zip(gate_positions, gate_charges):
    V_total += potential(X, Y, x_g, y_g, q)

# Plot the resulting potential landscape
plt.figure(figsize=(6, 6))
plt.contourf(X, Y, V_total, levels=50, cmap='viridis')
plt.colorbar(label='Potential (arb. units)')
plt.scatter(*zip(*gate_positions), color='red', label='Gate positions', marker='x')
plt.legend()
plt.title('Electrostatic Potential due to Gates')
plt.xlabel('x (nm)')
plt.ylabel('y (nm)')
plt.show()
