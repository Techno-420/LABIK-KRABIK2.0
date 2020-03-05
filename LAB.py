import csv
import os
def printmatr(matr):
    for i in range(len(matr)):
        print()
        for el in matr[i]:
            print( el, end=" ")
countries = []
lst = os.listdir("D:\git\LABIK-KRABIK2.0\eurovis")
for i in range(len(lst)):
    os.chdir(r"D:\git\LABIK-KRABIK2.0\eurovis")
    with open(lst[i]) as file:
        read = csv.reader(file)
        for row in read:
            countries.append(row)

del countries[0]
del countries[10]
#printmatr(countries)
donematrix=[]
for i in range(len(countries)):
    tmp=[]
    tmp += [countries[i][0]]
    for j in range(1,len(countries[0])):
        tmp+=[int(countries[i][j])]
    donematrix+=[tmp]
printmatr(donematrix)