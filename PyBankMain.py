import csv
import os

#creating the path

budget_data = os.path.join("budget_data.csv")

with open (budget_data,"r") as csvfile: 
    budget_reader =csv.reader(csvfile,delimiter =',')
    header = next (budget_reader)

   #lists to append the values to
    dates =[]
    net_income =[]
    greatest_increase= []
    greatest_decrease = []

    for rows in budget_reader:
# add to the dates empty list 
        dates.append(rows[0])

# add to net income for (profit change) empty list

        net_income.append(int(rows[1]))

# add to the greatest increase (which will be the maximum) list
        greatest_increase =  max(net_income) 

# add to the greatest decrease (minimum value)

        greatest_decrease = min(net_income)

#printing out the answers to look like the solution provided 

print ('Financial Analysis')
print ("................")
print (f"The total amount of months is {len(dates)}")
print (f"The total profit is $ {sum(net_income)}")
print (f"The average change is $ {round(sum(net_income)/len(dates))}")
print (f"The greatest increase  $ {greatest_increase}")
print (f"The greatest decrese is $ {greatest_decrease}")


datasum= ('Financial Analysis' ,"................" ,f"The total amount of months is {len(dates)}")
sumincome= (f"The total profit is $ {sum(net_income)}",f"The average change is $ {round(sum(net_income)/len(dates))}")
sumchange =(f"The greatest increase  $ {greatest_increase}", f"The greatest decrese is $ {greatest_decrease}")
sumbank = (sumincome,sumincome,sumchange)
textbank = os.path.join("Pybank_output.txt")
with open(textbank, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(sumbank)