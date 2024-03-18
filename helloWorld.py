def validate_name(name):
 
    name_parts = name.split()
        
    if len(name_parts) != 2:
        return False
    
    if not all(part.isalpha() for part in name_parts):
        return False
    
    return True

while True:
    name = input("Enter your full name: ")
    if validate_name(name):
        break
    else:
        print("Invalid name format. Please enter your first and last name separated by a space.")

print("Your name is:", name)