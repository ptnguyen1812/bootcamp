import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Set matplotlib rc params
rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# open df1: band   species  yearband  beak length  beak depth
# open df2, df3, : band   species  Beak length, mm  Beak depth, mm
# open df4, df5: band   species  blength  bdepth

df1973 = pd.read_csv('data/grant_1973.csv', comment='#')
df1975 = pd.read_csv('data/grant_1975.csv', comment='#')
df1987 = pd.read_csv('data/grant_1987.csv', comment='#')
df1991 = pd.read_csv('data/grant_1991.csv', comment='#')
df2012 = pd.read_csv('data/grant_2012.csv', comment='#')

#b. Merge df1 - 5 into one file:
# change 'yearband' into 'year' in df1
df1973 = df1973.rename(columns={'yearband': 'year'})
df1973['year'] = 1973

df1975['year'] = np.ones(len(df1975)).reshape(len(df1975),1)
df1987['year'] = np.ones(len(df1987)).reshape(len(df1987),1)
df1991['year'] = np.ones(len(df1991)).reshape(len(df1991),1)
df2012['year'] = np.ones(len(df2012)).reshape(len(df2012),1)

df1975['year'] = 1975
df1987['year'] = 1987
df1991['year'] = 1991
df2012['year'] = 2012

# tile_dict = {'beak length': 'beak length (mm)',
#                 'beak depth': 'beak depth(mm)',
#                 'Beak length, mm': 'beak length (mm)'}

df1973 = df1973.rename(columns ={'beak length' : 'beak length (mm)',
        'beak depth' : 'beak depth (mm)'})
df1975 = df1975.rename(columns ={'Beak length, mm' : 'beak length (mm)',
        'Beak depth, mm' : 'beak depth (mm)'})
df1987 = df1987.rename(columns ={'Beak length, mm' : 'beak length (mm)',
        'Beak depth, mm' : 'beak depth (mm)'})
df1991 = df1991.rename(columns ={'blength' : 'beak length (mm)',
        'bdepth' : 'beak depth (mm)'})
df2012 = df2012.rename(columns ={'blength' : 'beak length (mm)',
        'bdepth' : 'beak depth (mm)'})

df_concat = pd.concat((df1973, df1975, df1987, df1991, df2012), ignore_index=True).dropna()
#df_concat = df_concat['year'].astype(int)
df1973_drop = df1973.drop_duplicates('band')
df1975_drop = df1975.drop_duplicates('band')
df1987_drop = df1987.drop_duplicates('band')
df1991_drop = df1991.drop_duplicates('band')
df2012_drop = df2012.drop_duplicates('band')
# df_concat_dupl = df_concat.duplicated('band')
# df_concat_drop= df_concat.drop_duplicates('band')
df_concat_drop = pd.concat((df1973_drop, df1975_drop, df1987_drop,
                df1991_drop, df2012_drop), ignore_index=True).dropna()
df_concat_drop.to_csv('grant_tidy_data.csv', index = False)

def ecdf(data):
    """
    compute x, y values for an empirical distribution function
    """
    x = np.sort(data)
    y = np.arange(1, 1+len(x))/len(x)

    return x, y

x_1973, y_1973 = ecdf(df1973_drop['beak depth (mm)'])
x_1975, y_1975 = ecdf(df1975_drop['beak depth (mm)'])
x_1987, y_1987 = ecdf(df1987_drop['beak depth (mm)'])
x_1991, y_1991 = ecdf(df1991_drop['beak depth (mm)'])
x_2012, y_2012 = ecdf(df2012_drop['beak depth (mm)'])

#x_2012, y_2012 = ecdf(bd_2012)
#x_1975_bs, y_1975_bs = ecdf(bs_sample)
plt.close()
plt.plot(x_1973, y_1973, marker = '.', linestyle='none', color = 'blue', alpha = 0.5)
plt.plot(x_1975, y_1975, marker = '.', linestyle='none', color = 'red', alpha = 0.5)
plt.plot(x_1987, y_1987, marker = '.', linestyle='none', color = 'green', alpha = 0.5)
plt.plot(x_1991, y_1991, marker = '.', linestyle='none', color = 'green', alpha = 0.5)
plt.plot(x_2012, y_2012, marker = '.', linestyle='none', color = 'green', alpha = 0.5)

plt.xlabel('beak depth (mm)')
plt.ylabel('ECDF')
plt.legend(('1973', '1975', '1987', '1991', '2012'), loc='lower right')
plt.show()
