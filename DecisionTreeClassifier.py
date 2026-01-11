from sklearn.tree import DecisionTreeClassifier

X= [[0,0],[1,1],[1,0],[0,1]]

Y = [0,1,1,0]

model = DecisionTreeClassifier().fit(X,Y)

print(model.predict([[1,0]]))