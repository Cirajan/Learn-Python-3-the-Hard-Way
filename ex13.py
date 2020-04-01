from sys import argv

script, first, second, third, fourth = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("The fourth variable:", fourth)

fifth = input("Enter the fifth variable: ")

print(second, fourth, fifth)
