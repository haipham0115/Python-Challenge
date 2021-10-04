import csv
import os	
from count_the_months import count_the_months

#get the path to the budget_data file
#path = "../Resources/budget_data.csv"
path = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')




def avg_change(csvfile):
	change = 0
	list_profit_loss = []
	months = 0

	for row in csvfile:
		list_profit_loss.append(row[1])
		change = int(list_profit_loss[-1]) - int(list_profit_loss[0])
		months += 1
	return change / months



#read the file
with open(path, 'r') as csvfile:

	csvreader = csv.reader(csvfile, delimiter = ",")
	csv_header = next(csvreader)
	
	trial = avg_change(csvreader)
	print(trial)