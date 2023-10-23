import csv
import os

#creating the path (working in the same folder as the csv thus path as below)

budget_data = os.path.join("budget_data.csv")

with open (budget_data, mode='r', encoding="utf") as csvfile: 
        budget_reader =csv.reader(csvfile,delimiter =',')
        header = next (budget_reader)

   #empty lists(which will be columns) to append the values to (dates = total number of months)
        dates =[]

   #net_income = net total amount of profit/lossess
        net_income =[]

        greatest_increase= []
        greatest_decrease = []
        changes_profit_loss = []


        for rows in budget_reader:
# add to the dates empty list 
                dates.append(rows[0])

# add to net income for (profit change) empty list

                net_income.append(int(rows[1]))

        for x in range(1,len(net_income)):
                changes_profit_loss.append(net_income[x] - net_income[x -1])

total_months = len(dates)

total_profit = sum(net_income)


# Calculate the average change

average = sum(changes_profit_loss) / len(changes_profit_loss)

# Find the greatest increase and decrease
greatest_increase = max(changes_profit_loss)
greatest_decrease = min(changes_profit_loss)

max_date = dates[changes_profit_loss.index(greatest_increase) + 1]
min_date = dates[changes_profit_loss.index(greatest_decrease) + 1]



print ('Financial Analysis')
print ("................")
print (f"The total amount of months is {len(dates)}")
print (f"The total profit is $ {sum(net_income)}")
print (f"The average change is $ {average}")
print (f"The greatest increase: {max_date}  $ {greatest_increase}")
print (f"The greatest decrese: {min_date} $ {greatest_decrease}")



#Export a text file with the results.
txtpath = os.path.join("PyBankResults.txt")

#with open(txtpath, 'w') as text:
    #text.write("-------------------------------")
    #text.write("Total Months: " + str(dates))
    #text.write("Total: " + str(net_income))
    #text.write("Average: " + str(average))
    #text.write("Greatest Increase in Profits: " + str(max_date) + str(greatest_increase))
    #text.write("Greatest Decrease in Profit: " + str(min_date) + str(greatest_decrease))    

output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit}\n"
    f"Average Change: ${average}\n"
    f"Greatest Increase in Profits: {max_date}  $ {greatest_increase}\n"
    f"Greatest Decrease in Profits: {min_date} $ {greatest_decrease}\n")

# Export the results to text file
with open(txtpath, "w") as txt_file:
    txt_file.write(output)    