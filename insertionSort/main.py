def insertionSort(array):
    for i in range(1, len(array)):
        while(array[i] < array[i-1]):
            array[i], array[i-1] = array[i-1], array[i]
            i -= 1
    return array


list = []
prompt = 0
print("Press enter for stop the inserting process.")
while(prompt != ""):
    prompt = input("Please enter a number to add list : ")
    if(prompt.isnumeric()):
        list.append(int(prompt))
        print("Number added to list.")
    elif(not prompt.isnumeric()):
        print("This isn't a number!")

list = insertionSort(list)

for i in range(0, len(list)):
    print(list[i])