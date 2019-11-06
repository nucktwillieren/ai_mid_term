import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
import numpy as np
import time

df = pd.read_csv('466920.csv')
df_in_2017 = df[df.year == 2017]
df_with_temp_filter = df_in_2017[df_in_2017.TX01 > -9900]
df_with_prep_filter = df_in_2017[df_in_2017.PP01 > -9900]

year_avg_temp = df_with_temp_filter['TX01'].mean()
year_total_prep = df_with_prep_filter['PP01'].sum()

print(year_avg_temp)
print(year_total_prep)

month_avg_temp = [df_with_temp_filter[df_with_temp_filter.month == month]['TX01'].mean() for month in range(1,13)]
month_total_prep = [df_with_prep_filter[df_with_prep_filter.month == month]['PP01'].sum() for month in range(1,13)]

print(month_avg_temp)
print(month_total_prep)

year_max_temp = df_with_temp_filter['TX01'].max()
year_max_temp_time = df_with_temp_filter[df_with_temp_filter.TX01 == year_max_temp].yyyymmddhh
year_min_temp = df_with_temp_filter['TX01'].min()
year_min_temp_time = df_with_temp_filter[df_with_temp_filter.TX01 == year_min_temp]['yyyymmddhh']

print(year_max_temp)
print(year_max_temp_time)
print(year_min_temp)
print(year_min_temp_time)

month_max_temp = [df_with_temp_filter[df_with_temp_filter.month == month]['TX01'].max() for month in range(1,13)]
month_min_temp = [df_with_temp_filter[df_with_temp_filter.month == month]['TX01'].min() for month in range(1,13)]

print(month_max_temp)
print(month_min_temp)

def autolabel(ax,rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{:4.1f}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

##############################################

############## Global Variables ##############

date_formatter = '%Y %m'
bar_width = 0.35

##############################################

############### Data Process #################

timestamp = np.array(["2017/{:02d}".format(month) for month in range(1,13)])

###############################################

############# Plot ##############

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

month_max_temp_line = ax1.plot(timestamp, month_max_temp, label='Monthly Max Temp', color="#ff3300")
month_min_temp_line = ax1.plot(timestamp, month_min_temp, label='Monthly Min Temp', color="#33cc33")
month_avg_temp_line = ax1.plot(timestamp, month_avg_temp, label='Monthly Avg Temp', color="#3399ff")
prep_bar = ax2.bar(timestamp, month_total_prep, bar_width, label='Monthly Total Prep', color="#9999ff")

ax1.set_title('2017 Monthly Max/Min/Avg Temperature and Monthly Total Precipitation')
ax1.set_xlabel('Time')
ax1.set_ylabel('Temperature(mm)')
ax2.set_ylabel('Precipitation(mm)')
plt.setp(ax1.get_xticklabels(), rotation=30)

ax1.legend(framealpha=0.5, bbox_to_anchor=(0.8, 1), loc='upper center')
ax2.legend(framealpha=0.5, bbox_to_anchor=(0.8, 0.75), loc='upper center')

autolabel(ax2,prep_bar)

plt.savefig('test.png',dpi=1200)