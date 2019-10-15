number=input(":")
even = 0
odd = 0

for num in number:
    if int(num)%2 == 0:
        even += 1
    else:
        odd += 1

print("Парні:"+ str(even))
print("Не:"+ str(odd))
