import matplotlib.pyplot as plt

height = [150, 155, 160, 165, 170, 175]
weight = [45, 50, 54, 60, 65, 70]

plt.scatter(height, weight)

plt.title("Scatter Plot")
plt.xlabel("Height")
plt.ylabel("Weight")

plt.show()