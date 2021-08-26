import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

dat = np.array(pd.read_csv("RandBurr.txt"))
dim = 100
size = 50 * dim
hist = np.zeros(len(dat))
for i in range(size):
    rnd = dim * dat[i]
    if rnd >= size:
        continue
    hist[int(rnd)] += 1

hist *= dim / len(dat)

print (hist)





plt.plot(hist, 'b-', lw=3, label='burr ns3')
plt.grid()
plt.title("Burr Dist l=1/0.028 c=2.09 k=4.397")
plt.xlabel('X')
plt.ylabel('PDF')
plt.savefig('BurrsDistTest-l=0.028 c=2.09 k=4.397.png')
plt.show()