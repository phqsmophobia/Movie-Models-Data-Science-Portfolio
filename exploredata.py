import pandas as panda
import matplotlib.pyplot as plot
movies = panda.read_csv("movies.csv")
plot.style.use('seaborn-v0_8-whitegrid')

plot.scatter(movies["budget"], movies["revenue"])

plot.xlabel("Movie Budget in $")
plot.ylabel("Movie Revenue in $")
plot.title("Movie Budget vs Revenue")
plot.show()
