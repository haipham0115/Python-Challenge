import csv
import os	


#get the path to the budget_data file
#path = "../Resources/budget_data.csv"
path = os.path.join('..', 'PyPoll', 'Resources', 'PyPoll_Resources_election_data.csv')

def count_votes(csvfile):
	total_votes = 0
	for row in csvfile:
		total_votes += 1
	return total_votes


#read the file
with open(path, 'r') as csvfile:

	csvreader = csv.reader(csvfile, delimiter = ",")
	csv_header = next(csvreader)
	
	trial = count_votes(csvreader)
	print(trial)