import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Create data
np.random.seed(42)

x = np.linspace(0, 10, 20)
y = np.cumsum(np.random.randn(20))

# Create the figure
fig, ax = plt.subplots(figsize=(6, 4))

# Draw the line plot
sns.lineplot(
    x=x,
    y=y,
    ax=ax,
    linewidth=3
)

# Add title and labels
ax.set_title("Line Plot", fontsize=14, fontweight="bold")
ax.set_xlabel("X Values")
ax.set_ylabel("Y Values")

# Display the graph
plt.tight_layout()
plt.show()
