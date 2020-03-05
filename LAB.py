import csv
import os
def printmatr(matr):
    for i in range(len(matr)):
        print()
        for el in matr[i]:
            print( el, end=" ")
countries = []
lst = os.listdir("D:\eurovis")
for i in range(len(lst)):
    os.chdir(r"D:\eurovis")
    with open(lst[i]) as file:
        read = csv.reader(file)
        for row in read:
            countries.append(row)

del countries[0]
del countries[10]
printmatr(countries)