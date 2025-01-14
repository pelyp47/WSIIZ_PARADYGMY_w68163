import csv

def columnAvarage(fileName, columnName):
    with open(fileName, newline='') as plik:
        reader = csv.DictReader(plik)
        values = [float(row[columnName]) for row in reader if row[columnName]]
        return sum(values) / len(values) if values else 0

file = input("file CSV name: ")
column = input("column name: ")
print("avarage:", columnAvarage(file, column))