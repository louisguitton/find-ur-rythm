from sklearn.ensemble import RandomForestClassifier
from dataset_generator import *

xL1 = []
yL1 = []

add_samples(xL1, yL1, enrL1, features1, 5)

print(len(xL1))
classifier = RandomForestClassifier()
classifier.fit(xL1, yL1)

print(classifier.predict(xL1[0]))
print(yL1[0])
# classifier(X, y)
