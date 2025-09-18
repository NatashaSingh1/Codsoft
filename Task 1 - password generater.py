import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

   
    characters = string.ascii_letters + string.digits + string.punctuation

    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        print("\nGenerated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()


print("Welcome to the Simple Calculator")

num1 = input("Enter the first number: ")
try:
    num1 = float(num1)
except:
    print("Invalid input. Please enter a valid number.")
    exit()


num2 = input("Enter the second number: ")
try:
    num2 = float(num2)
except:
    print("Invalid input. Please enter a valid number.")
    exit()

print("Choose operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

choice = input("Enter your choice (1/2/3/4): ")


if choice == '1':
    result = num1 + num2
    print("Result: ", result)
elif choice == '2':
    result = num1 - num2
    print("Result: ", result)
elif choice == '3':
    result = num1 * num2
    print("Result: ", result)
elif choice == '4':
    if num2 == 0:
        print("Error: Division by zero not allowed.")
    else:
        result = num1 / num2
        print("Result: ", result)
else:
    print("Invalid choice.")
