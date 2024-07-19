import os
import csv
budget_csv = os.path.join(r"C:\Users\ashle\python-challenge\PyBank\Resources\budget_data.csv")

Total_Months = []
Profit_Losses = []
Changes = []

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    csvheader = next(csvreader)
    print(f"Header:{csvheader}")

    for row in csvreader:
        Total_Months.append(row[0])
        Profit_Losses.append(int(row[1]))

for i in range(len(Profit_Losses)-1):
    Changes.append(Profit_Losses[i+1] - Profit_Losses[i])

average_Changes = sum(Changes) / len(Changes)

greatest_increase = max(Changes)
greatest_increase_date = Total_Months[Changes.index(greatest_increase) + 1]
greatest_decrease = min(Changes)
greatest_decrease_date = Total_Months[Changes.index(greatest_decrease) + 1]

print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {len(Total_Months)}")
print(f"Total: ${sum(Profit_Losses)}")
print(f"Average Change: ${average_Changes:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

with open("output.txt", "w") as f:
    print("Financial Analysis", file=f)
    print("-------------------------", file=f)
    print(f"Total Months: {len(Total_Months)}", file=f)
    print(f"Total: ${sum(Profit_Losses)}", file=f)
    print(f"Average Change: ${average_Changes:.2f}", file=f)
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})", file=f)
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})", file=f)
