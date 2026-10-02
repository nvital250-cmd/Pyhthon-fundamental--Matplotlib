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

plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.text(1, 80, 'Python is good at graphs')

plt.title("The setp() Function Example")

plt.annotate(
    'divergence point',
    xy=(1.5, 3),
    xytext=(3, 1.5),
    arrowprops=dict(facecolor='black', shrink=0.05)
)

plt.show()