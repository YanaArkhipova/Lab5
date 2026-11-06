n=input("Введіть ціле число: ")
a=[]

for i in range(len(n)):
    b=n[:i]+n[i+1:]
    a.append(int(b))

print(max(a))
