import csv
import os	


#get the path to the budget_data file

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


	
	percentage = 0


	#make list of the data that will be needed to print out on the text file.
	#Then, manually passing the index of the candidates, quantities of their votes, 
	#and the percentage of theeir votes in the the write() function
	
	percentage_list= []
	candidates_list = []
	candidates_votes_list = []


	winner = ''
	winner_votes = 0

	for item in votes:
		if votes[item] > winner_votes:
			winner = item
			winner_votes = votes[item]

		percentage = "{:.3%}".format((votes[item] / total_votes))
		percentage_list.append(percentage)
		candidates_list.append(item)
		candidates_votes_list.append(votes[item])

		print(item, ":", percentage, votes[item])
	

	print("-----------------------------")
	print(f"winner: {winner}")
	print("-----------------------------")
	

	

	with open(output_path, 'w') as text_file:
		text_file.write("Election Results \n")
		text_file.write("----------------------------- \n")
		text_file.write(f"Total votes: {total_votes} \n")	
		text_file.write("----------------------------- \n")

		#write on the text file the data that need to be shown (MANUALY)
		#NOT A PREFERABLE WAY, BUT COULD NOT FIND A BETTER SOLUTION AT THIS MOMENT
		
		text_file.write(f"{candidates_list[0]} : {percentage_list[0]} {candidates_votes_list[0]} \n")
		text_file.write(f"{candidates_list[1]} : {percentage_list[1]} {candidates_votes_list[1]} \n")
		text_file.write(f"{candidates_list[2]} : {percentage_list[2]} {candidates_votes_list[2]} \n")
		text_file.write(f"{candidates_list[3]} : {percentage_list[3]} {candidates_votes_list[3]} \n")
		text_file.write("----------------------------- \n")
		text_file.write(f"Winner: {winner} \n")
		text_file.write("----------------------------- \n")

