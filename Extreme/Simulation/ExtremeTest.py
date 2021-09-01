import numpy as np
import matplotlib.pyplot as plt
import DistNs3 as Dist


# params
dim = 50          # accuracy of plot. 1/dim is
randNum = 5000   # number of Random numbers to plot
size = 20 * dim

# Extreme Distribution Params
# landa, c, k = 35.71, 2.09, 4.397
loc, scale = 1, 0.5


# Generate Data from the I CDF
histBurr = Dist.dataGen(dim, randNum, size, "Extreme", loc, scale, None)

# From Python
from scipy.stats import gumbel_r
x = np.linspace(gumbel_r.ppf(0.01),
                gumbel_r.ppf(0.99), 100)

# From ns-3
import pandas as pd
dat = np.array(pd.read_csv("RandExtreme2.txt"))
histBurrNs3 = np.zeros(size)
for i in range(0, len(dat)):
    rnd = dim * dat[i]
    if rnd >= size or rnd < 0:
        continue
    histBurrNs3[int(rnd)] += 1
histBurrNs3 *= dim / len(dat)


# Plot the figure
legend_entries = []
x = np.arange(0, size / dim, 1 / dim)

# PYTHON
plt.plot(x, gumbel_r.pdf(x, loc=loc, scale=scale),
       'r-', lw=2)
legend_entries += ['Extreme python']

# I-CDF
plt.bar(x, histBurr, width=0.1)
legend_entries += ["I-CDF Extreme"]

# NS3
plt.bar(x, histBurrNs3, color=['green'], width=0.1)
legend_entries += ['Extreme ns3']

plt.legend(legend_entries, loc='best')
plt.grid()
plt.title("Extreme Dist loc, scale = 1, 0.5")
plt.xlabel('X')
plt.ylabel('PDF')
plt.savefig('ExtremesDistTest2.png')
plt.show()
