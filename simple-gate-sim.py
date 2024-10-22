import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from matplotlib.path import Path
import matplotlib.patches as patches

# Constants
grid_size = 100  # 100x100 grid points
x = np.linspace(-400, 400, grid_size)
y = np.linspace(-400, 400, grid_size)
X, Y = np.meshgrid(x, y)

# Initialize the potential field
V = np.zeros((grid_size, grid_size))

# Define gate geometries and assign voltages to each gate using coordinates
gates = {
    "Gate 1": {
        "x": [-35, 35, 50, -50],  
        "y": [170, 170, 400, 400],
        "voltage": -2.5
    },
    "Gate 2": {
        "x": [-25, 25, 50, -50],
        "y": [-170, -170, -400, -400],
        "voltage": -3.25
    },
    "Gate 3": {
        "x": [-120, -120, -210, -210, -150, -300, -300, -370, -400, -400], 
        "y": [-160, -120, -20, 100, 170, 310, 30, -70, -90, -260],
        "voltage": -0.68
    }
}

# Function to apply the gate potential in specified polygonal regions
def apply_gate_potential(V, x_coords, y_coords, voltage):
    """Apply the specified voltage to a polygon gate region."""
    # Create a Path object from the polygon vertices
    gate_path = Path(np.column_stack((x_coords, y_coords)))
    
    # Iterate over the grid and check if points are inside the polygon
    for i in range(grid_size):
        for j in range(grid_size):
            if gate_path.contains_point((X[i, j], Y[i, j])):
                V[i, j] = voltage
    return V

# Apply the potential from each gate
for gate_name, coords in gates.items():
    voltage = coords["voltage"]
    V = apply_gate_potential(V, coords["x"], coords["y"], voltage)

# Smooth the potential to simulate realistic gate influence (Gaussian smoothing)
V_smoothed = gaussian_filter(V, sigma=5)

# Plot the smoothed potential landscape
plt.figure(figsize=(6, 6))
plt.contourf(X, Y, V_smoothed, levels=50, cmap='coolwarm')
plt.colorbar(label='Potential (V)')

# Show the gate locations as red polygons with voltage labels
for gate_name, coords in gates.items():
    x_coords = coords["x"]
    y_coords = coords["y"]
    voltage = coords["voltage"]
    
    # Draw the gate as a polygon
    plt.plot(x_coords + [x_coords[0]], y_coords + [y_coords[0]], color='black', lw=1)  # Closing the polygon
    
    # Add text to label the voltage of the gate
    plt.text(np.mean(x_coords), np.mean(y_coords), f"{voltage} V", color="white", 
             fontsize=12, ha='center', va='center', bbox=dict(facecolor='red', alpha=0.5, edgecolor='none'))
    
# Set the aspect ratio to be equal
plt.gca().set_aspect('equal', adjustable='box')

plt.title('Electrostatic Potential due to Gate Voltages')
plt.xlabel('x (nm)')
plt.ylabel('y (nm)')
plt.show()
