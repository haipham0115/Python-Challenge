import csv
import os	


#get the path to the budget_data file
#path = "../Resources/budget_data.csv"
path = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')
 


def count_the_months(csvfile):
	months = 0
	for row in csvfile:
		months += 1
	return months



#read the file
with open(path, 'r') as csvfile:

	csvreader = csv.reader(csvfile, delimiter = ",")
	csv_header = next(csvreader)
	cx = count_the_months(csvreader)
	print(cx)