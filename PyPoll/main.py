#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 04:41:45 2024

@author: conubogu
"""

import os
import csv
import sys

# Set variables to be used for calculations and storing data

candidate_pool = []
results_dict = {}


# Set path to locate csv file 
election_csv = os.path.join(".", "Resources", "election_data.csv")

# Open csv file using utf8 encoding and indicate delimiter is a comma
with open(election_csv, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
# Skip first row of csv file
    header = next(csvreader)
    
# Create a list of all the votes from the csv file
    votes = [row[2] for row in csvreader]
# Get the total number of voters using the votes list
    voter_count = len(votes)
# Get all the distinct candidates from the votes list       
    candidate_pool = set(votes)

# Assign the candidates to a dictionary with name as the key and 0 as the value
    for i in candidate_pool:
        results_dict[i] = 0
# Count the votes each candidate tallied by comparing the vote list to the 
# results_dict dictionary
    for vote in votes:
        results_dict[vote] += 1

# Identify the winner of the election        
    winner = max(results_dict, key = results_dict.get)

# Calculate the perecntage for each candidate and add to the dictionary    
    for k,v in results_dict.items():
        p = v/voter_count*100
        results_dict[k] = v,p

# Print results and format as needed               
    print(f"Total Votes: {voter_count}")
    for name, (votes, percentage) in results_dict.items():
        formatted_output = f'{name}: {percentage:.3f}% ({votes})'
        print(formatted_output)
    print(f"Winner: {winner}")
    
    
    #  Export results to text file named election results    
    with open('election_results.txt', 'w') as output_file:
        sys.stdout = output_file
        print('Election Results')
        print('------------------------------------------')
        print(f"Total Votes: {voter_count}")
        print('------------------------------------------')
        for name, (votes, percentage) in results_dict.items():
            formatted_output = f'{name}: {percentage:.3f}% ({votes})'
            print(formatted_output)
        print('------------------------------------------')
        print(f"Winner: {winner}")
       
    sys.stdout = sys.__stdout__
            
