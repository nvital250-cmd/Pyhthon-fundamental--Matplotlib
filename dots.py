import numpy as np
import matplotlib.pyplot as plt
x=np.random.normal(size=50)
y=np.random.normal(size=50)
plt.scatter(x,y, color = 'red', alpha =0.8)
plt.title('RANDOM DOTS')
plt.xlabel('X-axis')
plt.xlabel('Y-axis')
plt.show()