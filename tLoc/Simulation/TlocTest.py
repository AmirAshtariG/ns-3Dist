import numpy as np
import matplotlib.pyplot as plt
import DistNs3 as Dist

# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(35000)
# params
dim = 10          # accuracy of plot. 1/dim is
randNum = 5000   # number of Random numbers to plot
size = 50 * dim


# tloc Distribution Params
# landa, c, k = 35.71, 2.09, 4.397
v, loc, scale = 2, 1.1, 1.1

# Generate Data from the I CDF
histBurr = Dist.dataGen(dim, randNum, size, "tloc", v, loc, scale)


from scipy.stats import t


# From ns-3
import pandas as pd

dat = np.array(pd.read_csv("RandTLoc4.txt"))
histBurrNs3 = np.zeros(size)
for i in range(0, len(dat)):
    rnd = dim * dat[i] + size/2
    if rnd >= size or rnd < 0:
        continue
    histBurrNs3[int(rnd)] += 1
histBurrNs3 *= dim / len(dat)

# Plot the figure
legend_entries = []
x = np.arange(-1 * size / (2 * dim), size / (2 * dim), 1 / dim)


# python
plt.plot(x, t.pdf(x, v, loc=loc, scale=scale),
       'r-', lw=2, alpha=0.6, label='t pdf')
legend_entries += ["tloc Python"]


# I-CDF
plt.bar(x, histBurr, width=0.1)
legend_entries += ["I-CDF tloc"]

# NS3
plt.bar(x, histBurrNs3, color=['green'], width=0.1)
legend_entries += ['TLoc ns3']



plt.legend(legend_entries, loc='best')
plt.grid()
plt.title("t loc Distribution v, loc, scale= 2, 1.1, 1.1")
plt.xlabel('X')
plt.ylabel('PDF')
plt.savefig('tlocDist4.png')
plt.show()
