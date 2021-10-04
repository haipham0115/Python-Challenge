import csv
import os	


#get the path to the budget_data file
#path = "../Resources/budget_data.csv"
input_path = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')
output_path = os.path.join('..', 'PyBank', 'Resources', 'budget_data_output.txt')



#read the file
with open(input_path, 'r') as csvfile:

	csvreader = csv.reader(csvfile, delimiter = ",")
	csv_header = next(csvreader)


	#variables for average changes

	#variables for greatest increase and decreases
	#storing the first and the second row of data, use for calculating delta
	prev_row = next(csvreader)
	current_row = next(csvreader)

	#variable for total value of profit and loss
	total_profit_loss = int(prev_row[1]) + int(current_row[1])
	
	delta = int(current_row[1]) - int(prev_row[1])


	greatest_decrease = delta
	greatest_increase = delta
	
	greatest_increase_month = current_row[0]
	greatest_decrease_month = current_row[0]
	
	avg_total = 0
	
	#variable for counting the months: starting at 2 because the first 2 lines are in prev_row and current_row
	months = 2

	deltas = []

	for row in csvreader:

		#process total value of profit and loss
		total_profit_loss += int(row[1])

		#process the greatest increase and greatest decrease
		delta = int(row[1]) - int(prev_row[1])
		deltas.append(delta)
		prev_row = row

		#calculating the greatest decrease
		if delta < greatest_decrease:
			greatest_decrease = delta
			greatest_deccrease_month = row[0]

		#calculating the greatest increase
		if delta > greatest_increase:
			greatest_increase = delta
			greatest_increase_month = row[0]


		months += 1

	avg_total = sum(deltas) / (months - 1)

	print("Financial Analysis")
	print("------------------------------------------------")
	print("total months: ", months)
	print("total: ", total_profit_loss)
	print("Average change: ", avg_total)
	print("greatest increase in profit: " , greatest_increase, " ", greatest_increase_month)
	print("greatest decrease in profit: " , greatest_decrease, " ", greatest_decrease_month)

	
	with open(output_path, 'w') as output_text:
		output_text.write("Financial Analysis \n")
		output_text.write("------------------------------------------------ \n")
		output_text.write("total months: "+ str(months) + "\n")
		output_text.write("total: " + str(total_profit_loss) + "\n")
		output_text.write("verage change: " + str(avg_total) + "\n")
		output_text.write("greatest increase in profit: "  + str(greatest_increase_month) + " " + str(greatest_increase) + " " +"\n")
		output_text.write("greatest decrease in profit: "  + str(greatest_decrease_month) + " " + str(greatest_decrease) + " " +"\n")
