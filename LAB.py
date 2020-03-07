import csv
import os


countries = []
name = str(input("Введите путь к папке:"))
lst = os.listdir(name)
for i in range(len(lst)):
    os.chdir(name)
    with open(lst[i]) as file:
        read = csv.reader(file)
        for row in read:
            countries.append(row)
del countries[0]
del countries[10]
for i in range(len(countries)):
    for j in range(1, len(countries[i])):
        countries[i][j] = int(countries[i][j])


def points_and_countries(matrcountr):
    pointcountrmass = []
    for j in range(len(matrcountr)):
        pointcountrmass.append([])
    for i in range(len(pointcountrmass)):
        for j in range(1):
            pointcountrmass[i].append(matrcountr[i][j])
            pointcountrmass[i].append(0)
    return pointcountrmass


pointscountr = points_and_countries(countries)


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


sortmatrx = sort_voice_of_day(voice_of_day(countries))


def count_points(matrcountr, pointsandcountr, sortmatr):
    point = 10
    maxel = 0
    for l in range(10):
        for i in range(1, len(matrcountr)+1):
            maxelindI = 0
            maxel = sortmatr[i-1][l]
            for k in range(1, len(matrcountr)+1):
                for o in range(len(matrcountr)):
                    if matrcountr[o][k] == maxel:
                        matrcountr[o][k] = 0
                        maxelindI = o
            if l == 0:
                pointsandcountr[maxelindI][1] += 12
            elif l == 1:
                pointsandcountr[maxelindI][1] += 10
            elif (l >= 2) and (l <= 9):
                pointsandcountr[maxelindI][1] += point
        point -= 1
    return pointsandcountr


pointscountr = count_points(countries, pointscountr, sortmatrx)


def sort(matrcountr):
    newmatrcountr = []
    sortarr = []
    for i in range(len(matrcountr)):
        for j in range(1):
            sortarr.append(matrcountr[i][j+1])
    sortarr.sort(reverse=True)
    for i in range(len(matrcountr)):
        for j in range(len(sortarr)):
            if matrcountr[j][1] == sortarr[i]:
                newmatrcountr.append(matrcountr[j])
                matrcountr[j][1] = 0
    for i in range(len(matrcountr)):
        for j in range(1):
            newmatrcountr[i][j+1] = sortarr[i]
    return newmatrcountr


newmatrcountr = sort(pointscountr)
newmatrcountr = newmatrcountr[:10]
os.chdir(r"D:\results")
filename = "results.csv"
with open(filename, "w", newline="") as file:
    write = csv.writer(file)
    write.writerows(newmatrcountr)

