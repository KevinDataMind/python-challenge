# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 21:58:41 2020

@author: 16366
"""

import os
import csv

total_months = 0
total_value = 0
previous = 0
diff = [] #creating to save "3rd" column to hold the difference
change = []
change = 0
Averagediff = 0
date = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999]



csvpath = os.path.join("C:/Users/16366/python-challenge/pybank/budget_data.csv")

with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    next(csv_reader)

    for row in csv_reader:
        #total months included in dataset
        total_months = total_months + 1


        #for collecting the greatest increase and decrease date
        date.append(row[0])

        #total amount of profit/losses over the period
        total_value = total_value + int(row[1])
        change = int(row[1])-previous #subtracting profit/loss 
        previous = int(row[1])
        diff.append(change) #diff is being pushed to the list to be saved
        length = len(diff) - 1
        date=date + [row[0]]

        #greatest increase/decrease in profits over the period
        if(change>greatest_increase[1]):
            greatest_increase[1]=change
            greatest_increase[0]=row[1]
        if(change<greatest_decrease[1]):
            greatest_decrease[0]=row[1]
            greatest_decrease[1]=change
     


    #average of the changes in profit/losses over the period    
    Averagediff = sum(diff[1:])/length      


    #print total months, total profit/losses, and average change
    print("----------------------------------------------------------")
    print("Fiancial Analysis")
    print("----------------------------------------------------------")

    print("Total Months: " + str(total_months))  
    print("Total: $" +str(total_value))
    print("Average Change: $", (Averagediff, 2))
    print("Greatest Increase in Profits:" + str(date[0]), "$" + str(greatest_increase[1]))
    print("Greatest Decrease in Profits:" + str(date[0]), "$" + str(greatest_decrease[1]))
    print("----------------------------------------------------------")

     #print total months, total profit/losses, and average change to a file
    
    f = open("budget_summary.txt", "w")
    print("----------------------------------------------------------", file=f)
    print("Fiancial Analysis", file=f)
    print("----------------------------------------------------------", file=f)

    print("Total Months: " + str(total_months), file=f)  
    print("Total: $" +str(total_value), file=f)
    print("Average Change: $", (Averagediff, 2), file=f)
    print("Greatest Increase in Profits:" + str(date[0]), "$" + str(greatest_increase[1]), file=f)
    print("Greatest Decrease in Profits:" + str(date[0]), "$" + str(greatest_decrease[1]), file=f)
    print("----------------------------------------------------------", file=f)

    f.close()   