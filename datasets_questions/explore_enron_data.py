#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print(enron_data[enron_data.keys()[0]])
print(len(enron_data))
no_of_features=len(enron_data[enron_data.keys()[0]])
print(no_of_features)
#no of values where POI is true
count=0
for i in range(len(enron_data)):
	a=enron_data.values()
	if a[i]['poi']==True:
		count=count+1
print "No. of values where POI is true:", count

#total no of POI's
poi_text='/home/vamshi/Desktop/Workspace/ud120-projects/final_project/poi_names.txt'
poi_names= open(poi_text, 'r')
fr = poi_names.readlines()
print "Total no of POI's:",(len(fr[2:]))
poi_names.close()

#total value of stock belonging to James Prentice

print "total value of stock belonging to James Prentice:",(enron_data["PRENTICE JAMES"]["total_stock_value"])

# from Wesley Colwell to POI's
print "from Wesley Colwell to POI's:",(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

# Value of stock options excercised by Jeffery Skilling
print "Value of stock options excercised by Jeffery Skilling:",(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

#Highest money taken
print "Highest money taken:"
print(enron_data['SKILLING JEFFREY K']['total_payments'])
print(enron_data['FASTOW ANDREW S']['total_payments'])
print(enron_data['LAY KENNETH L']['total_payments'])

# Quantified salary
count=0
for i in range(len(enron_data)):
    a=enron_data.values()
    if a[i]['salary']!='NaN':
        count=count+1
print "Quantified salary:", count


# Known E-mail address
count=0
for i in range(len(enron_data)):
    a=enron_data.values()
    if a[i]['email_address']!='NaN':
        count=count+1
print "Known E-mail address", count

#People with total_payments


#People with no total payments
count_NaN_tp = 0
for key in enron_data.keys():
    if enron_data[key]['total_payments'] == 'NaN':
        count_NaN_tp+=1
print "People with no total payments:", count_NaN_tp
tp=float(count_NaN_tp)/len(enron_data.keys())

#Percentage of people in the dataset having 'NaN' for their total payments

perc = tp*100
print 'Percentage of people in dataset having NaN for their payments', perc

count_NaN_tp = 0
for key in enron_data.keys():
    if enron_data[key]['total_payments'] == 'NaN' and enron_data[key]['poi'] == True :
        print
        count_NaN_tp+=1
print count_NaN_tp
print float(count_NaN_tp)/len(enron_data.keys())
