#Name: Abhiraj Mengade
#Roll no: 201CS102


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
a_1 = list(filter(lambda ele1: ele1 not in b, a))
b_1 = list(filter(lambda ele1: ele1 not in a, b))

print(a_1)
print(b_1)
