import csv
import os	


#get the path to the budget_data file
#path = "../Resources/budget_data.csv"
path = os.path.join('..', 'PyPoll', 'Resources', 'PyPoll_Resources_election_data.csv')

#outout the result



def voting_result(csvfile):
	candidates= []

	previous_row = next(csvfile)

	for row in csvfile:
			candidates.append(row[2])

	



	list_candidates = list(set(candidates))
			

		
	return list_candidates


#read the file
with open(path, 'r') as csvfile:

	csvreader = csv.reader(csvfile, delimiter = ",")
	csv_header = next(csvreader)
	
	trial = voting_result(csvreader)
	print(trial)