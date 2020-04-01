
numbers = []


def fillList(n, x):
    for i in range(0, n):
        print(f"At the top i is {i}")
        numbers.append(i)



        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")



fillList(7, 2)

print("The numbers: ")

for num in numbers:
    print(num)
