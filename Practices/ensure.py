numbers = []

for i in range(5):
    num = float(input("Enter a number: "))
    numbers.append(num)

total = sum(numbers)
average = total / len(numbers)

print("Total:", total)
print("Average:", average)