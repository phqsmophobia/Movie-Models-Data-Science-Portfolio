import pandas as panda
import matplotlib.pyplot as plot
from matplotlib.ticker import StrMethodFormatter
movies = panda.read_csv("movies.csv")
plot.style.use('seaborn-v0_8-whitegrid')

#create a chart
figuregraph, axes = plot.subplots()
#plot our points
axes.scatter(movies["release_year"], movies["revenue"])
#for each movie, plot its title also
for i, movie in movies.iterrows():
    axes.annotate( movie["title"],(movie["release_year"], movie["revenue"]),fontsize=7)

#format the label so it shows in dollars and not in e
axes.yaxis.set_major_formatter(StrMethodFormatter('${x:,.0f}'))

#set axis labels & title
axes.set_xlabel("Movie Release Year")
axes.set_ylabel("Movie Revenue in $")
axes.set_title("Movie Release Year vs Movie Revenue")
plot.show()
