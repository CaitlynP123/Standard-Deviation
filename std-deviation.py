import csv
import math

with open ('C:/Users/C/OneDrive/Desktop/Coding/python/Standard Deviation/project.csv', newline="") as f:
    reader = csv.reader(f)
    fileData = list(reader)

data = fileData[0]

def mean(data):         
    total = 0

    for i in data:
        total = total + int(i)

    n = len(data)
    mean = total / n

    return mean

squaredList = []
for i in data:
    a = int(i) - mean(data)
    a = a**2
    squaredList.append(a)

sum = 0
for i in squaredList:
    sum = sum+i

result = sum / (len(data) - 1)

stdDeviation = math.sqrt(result)
print(stdDeviation)

