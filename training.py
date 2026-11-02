from datapreprocesser import x_value, y_value, movietitles
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

trainingsetx,testingsetx,trainingsety,testingsety, trainingtitles, testingtitles = train_test_split(x_value, y_value, movietitles, test_size=0.2, random_state=42)
newmodel = LinearRegression()
newmodel.fit(trainingsetx, trainingsety)