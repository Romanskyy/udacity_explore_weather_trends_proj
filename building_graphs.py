# import Pandas library for working with data sets
import pandas as pd
# import graph plotting library
import matplotlib.pyplot as plt

# open a SCV file and assign one to <df> variable
df = pd.read_csv(
    'CSV_files/data.csv')

# DataFrame plotting accessor and method from pandas
df.plot(y=['est_moving_average', 'fin_moving_average',
           'glob_moving_average'], x='year')

# plots lines to the axes
plt.plot()

plt.title(
    'Visualization for comparing changing temperature for period from 1915 to 2013')
plt.ylabel('temperature')
plt.xlabel('period for analysis, years')

# displays all open figures
plt.show()
