import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
import pandas as pd
a = """Date, Name of Fruit, Sold, Remaining (Sellable)
2016-08-18, Apple, 12, 25
2016-08-18, Cucumber, 5, 6
2016-08-18, Peach, 1, 9
2016-08-18, Watermelon, 1, 4"""
dat = pd.read_clipboard(sep=', ')
dat.date = pd.to_datetime(dat.Date)
tot = dat.Sold.sum()
plt.pie(dat['Remaining (Sellable)'] / dat['Remaining (Sellable)'].sum(), labels=dat['Name of Fruit'])
plt.title('Remaining fruit')
dat2 = dat3 = dat
dat2.Date = '2016-08-19'
dat3.Date = '2016-08-20'
# pd.concat([dat, dat2, dat3]).plot.bar(["Date", "Name of Fruit"], "Sold")
fd = pd.concat([dat, dat2, dat3])
fd
fd.Date + fd["Name of Fruit"]
fd.Date + " " +  fd["Name of Fruit"]
x = fd.Date + " " +  fd["Name of Fruit"]
plt.show()
plt.bar(x, fd.Sold)
plt.xticks(x, rotation=90)
plt.gcf().subplots_adjust(bottom=0.2)
plt.show()

x = fd.Date[5:] + " " +  fd["Name of Fruit"]

X = []
for a in x.values:
    X.append(a[5:])

plt.bar(X, fd.Sold)
plt.xticks(X, rotation=90)
plt.gcf().subplots_adjust(bottom=0.33)
plt.show()

# libraries
import numpy as np
import matplotlib.pyplot as plt
 
# set width of bar
barWidth = 0.25
 
# set height of bar
bars1 = [12, 30, 1, 8, 22]
bars2 = [28, 6, 16, 5, 10]
bars3 = [29, 3, 24, 25, 17]
 
# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
 
# Make the plot
plt.bar(r1, bars1, color='#7f6d5f', width=barWidth, edgecolor='white', label='var1')
plt.bar(r2, bars2, color='#557f2d', width=barWidth, edgecolor='white', label='var2')
plt.bar(r3, bars3, color='#2d7f5e', width=barWidth, edgecolor='white', label='var3')
 
# Add xticks on the middle of the group bars
plt.xlabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], ['A', 'B', 'C', 'D', 'E'])
 
# Create legend & Show graphic
plt.legend()
plt.show()
