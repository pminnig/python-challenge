import os
import csv

csvpath = os.path.join('PyBank', 'resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    first_row = next(csvreader)
    previous = first_row[1]
    print(previous)
    previous = int(previous)
    Differences = []
    current = 0
    total = 0
    max = 0
    MaxDate = []
    min = 0
    MinDate = []
    length = 0
    for x in csvreader:
        current = int(x[1])
        Differences.append(current - previous)
        total += (current - previous)
        previous = current
        length += 1
        
        if current < max:
            max = current
            MaxDate = x[0]
            
        if current > min:
            min = current
            MinDate = x[0]  

    text = [f'Financial Analysis: Total Months: {length}, Total: $, {total}, Average Change: ${total/length}, Greatest Increase in Profits: ${max}, {MinDate}, Greatest Decrease in Profits: ${min},{MaxDate}']

    print('Financial Analysis')
    print('___________________')
    print('Total Months: ', length)
    print('Total: $', total)
    print('Average Change: $',total/length)
    print('Greatest Increase in Profits: ($',max,') ',MinDate)
    print('Greatest Decrease in Profits: ($',min,') ',MaxDate)

    file = open("analysis.txt", "w") 
    file.writelines(text) 
    file.close() 
