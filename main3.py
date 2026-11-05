string=input("Введіть рядок: ").split()
string.sort(key=len)
print(", ".join(string))
