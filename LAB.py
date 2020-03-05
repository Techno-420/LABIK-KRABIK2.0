import csv
import os


def printmatr(matr):
    for i in range(len(matr)):
        print()
        for el in matr[i]:
            print(el, end=" ")


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
#printmatr(countries)
for i in range(len(countries)):
    for j in range(1, len(countries[i])):
        countries[i][j] = int(countries[i][j])


def voice_of_day(matrcountr):
    c = []
    for i in range(1, len(matrcountr[0])):
        c.append([])
    for i in range(1, len(matrcountr)+1):
        for j in range(len(matrcountr)):
            c[i-1].append(matrcountr[j][i])
    return c


def sort_voice_of_day(matrvoice):
    for i in range(len(matrvoice)):
        matrvoice[i].sort(reverse=True)
    return matrvoice



