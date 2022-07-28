#Name: Abhiraj Mengade
#Roll no: 201CS102

def mod(a,b):
    return a%b
def mul(a,b):
    return a*b
def add(a,b):
    return a+b
def div(a,b):
    if(b==0):
        return "cannot divide by 0"
    return a/b
def main():
    while True:
        print("Select an option:"
              "1.Add"
              "2.Subtract"
              "3.Multiply"
              "4.Divide"
              "5.Modulus")
        choice = input()
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", add(num1, -num2))

            elif choice == '3':
                print(num1, "*", num2, "=", mul(num1, num2))

            elif choice == '4':
                print(num1, "/", num2, "=", div(num1, num2))
            elif choice == '5':
                print(num1, "%", num2, "=", mod(num1, num2))
        else:
            print("Invalid Input")
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break



if __name__ == '__main__':
    main()
