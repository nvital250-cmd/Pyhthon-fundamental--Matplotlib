import numpy as np
import matplotlib.pyplot as plt
plt.plot([1,2,3,4,5], [1,4,9,50,2], '-', linewidth=5.0)
plt.ylabel('some numbers')
plt.xlabel('A meaningless axis')
plt.axis([0,10,0,60])
plt.show()