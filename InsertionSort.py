# Time complexity O(n²)
from numpy import random

arrayNumbers = random.randint(100, size=(20))

print(arrayNumbers)

# Start on the array's second record
for i in range(1, len(arrayNumbers)):
    key = arrayNumbers[i]
    j = i - 1 # Get record before key

    # If current record is bigger than key
    while j >= 0 and arrayNumbers[j] > key:
        arrayNumbers[j + 1] = arrayNumbers[j] # Record after receive the value of the current
        j = j - 1 # go to the record before
    
    arrayNumbers[j + 1] = key # At the end, put the key on the sorted position

print(arrayNumbers)