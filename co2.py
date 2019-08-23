import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
import pandas as pd

def no_spines(ax, left=False, right=False, top=False, bottom=False):
    ax.spines["top"].set_visible(top)
    ax.spines["right"].set_visible(right)
    ax.spines["left"].set_visible(left)
    ax.spines["bottom"].set_visible(bottom)

def no_ticks(ax, left=False, right=False, top=False, bottom=False):
    ax.tick_params(axis='both', which='both',
                   left=left, right=right, top=top, bottom=bottom)

df = pd.read_csv('co2.csv')
long_df = df.melt(id_vars=['Year'],
                  var_name='Month',
                  value_name='CO2')  # wide -> long

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', "Jul", "Aug",
          'Sep', 'Oct', 'Nov', 'Dec']

fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(13, 5))

ax1.scatter(df.Year, df.set_index('Year').mean(axis=1), s=10)
m, b = np.polyfit(df.Year, df.set_index('Year').mean(axis=1), 1)
# x = np.arange(min(long_df.index), max(long_df.index), 20)
x = df.Year
y = m * x + b
ax1.plot(x, y, '--', c='grey', label='Line of best fit', alpha=0.5)

ax1.legend()

no_spines(ax1)
no_ticks(ax1)
# turn on y-axis grid (horizontal indicator bars)
ax1.yaxis.grid(True, alpha=0.3)
ax1.xaxis.grid(True, alpha=0.3)


ax1.set_xlabel('Year', fontsize=13)
ax1.set_ylabel('CO$_2$ concentration (ppm)', fontsize=13)
ax1.set_title('Plot A', fontsize=15)

df = df.set_index('Year')
ax2.plot(df.mean())

no_spines(ax2, bottom=True)
no_ticks(ax2)
ax2.yaxis.grid(True, alpha=0.3)
ax2.xaxis.grid(True, alpha=0.3)
fig.tight_layout()
ax2.set_xlabel('Month', fontsize=13)
ax2.set_title('Plot B', fontsize=15)


winter = ['Dec', 'Jan', 'Feb']
summer = ['Jun', 'Jul', 'Aug']
spring = ['Mar', 'Apr', 'May']
fall = ['Sep', "Oct", 'Nov']
seasons = [('Winter', winter), ('Spring', spring), ('Summer', summer),
           ('Fall', fall)]
lbs = []
dats = []
for sn, ms in seasons:
    lbs.append(sn)
    dats.append(df[ms].melt().value)

ax3.boxplot(dats, labels=lbs)
no_ticks(ax3)
no_spines(ax3)
ax3.yaxis.grid(True, alpha=0.3)
ax3.set_title('Plot C', fontsize=15)


fig.savefig('co2question.png')
plt.subplots_adjust(wspace=0.3)
plt.show()

