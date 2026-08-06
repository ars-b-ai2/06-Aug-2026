
num = list(map(int, input("Enter numbers separated by spaces: ").split()))
highest = num[0]
second_highest = num[0]

for n in num[1:]:
    if n > highest:
        second_highest = highest
        highest = n
    elif n > second_highest and n != highest:
        second_highest = n

print("Second Highest Element:", second)