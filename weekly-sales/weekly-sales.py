import csv

ItemList = []
print('Press Enter to move to a newline')

with open('sales-summary-2024-02-01-2024-12-31 3.csv', newline='') as CSVFile:
  FileReader = csv.DictReader(CSVFile, delimiter=',')
  for i in FileReader:
    ItemList.append(i)

print(f'| {"Date":<17}|{"Gross sales":>12} |')
for i in reversed(ItemList):
  input(f'| {i["Date"]:<17}|{'$' + i["Gross sales"]:>12} |')