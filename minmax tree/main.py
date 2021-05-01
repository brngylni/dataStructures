def minmax(data):
    counter = len(data)
    x = 0
    y = 0
    for x in range(counter - 1):
        for y in range(counter - x - 1):
            if data[y] < data[y + 1]:
                data[y], data[y + 1] = data[y + 1], data[y]
    minandmax = data[0], data[-1]
    return (minandmax)


data = []
x = 0
y = int(input('Enter size :'))
number = 0

while x < y:
    number = input("Enter the number : ")
    c = int(number , 10)
    data.append(c)
    x += 1

values = minmax(data)

print("Here is the our min and max values : ", values)
