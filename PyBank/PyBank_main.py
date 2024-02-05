import os
import csv

# List out the variables required
months = []
amounts = []
profit_loss_change = []
changes = 0
net_amount = 0
total_months = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Find the file
budget_data_csv = os.path.join("Resources", "budget_data.csv")

# Open the data as a csv file and read the data
with open(budget_data_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    # Read header line and continue
    header = next(csv_reader)

    # Initialize variables
    first_row = next(csv_reader)
    total_months += 1
    net_amount += int(first_row[1])
    previous_amount = int(first_row[1])

    # Start the for loop for each row
    for row in csv_reader:

            # Set the vairables to the respective columns
            months = row[0]
            amounts = int(row[1])

            # Keep counting the months & amount in the loop
            total_months += 1
            net_amount += amounts

            # Changes between previous row and current row to calculate the profit/loss
            changes = amounts - previous_amount
            previous_amount = amounts

            profit_loss_change.append(changes)
            average_change = round(sum(profit_loss_change)/len(profit_loss_change), 2)
            
            # Greatest Increase & Greatest Decrease
            if changes > greatest_increase[1]:
                greatest_increase[1] = changes
                greatest_increase[0] = months

            if changes < greatest_decrease[1]:
                greatest_decrease[1] = changes
                greatest_decrease[0] = months

# Print the values
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase In Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease In Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Print to terminal & create a txt file
output_file_path = os.path.join("Analysis", "PyBank_output.txt")

with open(output_file_path, 'w') as textfile:
    # Write the header
    textfile.write("Financial Analysis\n")
    textfile.write("---------------------------\n")

    # Write the results
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${net_amount}\n")
    textfile.write(f"Average Change: ${average_change}\n")
    textfile.write(f"Greatest Increase In Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    textfile.write(f"Greatest Decrease In Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(f"The results have been saved to {output_file_path}")
