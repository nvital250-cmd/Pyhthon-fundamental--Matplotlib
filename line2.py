import numpy as np
import matplotlib.pyplot as plt

# Time values
t = np.arange(0, 5, 0.2)

# Plot three curves
lines = plt.plot(
    t, t,
    t, t**2,
    t, t**3
)

# Set properties for all lines at once
plt.setp(lines, color='red', linewidth=2)

plt.title("The setp() Function Example")


plt.show()