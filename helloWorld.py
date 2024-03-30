while True:
    name = input("Enter your name: ")
    if name.replace(" ", "").isalpha():  # Check if the name contains only alphabetic characters and spaces
        print(name)
        break  # Exit the loop if a valid name is provided
    else:
        print("Please enter a valid name containing only letters and spaces.")
