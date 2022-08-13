"""
Cuenta y imprime la cantidad de caracteres que tiene un archivo dado por el usuario con un limite de caracteres modificable.
"""

print("Put END to finish the program")

while True:
    
    count = 0
    archivo = input("Enter your archive name: ")
    
    if archivo == "END":
        break
    
    try:
        archive = open(archivo)
        for i in archive:
            if count == 3000:
                print("You reach the limit of 3000 characters.")
                break
            print(i)
            count = count + 1
    except:
        print("Enter a valid archive name")
        
print(f"The total count of characters is: {count}")
