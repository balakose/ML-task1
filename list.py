# list
n=int(input("enter the number of day:"))
temperature =[]
for i in range(n):
    temp=float(input(f"enter temp for day{i+1}:"))
temperature.append(temp)

avg_temp=sum(temperature)/n

print(f"\ntemperature entered:{temperature}")
print(f"average temperature:{avg_temp:.2f}")






