import csv
import os	


#get the path to the budget_data file
#path = "../Resources/budget_data.csv"
path = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')




def greatest_decrease(csvfile):
	max_decrease = 0

	great_decrease_in_profit = {}

	for row in csvfile:
		if int(row[1]) < 0 and int(row[1]) < max_decrease:
			max_decrease = int(row[1])
			great_decrease_in_profit = {row[0] : max_decrease}

	

	return great_decrease_in_profit



#read the file
with open(path, 'r') as csvfile:

	csvreader = csv.reader(csvfile, delimiter = ",")
	csv_header = next(csvreader)
	
	trial = greatest_decrease(csvreader)
	print(trial)