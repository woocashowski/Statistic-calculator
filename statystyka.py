from statistics import mode
from math import sqrt
from statistics import variance
import sys

t = sys.argv[1]
try:
    file = open(t, "r")
except:
    print("Brak pliku")
    exit(0)
output = sys.argv[2]
input = []
for i in file:
    if i is not "":
        input.append(float(i))
file.close()
print(input)

fileoutput = open(output, "w")
# Liczby:
fileoutput.write("Dane:\n")
fileoutput.write(str(input))


# print("Tabela:")
# print(input)

# średnia
# print("\nŚrednia:\n")
def mean(numList):
    finalMean = 0.0

    for num in numList:
        finalMean += int(num)
    finalMean = finalMean / float(len(numList))
    return finalMean


fileoutput.write("\nŚrednia:\n")
fileoutput.write(str(mean(input)))
print(mean(input))


# mediana (wartość środkowa)
# print("\nMediana:\n")
def median(numList):
    tempList = sorted(numList)
    index = (len(tempList) - 1) // 2

    if len(tempList) % 2 == 0:
        return "{0:.4f}".format((tempList[index] + tempList[index + 1]) / 2.0)
    else:
        return tempList[index]


# print(median(input))
fileoutput.write("\nMediana:\n")
fileoutput.write(str(median(input)))

# moda
try:
    k = mode(input)
    # print("Moda:")
    # print(mode(input))
    fileoutput.write("\nModa:\n")
    fileoutput.write(str(mode(input)))
except:
    print("")
    # print("brak")


# odchylenie standardowe
# print("Odchylenie standardowe:")
def standardDeviation(numList):
    newMean = float(mean(numList))
    tempList = [0 for n in range(len(numList))]
    finalDeviation = 0

    for q, r in enumerate(numList):
        tempList[q] = float((numList[q] - newMean) ** 2)

    finalDeviation = sqrt(float(mean(tempList)))

    # print "{0:.4f}".format(finalDeviation)
    return finalDeviation


# print(standardDeviation(input))
fileoutput.write("\nOdchylenie standardowe:\n")
fileoutput.write(str(standardDeviation(input)))

# wariancja
# print("Wariancja:")
# print(variance(input))
fileoutput.write("\nWariancja:\n")
fileoutput.write(str(variance(input)))

file.close()
