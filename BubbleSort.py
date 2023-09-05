from numpy import random

arrayNumbers = random.randint(100, size=(20))

print(arrayNumbers)

for i in range(0, len(arrayNumbers)):

    for j in range(len(arrayNumbers) - 1, i, -1):
        if arrayNumbers[j] < arrayNumbers[j - 1]:
            temp = arrayNumbers[j]
            arrayNumbers[j] = arrayNumbers[j - 1]
            arrayNumbers[j - 1] = temp

print(arrayNumbers)