import csv

file = open('cards.csv')

csvreader = csv.reader(file)

header = []

header = next(csvreader)

def getAll():
    rows = []
    for row in csvreader:
        rows.append(row)
    return rows