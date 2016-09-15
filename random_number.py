import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns
import bootcamp_utils

# Set matplotlib rc params
rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# def ecdf(data):
#     return np.sort(data), np.arange(1, len(data)+1)/len(data)
#
# x_ecdf, y_ecdf = ecdf(x)
#
# plt.plot(x_ecdf[::1000], y_ecdf[::1000], marker= '.', linestyle='none',
#         marketsize=10)
# plt.show()

data = np.random.randint(0, 4, size = 20)

bases = 'ATGC'

x=  np.random.randint(0,4, size=50)
seq_list = [None] * 50

for i, b in enumerate(x):
    seq_list[i] = bases[b]
print(''.join(seq_list))
#return ''.join(seq_list)
