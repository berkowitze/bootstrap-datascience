import matplotlib.pyplot as plt
import numpy as np
import math

def no_spines(ax, left=False, right=False, top=False, bottom=False):
    ax.spines["top"].set_visible(top)
    ax.spines["right"].set_visible(right)
    ax.spines["left"].set_visible(left)
    ax.spines["bottom"].set_visible(bottom)


def no_ticks(ax, left=False, right=False, top=False, bottom=False):
    ax.tick_params(axis='both', which='both',
                   left=left, right=right, top=top, bottom=bottom)

def gen_watered():
    return int(math.floor((np.random.randn() * 2) + 20))
def gen_unwatered():
    return int(math.floor((np.random.randn() * 2.1) + 13))

def getwatered(n = 13):
    return [gen_watered() for _ in range(n)]

def getunwatered(n = 13):
    return [gen_unwatered() for _ in range(n)]

def doit():
    bins = np.linspace(10, 24, 8, endpoint=True)
    a = getunwatered()
    b = getwatered()
    if max(a) >= min(b):
        doit()
    fig, ax = plt.subplots()
    ax.hist([a, b], label=['Not Watered', 'Watered'], alpha=0.4, bins=bins, stacked=True)
    ax.legend()
    ax.set_xlabel('Days plant lived', fontsize=13)
    ax.set_ylabel('Number of plants', fontsize=13)
    ax.set_title('Watered vs unwatered plant lifetime', fontsize=15)
    ax.grid(True)
    no_spines(ax)
    no_ticks(ax)
    fig.tight_layout()
    fig.savefig('watered.png')
    plt.show()
    return a, b

doit()
def miniplot(ax, x, y, title, tick_at, xmin, xmax):
    ax.bar(x, y, width=1.0, color='black')
    no_spines(ax, bottom=True, left=True)
    ax.set_xlim(xmin, xmax)
    ax.set_xticks([tick_at])
    ax.set_xticklabels([tick_at])
    ax.set_yticks([])
    ax.set_title(title)

def doit2():
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=1, ncols=4, figsize=(10, 2.5))

    miniplot(ax1, [22, 23, 24, 30], [5, 7, 4, 2], 'Plot A', 23, 15, 31)
    miniplot(ax2, [16, 22, 23, 24], [3, 5, 7, 4], 'Plot B', 23, 15, 31)
    miniplot(ax3, [26, 27, 28, 34], [5, 7, 4, 2], 'Plot C', 27, 19, 35)
    miniplot(ax4, [26, 27, 28], [5, 7, 4], 'Plot D', 27, 19, 35)
    fig.tight_layout()
    plt.subplots_adjust(wspace=0.3)
    fig.savefig('lifeexp.png')
    plt.show()

doit2()