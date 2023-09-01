# Time complexity O(n)

import numpy as np

def MergeSort(arrayNumbers):
    if len(arrayNumbers) == 1 or len(arrayNumbers) == 0:
        return arrayNumbers

    leftArray = MergeSort(arrayNumbers[: len(arrayNumbers) // 2])
    rightArray = MergeSort(arrayNumbers[len(arrayNumbers) // 2 :])

    newArray = []
    while len(leftArray) > 0 and len(rightArray) > 0:
        if len(leftArray) == 0:
            newArray.append(rightArray.pop(0))

        elif len(rightArray) == 0:
            newArray.append(leftArray.pop(0))

        elif leftArray[0] <= rightArray[0]:
            newArray.append(leftArray.pop(0))

        else:
            newArray.append(rightArray.pop(0))

    if len(leftArray) > 0:
        newArray.extend(leftArray)

    elif len(rightArray) > 0:
        newArray.extend(rightArray)

    return newArray

if __name__ == "__main__":
    arrayNumbers = np.random.randint(200, size=(12)).tolist()
    print(arrayNumbers)
    sortedArray = MergeSort(arrayNumbers)
    print(sortedArray)