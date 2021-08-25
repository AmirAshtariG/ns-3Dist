import numpy as np
import matplotlib.pyplot as plt
import DistNs3 as Dist


# params
dim = 100          # accuracy of plot. 1/dim is
randNum = 1000000   # number of Random numbers to plot
size = 5 * dim

# Burr Distribution Params
landa, c, k = 0.9, 2, 1


# Generate Data from the I CDF
histBurr = Dist.dataGen(dim, randNum, size, "burr", landa, c, k)
histBurr2 = Dist.dataGen(dim, randNum, size, "burr", 1, c, k)



# Plot the figure
legend_entries = []


x = np.arange(0, size / dim, 1 / dim)
plt.bar(x, histBurr)
legend_entries += ["I-CDF Burr"]

plt.bar(x, histBurr2)
legend_entries += ["I-CDF Burr landa 1"]
plt.legend(legend_entries, loc='best')
plt.grid()
plt.xlabel('X')
plt.ylabel('PDF')
plt.savefig('BurrsDist.png')
plt.show()


