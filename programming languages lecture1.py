#Sandra Wendy Katheu Kyavoa
#SCT211-0047/20022
def greet_and_add():
    # Ask for the user's name
    name = input("Please enter your name: ")
    print(f"Hello, {name}!")

    # Ask for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Add the numbers
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}.")

# Call the function to run it
greet_and_add()
