import csv
def printmatr(matr):
    for i in range(len(matr)):
        print()
        for el in matr[i]:
            print( el, end=" ")
countries = []
with open('eurovision1.csv') as f:
    read = csv.reader(f)
    for row in read:
        countries.append(row)
with open('eurovision2.csv') as f:
    read1 = csv.reader(f)
    for row in read1:
        countries.append(row)
del countries[0]
del countries[10]
printmatr(countries)