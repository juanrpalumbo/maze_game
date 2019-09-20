base = int(input("base"))
power = int(input("power"))



to_add=1
for i in range(power):
    sum=0
    for j in range(base):
        sum=sum+to_add
    to_add=sum

print(to_add)