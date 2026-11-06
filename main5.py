list=list(map(int, input("Ведіть список цілих чисел: ").split()))
v=0

for i in range(len(list)):
    if list[i]!=0:
        list[i], list[v]=list[v], list[i]
        v+=1
print(*list)
