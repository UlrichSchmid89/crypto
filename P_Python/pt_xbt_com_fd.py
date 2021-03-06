import os
import scipy
print('scipy: %s' % scipy.__version__)
import numpy as np
print('numpy: %s' % np.__version__)
import matplotlib
print('matplotlib: %s' % matplotlib.__version__)
import matplotlib.pyplot as plt
import pandas as pd
print('pandas: %s' % pd.__version__)
import sklearn
# import statsmodels
from pandas import Series
import datetime as dt
import pickle
import pylab

print(os.getcwd())

def main():
    print("First Module's Name: {}".format(__name__))

    if os.name == 'posix':
        sl = '/'
    elif os.name == 'nt':
        sl = '\\'

    dt_pd_xbt_com = pd.read_pickle('dt_pd_xbt_com.pickle')
    dt_pd_xbt_com = dt_pd_xbt_com[dt_pd_xbt_com.price_usd != 0]
    dt_pd_xbt_com['segment'] = 1
    # calculate log returns
    dt_pd_xbt_com['xbt_log_ret'] = np.log(dt_pd_xbt_com['price_usd'] / dt_pd_xbt_com['price_usd'].shift(1))
    dt_pd_xbt_com['xbt_fd'] = dt_pd_xbt_com['price_usd'] - dt_pd_xbt_com['price_usd'].shift(1)
    dt_pd_xbt_com['xbt_pct'] = dt_pd_xbt_com['price_usd'] / dt_pd_xbt_com['price_usd'].shift(1) - 1

    matplotlib.rcParams.update({'font.size': 16})

    dt_pd_xbt_com[['xbt_fd', 'xbt_pct', 'xbt_log_ret']].plot(subplots=True, color='blue', figsize=(8, 6))
    plt.gcf().set_size_inches(9, 8)

    os.chdir('..')
    os.chdir(os.path.abspath(os.curdir) + sl + "F_Figs" + sl)
    plt.savefig('pt_xbt_com_fd_pct_log_ret.pdf')

    plt.show()

    print('Plotting xbt_com_std done')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")