#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys

sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

### your code goes here
from sklearn.cross_validation import train_test_split

features_train, features_test, lables_train, labels_test = train_test_split(features, labels, random_state=42,
                                                                            test_size=0.3)
from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()

clf.fit(features_train, lables_train)

acc = clf.score(features_test, labels_test)

pred = clf.predict(features_test)
print pred
print sum(pred)
print len(pred)

print pred.tolist().count(0) / float(len(pred))

print acc

# no of true positives
true_positives = 0
for i in range(len(pred)):
    if (pred[i] == labels_test[i]) and labels_test[i] == 1:
        true_positives += 1

print true_positives

false_positives = 0
for i in range(len(pred)):
    if (pred[i] != labels_test[i]) and labels_test == 1:
        false_positives += 1
print false_positives

false_negatives = 0
for i in range(len(pred)):
    if (pred[i] != labels_test[i]) and labels_test == 0:
        false_negatives += 1
print false_negatives

precision_score =  true_positives/(true_positives+false_positives)

#recall_score = true_positives/(true_positives+false_negatives)

#print precision_score, recall_score