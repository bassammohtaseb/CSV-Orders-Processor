import csv, sys
from collections import OrderedDict, Counter 

class Item:
  def __init__(self, id, area, name, quantity, brand):
    self.id = id
    self.area = area
    self.name = name
    self.quantity = quantity
    self.brand = brand

class CalculatedItem:
  orderCount = 1
  brandNames = []

  def __init__(self, item, quantityCount):
    self.item = item
    self.quantityCount = quantityCount
    self.brandNames = []


fileName = input("Please enter your csv file name: ")

items = []

try:
  # opening the CSV file to read
  with open(fileName,'r') as file:
   
    # reading the CSV file
    csvFileReader = csv.reader(file)

    try:
      for row in csvFileReader:
        items.append(Item(row[0], row[1], row[2], int(row[3]), row[4]))
    except Exception as exceptions:
      sys.exit('Columns are not in the correct format')

    if csvFileReader.line_num == 0:
      sys.exit('No rows in the csv file')
    if csvFileReader.line_num >= 10000:
      sys.exit('Number of rows exceeds the limit')

    quantityItems = {}
    for item in items:
      if item.name in quantityItems:
        quantityItems[item.name].orderCount += 1
        quantityItems[item.name].quantityCount += item.quantity
      else:
        quantityItems[item.name] = CalculatedItem(item, item.quantity)
      quantityItems[item.name].brandNames.append(item.brand)

    # displaying the contents of the average orders in CSV file
    with open('0_'+fileName, 'w') as wcsvfile:
      csvFileWriter = csv.writer(wcsvfile)
      for key, value in quantityItems.items():
        csvFileWriter.writerow([key,value.quantityCount/len(items)])

    # displaying the contents of most ordered brand in CSV file
    with open('1_'+fileName, 'w') as wcsvfile:
      csvFileWriter = csv.writer(wcsvfile)
      for key, value in quantityItems.items():
        # get most common item in list
        counter = Counter(value.brandNames).most_common()
        # set the name of the common item in list
        csvFileWriter.writerow([key,list(counter[0])[0]])

  print("Please check the generated csv files in the same folder")

except FileNotFoundError as e:
  print("there is no file with the name that you've provided")
