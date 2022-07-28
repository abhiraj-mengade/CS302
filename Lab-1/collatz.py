# Name: Abhiraj Mengade
# Roll no: 201CS102

def collatz(n):
    if(n<=1):
        print(1)
        return 1
    if(n%2==0):
        print(int(n/2))
        return collatz(int(n/2))
    print(3*n +1)
    return collatz(3*n + 1)

a = int(input("Enter a number"))
collatz(a)