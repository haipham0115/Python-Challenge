import csv
import os	


#get the path to the budget_data file
#path = "../Resources/budget_data.csv"
input_path = os.path.join('..', 'PyPoll', 'Resources', 'PyPoll_Resources_election_data.csv')
output_path = os.path.join('..', 'PyPoll', 'Resources', 'election_result_printout.txt')

with open(input_path) as csvfile:
	csvreader = csv.reader(csvfile)
	header = next(csvreader)



	print("Election Results")
	print("-----------------------------")
	total_votes = 0

	votes = {}

	for row in csvreader:
		if row[2] in votes:
			votes[row[2]] +=1
		else:
			votes[row[2]] = 1

		
		total_votes +=1

	print(f"Total votes: {total_votes}")
	print("-----------------------------")


	def election_winner(votes):
		percentage = 0

		winner = ''
		winner_votes = 0

		for item in votes:
			if votes[item] > winner_votes:
				winner = item
				winner_votes = votes[item]

			percentage = "{:.3%}".format((votes[item] / total_votes))
			print(item, ":", percentage, votes[item])
		

		print("-----------------------------")
		print(f"winner: {winner}")
		print("-----------------------------")

	print_out_function = election_winner(votes)
	

	with open(output_path, 'w') as text_file:
		text_file.write("Election Results \n")
		text_file.write("----------------------------- \n")
		text_file.write(f"Total votes: {total_votes} \n")	
		text_file.write("----------------------------- \n")
		text_file.write(print_out_function)
		
		text_file.write("----------------------------- \n")
		text_file.write()
		text_file.write("----------------------------- \n")

