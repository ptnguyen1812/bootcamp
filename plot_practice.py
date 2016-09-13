import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns

# Set matplotlib rc params
rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

#data_txt = np.loadtxt('data/collins_switch.csv', delimiter=',', skiprows=2)

# iptg = data_txt[:,0]
# gfp = data_txt[:,1]
#
# # plot iptg vs gfp
# plt.semilogx(iptg, gfp, linestyle='none', marker = '.', markersize=20)
# plt.xlabel('IPTG (mM)')
# plt.ylabel('normalized GFP')
# plt.title('IPTG titration')
# plt.xlim(8e-4, 15)
# plt.ylim(-0.02, 1.02)
# plt.show()
# #plt.save

# iptg = data_txt[:,0]
# gfp = data_txt[:,1]
# sem = data_txt[:,2]
# plot iptg vs gfp
# plt.errorbar(iptg, gfp, yerr=sem, linestyle='none',
#               marker = '.', markersize=20)
# plt.xlabel('IPTG (mM)')
# plt.ylabel('normalized GFP')
# plt.title('IPTG titration')
# plt.xlim(8e-4, 15)
# plt.ylim(-0.02, 1.02)
# plt.xscale('log')
# plt.show()
#plt.save

# Practice exercise 3

def ecdf(data):
    """
    compute x, y values for an empirical distribution function
    """
    x = np.sort(data)
    y = np.arange(1, 1+len(x))/len(x)

    return x, y

# Load data
xa_high = np.loadtxt('data/xa_high_food.csv', comments = '#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments = '#')

x_high, y_high = ecdf(xa_high)
x_low, y_low = ecdf(xa_low)

plt.plot(x_high, y_high, marker = '.', linestyle = 'none',
         markersize= 20, alpha = 0.5)
plt.plot(x_low, y_low, marker = '.', linestyle = 'none',
         markersize= 20, alpha = 0.5)
plt.legend(('high food', 'low food'), loc='lower right')
plt.xlabel('Cross-sectional area (um)')
plt.ylabel('eCDF')
plt.show()
