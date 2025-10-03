cont = "y"
print("Welcome to the Star Pyramid Generator!")
print()

while cont == "y":
    num = int(input("Enter a number: "))

    t = 0
    i = 1
    k = num

    while i <= num:
        # Print leading spaces
        print(" " * k, end="")
        
        # Print stars
        for j in range(t + 1):
            print("*", end=" ")
        
        # Move to the next line
        print()
        
        # Update variables for the next row
        i += 1
        t += 1
        k -= 1

    cont = input("Do you want to continue? (Enter 'y' to continue or 'q' to quit): ").lower()
