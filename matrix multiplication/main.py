# Column number of first matrix must be equal to row number of second matrix
arr1 = []
arr2 = []
result = []


def multiplication(arr1, arr2, result):
    for i in range(row1):
        result.append([])
        for j in range(column2):
            result[i].append(0)
    for i in range(len(arr1)):                                              # Multiplication process happens here.
        for j in range(len(arr2)):
            for k in range(len(arr2[0])):
                result[i][j] += int(arr1[i][k] * arr2[j][k])
    return result


column1 = input("Enter the column number of first matrix:")
row1 = input("Enter the row number of first matrix : ")
column2 = input("Enter the column number of second matrix: ")               # Prompting the matrix sizes from user.
row2 = input("Enter the row number of second matrix: ")

column1, row1, column2, row2 = int(column1), int(row1), int(column2), int(row2)  # Making some data type transformations

for i in range(row1):
    arr1.append([])
    for j in range(column1):
        arr1[i].append(0)
for i in range(column2):            # Assigning some elements to lists for avoid the index out of range error.
    arr2.append([])
    for j in range(row2):
        arr2[i].append(0)

if column1 != row2:
    print("These two matrix can not be multiplied.")        # Our logical/mathematical condition.
else:
    for i in range(row1):
        for j in range(column1):
            arr1[i][j] = float(input("Enter the first matrix's  " + str(i) + "x" + str(j) + " component : "))

    for i in range(column2):                # Prompting matrix contents from user.
        for j in range(row2):
            arr2[i][j] = float(input("Enter the second matrix's  " + str(j) + "x" + str(i) + " component : "))
    conclusion = multiplication(arr1, arr2, result)   # Calling the multiplication function.

    for i in range(len(conclusion)):
        print(conclusion[i])   # Printing the result to screen.
