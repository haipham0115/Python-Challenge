import csv
import os	


#get the path to the budget_data file
#path = "../Resources/budget_data.csv"
path = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')




def greatest_increase(csvfile):
	
	max_increase = 0

	great_increase_in_profit = {}

	for row in csvfile:
		if int(row[1]) >= 0 and int(row[1]) >= max_increase:
			max_increase = int(row[1])
			great_increase_in_profit = {row[0] : max_increase}

	

	return great_increase_in_profit


#read the file
with open(path, 'r') as csvfile:

	csvreader = csv.reader(csvfile, delimiter = ",")
	csv_header = next(csvreader)
	
	trial = greatest_increase(csvreader)
	print(trial)