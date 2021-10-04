import csv
import os	


#get the path to the budget_data file
#path = "../Resources/budget_data.csv"
path = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')


def total(csvfile):
	total_profit_loss = 0
	for row in csvfile:
		total_profit_loss = total_profit_loss + int(row[1])
	return total_profit_loss



#read the file
with open(path, 'r') as csvfile:

	csvreader = csv.reader(csvfile, delimiter = ",")
	csv_header = next(csvreader)
	
	trial = total(csvreader)
	print(trial)