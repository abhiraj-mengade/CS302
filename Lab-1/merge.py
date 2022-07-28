
a = []
n = int(input("Enter number of elements in a: "))

for i in range(0, n):
    ele = int(input())
    a.append(ele)

b = []
n = int(input("Enter number of elements in b: "))
for i in range(0, n):
    ele = int(input())
    b.append(ele)

print(sorted(a + b))
