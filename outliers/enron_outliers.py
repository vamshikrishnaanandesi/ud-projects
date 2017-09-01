#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop("TOTAL",0)
data = featureFormat(data_dict, features)

### your code below
print data[0]

for point in data:
    salary = point[0]
    bonus = point[1]
    if bonus > 5000000 and salary > 1000000:
	print bonus
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

#to find the outlier
for key, value in data_dict.items():
	if value['bonus'] == data.max():
		print key

biggest = 0
for key, value in data_dict.items():
	if value['bonus'] > biggest:
		biggest = value['bonus']
		print key
