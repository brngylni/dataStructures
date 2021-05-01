def minmax(data):
    counter = len(data)      #Finding the size of the list that holds the numbers.
    x = 0
    y = 0
    for x in range(counter - 1):
        for y in range(counter - x - 1):
            if float(data[y]) < float(data[y + 1]):    # We are looking the float equivalent of these values for the more accurate sorting.
                data[y], data[y + 1] = data[y + 1], data[y]
    min = int(data[0])
    max = int(data[-1])     #Returning the results as an integers.
    return min,max