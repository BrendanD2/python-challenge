# Importing necessary packages
import os
import csv

# Creating a path to open the budget data csv file.
csvpath = os.path.join( 'PyBank','resources', 'budget_data.csv')

# Opening the csv file
with open(csvpath) as csvfile:

    # Marking the delimeter as commas.
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Reading the header and leaving it commented out because it is not necessary to print into our terminal.
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    
    # Setting variables to track the total months, the total profit/loses, a list for the dates, and a list for the profits/loses. 
    total_months = 0
    total = 0
    date_list = []
    budget_list = []
    # Going through each row and adding 1 to total months, the total of profit/loses to the total, adding the P/L to the budget list,
    # and the date to the date list.
    for row in csvreader:
      total_months += 1
      total = total + int(row[1])
      budget_list.append(row[1])
      date_list.append(row[0])
      
    # Creating a list to find the change by month.
    pl_change = []
    # Going tnrough the budget list and finding the difference between months and appending that result to the new list.
    for i in range(len(budget_list)):
      change = int(budget_list[i]) - int(budget_list[i-1])
      pl_change.append(change)
    
    # Popping the first value because that is the difference between the first row and last row. 
    pl_change.pop(0)
    # Finding the total of the differences to help find average later.
    pl_total = 0
    for i in range(len(pl_change)):
      pl_total = pl_total + pl_change[i]
    
    # Can now take the total and divide the length of the list to find the averages 
    average_plchange = float(pl_total / len(pl_change))
    
    # Creating a function that accepts a list to find the greatest value in that list to help us find the greatest increase. 
    def greatest_increase(list):
        greatest = 0
        for number in list:
            if number > greatest:
                greatest = number
        return greatest
    # Creating a function to help us find the greatest decrease between the months. This also accepts a list. 
    def greatest_decrease(list):
        smallest = 0
        for number in list:
            if number < smallest:
                smallest = number
        return smallest
    # Using our two new functions with the profit/loss list to find the greatest increases and decreases.
    increase = greatest_increase(pl_change)
    decrease = greatest_decrease(pl_change)
    # Finding the index of those values to help us find the date. We add 1 because the P/L list is 1 smaller than the date list. 
    date_indexincrease = pl_change.index(increase) + 1
    date_indexdecrease = pl_change.index(decrease) + 1
    #Using those indexes to find the dates associated to the greatest increase and decrease. 
    date_increase = date_list[date_indexincrease]
    date_decrease = date_list[date_indexdecrease]
    
    # Printing out the financial analysis with all of the values we found. 
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total}")
    print(f"Average Change: ${average_plchange:.2f}")
    print(f"Greatest Increase in Profits: {date_increase} (${increase})")
    print(f"Greatest Decrease in Profits: {date_decrease} (${decrease})")
    
    # Using the same print to create a text file with the analysis. 
    output_path = os.path.join('PyBank','analysis', 'results.txt')
    with open(output_path, "w") as resultstxt:
        resultstxt.write(f"Financial Analysis\n"
        "----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total}\n"
        f"Average Change: ${average_plchange:.2f}\n"
        f"Greatest Increase in Profits: {date_increase} (${increase})\n"
        f"Greatest Decrease in Profits: {date_decrease} (${decrease})\n")
    
