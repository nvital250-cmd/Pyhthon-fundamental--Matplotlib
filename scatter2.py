import numpy as np
import matplotlib.pyplot as plt
t= np.arange(0,5,0.2)
plt.plot(t,t,'rx',
         t, t**2, 'b*',
         t, t**3, 'go')
plt.show()