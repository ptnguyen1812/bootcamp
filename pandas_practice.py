import pandas as pd
df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

# extract impf > 2000
df_big_force = df.loc[(df['adhesive strength (Pa)'] < -2000),['impact force (mN)']]
# impact force and adhesive force for all of Frog II's strikes
df_impf_af_II = df.loc[(df['ID'] == 'III'),
                        ['impact force (mN)', 'adhesive force (mN)']]

#xtract the adhesive force and the time the frog
#pulls on the target for juvenile frogs (Frogs III and IV).
df_af_time = df.loc[(df['ID'] == 'III') | (df['ID'] == 'IV'),
             ['time frog pulls on target (ms)', 'adhesive force (mN)']]
