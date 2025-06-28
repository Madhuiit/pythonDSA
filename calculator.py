def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def  multiply(a,b):
    return a*b
def divide(a,b):
    #handle division by zero
    if b==0:
        return "Error : division by zero is not allowed."
    return a/b
def calculator():
    print("Simple comman line calculator")
    print(".................................")
    print("Avaiabl operation : + .-.*,/")


    try:
        #Take user input 
        num1 = float(input("Enter  the first number: "))
        operation = input("Enter the operation (+.-,*,/)").strip()
        num2 = float(input("Enter the second number :  "))

        if operation == "+":
            result =add(num1,num2)
        elif operation == "-":
            result = subtract(num1,num2)
        elif operation== "*":
            result =multiply(num1,num2)
        elif operation == "/":
            result = divide(num1,num2)
        else:
            result = "Error Inalid operation."

        print(f"REsult : {result}")
    except ValueError:
        print("Error : Invalid input .please enter numerti valus only.")
if __name__ == "__main__":
    while True:
        calculator()
        cont = input("Do you want to perform another calculation ? (y/n): ").lower()
        if cont!="y":
            print("Goodbye!")
            break




