import csv
import os	


#get the path to the budget_data file
#path = "../Resources/budget_data.csv"
path = os.path.join('..', 'PyPoll', 'Resources', 'PyPoll_Resources_election_data.csv')

with open(path) as csvfile:
	csvreader = csv.reader(csvfile)
	header = next(csvreader)

	total_votes = 0

	votes = {}

	for row in csvreader:
		if row[2] in votes:
			votes[row[2]] +=1
		else:
			votes[row[2]] = 1

		
		total_votes +=1

	print(votes)

	print(votes.items())