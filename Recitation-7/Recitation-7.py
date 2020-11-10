# Count Sort, Recitation 7, 10.10.2020

def countingSort(numList):

    auxList = []

    # Set a new list as the same length with all zeros
    for i in range( max(numList)+1 ):
        auxList.append(0)

    # Increment the count
    for j in range(len(numList)):
        auxList[ numList[j] ] += 1
    
    index = 0

    # Replace the values in the original list
    for k in range(len(auxList)):

        # The index (k) is the value 
        # (numList[k]) is the count

        for l in range(auxList[k]):

            numList[index] = k
            index += 1

    return numList