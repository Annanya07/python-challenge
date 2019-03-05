import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)
    csv_header = next(csvreader)
    profit = []
    date = []
    Change = []

    for row in csvreader:
        profit.append(float(row[1]))
        date.append(row[0])

    print('Financial Analysis')
    print('-'*25) 
    print(f'Total Months: {len(date)}')
    print(f'Total Revenue: ${int(sum(profit))}')

    x = 0
    for x in range(1,len(profit)):
        Change.append(profit[x] - profit[x-1])
        avgChange = sum(Change)/len(Change)
        maxChange = max(Change)
        minChange = min(Change)
        maxChangeDate = str(date[Change.index(max(Change))+1])
        minChangeDate = str(date[Change.index(min(Change))+1])

    print(f'Average Change: ${round(avgChange, 2)}')
    print(f'Greatest Increase in Profits: {maxChangeDate}  (${int(maxChange)})')
    print(f'Greatest Decrease in Profits: {minChangeDate}  (${int(minChange)})')



   