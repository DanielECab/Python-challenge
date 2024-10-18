#Importing csv and os, loding the file using path.join.

import csv
import os

file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("analysis", "budget_analysis.txt")

  #Setting the variables for the Pybank.

total_months = 0
total_net = 0
monthly_change =[]
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999999]

#Opening and reading the csv file

with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    header = next(reader)
   
    first_row = next(reader)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    Prev_net = int(first_row[1])
   
   #Loop to calculate the total and net change

    for row in reader:
        total_months = total_months + 1
        total_net = total_net + int(row[1])
       
        net_change = int(row[1]) - Prev_net
        Prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        monthly_change = monthly_change + [row[0]]
       
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
       
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

#Calculating the average

monthly_avg = sum(net_change_list) / len(net_change_list)

#Printing the output to txt file.

output = (
    f"\nFinancial Analysis\n"
    f"------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(output)

#Results as a txt file

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

