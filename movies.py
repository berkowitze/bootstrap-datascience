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


fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))

df = pd.read_csv('IMDBdata_hotlist2.csv')
lookat = ['Top 250 Movies', 'Bottom 250 Movies']
df = df[df.Record.isin(lookat)]
means = df.groupby('Record').Rating.mean()

ax1.bar([0, 1], means[lookat])
ax1.set_xticks([0, 1])
ax1.set_xticklabels([r.replace(' Movies', '') for r in lookat],
                    rotation=90)
ax1.set_ylabel('Average rating (1-10)', fontsize=13)
ax1.set_title('Top/Bottom movies average rating', fontsize=15)
ax1.set_xlabel('')
no_spines(ax1, bottom=True)
no_ticks(ax1)
ax1.yaxis.grid(True, alpha=0.3)

fig.subplots_adjust(bottom=0.33)


top250 = df[df.Record == 'Top 250 Movies']
revs = top250.Num_Reviews / 1e6
rating = top250.Rating
ax2.scatter(revs, rating, s=10, alpha=0.5)
ax2.set_xlabel('Number of movie reviews (millions)', fontsize=13)
ax2.set_ylabel('Movie rating (1-10)', fontsize=13)
ax2.set_title('Movie rating vs number of reviews', fontsize=15)
m, b = np.polyfit(revs, rating, 1)
x = np.linspace(revs.min(), revs.max(), 100)
y = m*x + b
ax2.plot(x, y, '--', color='grey', label='Best fit', alpha=0.5)
ax2.legend()
no_spines(ax2)
no_ticks(ax2)
ax2.yaxis.grid(True)
fig.tight_layout()
fig.subplots_adjust(wspace=0.3)
fig.savefig('movies.png')
plt.show()