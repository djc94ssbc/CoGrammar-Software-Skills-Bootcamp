while True:
    name = input("Enter your name: ")
    if name.strip():  # Check if the name is not empty after stripping whitespace
        print(name)
        break  # Exit the loop if a valid name is provided
    else:
        print("Please enter a valid name.")
