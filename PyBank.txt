import os
import csv

records = os.path.join("03-Python_homework_Instructions_PyBank_Resources_budget_data.csv")

date = []
profit_loss = []
new_profit_loss = []

with open(records, newline = "") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
    next(csv_reader)
    for row in csv_reader:
        date.append(row[0])
        profit_loss.append(row[1])

        for item in profit_loss:
            new_profit_loss.append(int(item))

        total_p_l = sum(new_profit_loss)

        average_changes = total_p_l / (len(new_profit_loss))

        greatest_gain = max(new_profit_loss)

        greatest_gain_initial = 0
        if greatest_gain_initial < int(row[1]):
            greatest_gain_inital = int(row[1])
            greatest_gain_date = row[0]

        greatest_loss = min(new_profit_loss)

        greatest_loss_initial = 0
        if greatest_loss_initial > int(row[1]):
            greatest_loss_inital = int(row[1])
            greatest_loss_date = row[0]

print("Financial Analysis")
print("-------------------------------------------")
print(f'Total Months: {len(date)}')
print(f'Total: {total_p_l}')
print(f'Average Change: ${average_changes}')
print(f'Greatest Increase in Profits: {greatest_gain_date} {greatest_gain}')
print(f'Greatest Decrease in Profits: {greatest_loss_date} {greatest_loss}')