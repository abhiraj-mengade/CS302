# Name: Abhiraj Mengade
# Roll no: 201CS102

def collatz(n, l):
    if(n<=1):
        print("length = " + str(l))
        return 1

    if(n%2==0):
        print(int(n/2))
        l+=1
        return collatz(int(n/2),l)
    print(3*n +1)
    l+=1
    return collatz(3*n + 1,l)

a = int(input("Enter a number"))
collatz(a,0)
