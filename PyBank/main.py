import csv
import os	


#get the path to the budget_data file
#path = "../Resources/budget_data.csv"
path = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')


#read the file
with open(path, 'r') as csvfile:

	csvreader = csv.reader(csvfile, delimiter = ",")
	

	csv_header = next(csvreader)



	#Begin analysis
	total_profit_loss = 0
	change = 0
	avg_change = 0
	list_profit_loss = [0]

	profit_period = []
	max_increase = []

	loss_period = []
	min_decrease = []

	for row in csvreader:

		#count the months

		#calculate the total profit/loss
		total_profit_loss = total_profit_loss + int(row[1])


		#read all the profit/loss and append them into a list for calculation
		list_profit_loss.append(row[1])
		change = int(list_profit_loss[-1]) - int(list_profit_loss[0])

		#finding the highest increase
		if int(row[1]) >= 0:
			profit_period.append(row[1])

		


	print(months)
	print(total_profit_loss)
	print(change)


	
	
	
