import pandas as panda
import matplotlib.pyplot as plot
from matplotlib.ticker import StrMethodFormatter
movies = panda.read_csv("movies.csv")
plot.style.use('seaborn-v0_8-whitegrid')

figuregraph, axes = plot.subplots()
axes.scatter(movies["budget"], movies["revenue"])
for index, movie in movies.iterrows():
    axes.annotate( movie["title"],(movie["budget"], movie["revenue"]),fontsize=7)

axes.xaxis.set_major_formatter(StrMethodFormatter('${x:,.0f}'))
axes.yaxis.set_major_formatter(StrMethodFormatter('${x:,.0f}'))

axes.set_xlabel("Movie Budget in $")
axes.set_ylabel("Movie Revenue in $")
axes.set_title("Movie Budget vs Movie Revenue")
plot.show()
