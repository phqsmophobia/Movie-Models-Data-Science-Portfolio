from datapreprocesser import x_value, y_value, movietitles
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from matplotlib.ticker import StrMethodFormatter
import pandas as panda
import matplotlib.pyplot as plot

trainingsetx,testingsetx,trainingsety,testingsety, trainingtitles, testingtitles = train_test_split(x_value, y_value, movietitles, test_size=0.2, random_state=42)
newmodel = LinearRegression()
newmodel.fit(trainingsetx, trainingsety)
predictions = newmodel.predict(testingsetx)

for i in range(len(testingtitles)):
    #get per test
    title = testingtitles.iloc[i]
    actualrev = testingsety.iloc[i]
    predictedrev = predictions[i]
    #print per movie
    print(title)
    print("Actual Revenue:", actualrev)
    print("Predicted Revenue:", predictedrev)
    print()

#time to test our validity with comparison of actual vs predicted
#create a table to store the revenue values
result = panda.DataFrame()
result["Actual Revenue"] = testingsety.values
result["Predicted Revenue"] = predictions

# Display a graph comparing both values
result.plot(alpha=0.5)
plot.gca().yaxis.set_major_formatter(StrMethodFormatter('${x:,.0f}'))
plot.xlabel("Test Movie Number")
plot.ylabel("Movie Revenue in $")
plot.title("Actual Revenue vs Predicted Revenue")
plot.show()