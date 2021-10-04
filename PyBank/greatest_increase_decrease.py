import csv
import os	


#get the path to the budget_data file
#path = "../Resources/budget_data.csv"
path = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')




def greatest_decrease(csvfile):
	prev_row = next(csvfile)
	current_row = next(csvfile)
	
	delta = int(current_row[1]) - int(prev_row[1])
	greated_decrease = delta
	greated_increase = delta
	greatest_increase_month = current_row[0]
	greatest_deccrease_month = current_row[0]
	avg_total = delta
	months = 2

	for row in csvfile:
		delta = int(row[1]) - int(prev_row[1])
		prev_row = row

		if delta < greated_decrease:
			greated_decrease = delta
			greatest_deccrease_month = row[0]

		avg_total += delta
		months += 1

	print("months: ", months)
	print("greated_decrease: ", greatest_deccrease_month, " ", greated_decrease)

#read the file
with open(path, 'r') as csvfile:

	csvreader = csv.reader(csvfile, delimiter = ",")
	csv_header = next(csvreader)
	
	trial = greatest_decrease(csvreader)
	print(trial)