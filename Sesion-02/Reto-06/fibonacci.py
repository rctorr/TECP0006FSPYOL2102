n1 = 1
print(n1)
n2 = 1
print(n2)
m = 1000
n = n1 + n2
while n < 1000:
    print(n)
    n1, n2, n = n2, n, n2 + n
