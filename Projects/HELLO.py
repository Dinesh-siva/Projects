 import numpy as np
 import matplotlib.pyplot as plt

x = np.linspace(0, 20, 100)
y = np.sin(x)
 # Plot the data.
plt.plot(x, y)

# Add a title.
plt.title("COST(x)")

# Add labels to the axes.
plt.xlabel("x")
plt.ylabel("y")

# Show the plot.
plt.show()
