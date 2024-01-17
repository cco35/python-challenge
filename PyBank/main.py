#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 01:35:38 2024

@author: conubogu
"""

import os
import csv
import sys

# Set variables to be used for calculations and storing data
Months = 0
Total_PL = 0
Previous_Change = None
Total_Change = 0
Change = 0
max_inc = 0
max_dec = 0
Increase = ""
Decrease = ""

# Set path to locate csv file 
budget_csv = os.path.join(".", "Resources", "budget_data.csv")

# Open csv file using utf8 encoding and indicate delimiter is a comma
with open(budget_csv, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
# Skip first row of csv file
    header = next(csvreader)
    
# Go through each line of csv file
    for row in csvreader:
# Increase number of months with each row
        Months = Months + 1
# Add to total P/L with each row
        Total_PL = Total_PL + int(row[1])
        Change = int(row[1])
# Check if there is a value for previous change and if there is calclulate
# the change and add it to the counter for total change
        if Previous_Change is not None:
            Change = Change - Previous_Change
            Total_Change = Total_Change + Change
        
# Check if change is positive and > the max_inc value and replace max_inc if so
            if Change > 0 and Change > max_inc:
                max_inc = Change
                Increase = row[0] + " ($" + str(Change) + ")"
# Check if change is negative and < the max_inc value and replace max_dec if so                
            elif Change < 0 and Change < max_dec:
                max_dec = Change
                Decrease = row[0] + " ($" + str(Change) + ")"
                
# Update the previous change value 
        Previous_Change = int(row[1])

# Calculate the average change    
    Avereage_Change = round(Total_Change/(Months-1),2)

# Print Results    
    print(f"Total Months {Months}")
    print(f"Total ${Total_PL}")
    print(f"Average Change ${Avereage_Change}")
    print(f"Greatest Increase in Profits {Increase}")
    print(f"Greatest Decrease in Profits {Decrease}")

#  Export results to text file named financial_analysis    
    with open('financial_analysis.txt', 'w') as output_file:
        sys.stdout = output_file
        print('Financial Analysis')
        print('------------------------------------------')
        print(f"Total Months {Months}")
        print(f"Total ${Total_PL}")
        print(f"Average Change ${Avereage_Change}")
        print(f"Greatest Increase in Profits {Increase}")
        print(f"Greatest Decrease in Profits {Decrease}")
   
    sys.stdout = sys.__stdout__
        
        