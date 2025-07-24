'''print("Hello Ty")'''

n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))

print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus")
choice = input("Enter operation (1/2/3/4/5): ")

if choice == '1':
    print("Result:", n1 + n2)
elif choice == '2':
    print("Result:", n1 - n2)
elif choice == '3':
    print("Result:", n1 * n2)
elif choice == '4':
    print("Result:", n1 / n2)
elif choice == '5':
    print("Result:", n1 % n2)
else:
    print("Invalid choice")
