# Vamos a añadir un bucle para que el usuario pueda calcular su indice de masa corporal varias veces sin tener que reiniciar el programa

while   True: 
    name = input("Cual es su nombre? ")
    firstlastname = input("Cual es su apellido paterno? ")
    secondlastname = input("Cual es su apellido materno? ") 

# Aqui solicitamos los datos de edad, peso y altura para calcular el indice de masa corporal
    age = int(input("Cual es su edad? "))
    weight = float(input("Cual es su peso en kg? "))
    height = float(input("Cual es su altura en metros? "))

# Establece el indice de masa corporal
    bmi = weight / (height ** 2)

# Establecemos los valores if y else if para determinar el resultado del indice de masa corporal y dar el resultado al usuario con su nombre completo
# y en que estado se encuentra su indice de masa corporal

# utilizamos if y else if para determinar el resultado del indice de masa corporal haciendo basicamente una
#  cadena de if y else if para determinar el resultado del indice de masa corporal y dar el resultado al usuario con su nombre completo
    if bmi <=18.49:
           print(f"{name} {firstlastname} {secondlastname}, su indice de masa corporal es {bmi:.2f} y se encuentra en estado de peso bajo.")
    elif bmi >= 18.50 and bmi <= 24.99:
           print(f"{name} {firstlastname} {secondlastname}, su indice de masa corporal es {bmi:.2f} y se encuentra en estado de peso normal.")
    elif bmi >= 25.00 and bmi <= 29.99:
           print(f"{name} {firstlastname} {secondlastname}, su indice de masa corporal es {bmi:.2f} y se encuentra en estado de sobrepeso.")
    elif bmi >= 30.00 and bmi <= 34.99:
           print(f"{name} {firstlastname} {secondlastname}, su indice de masa corporal es {bmi:.2f} y se encuentra en estado de obesidad leve.")
    elif bmi >= 35.00 and bmi <= 39.99:
           print(f"{name} {firstlastname} {secondlastname}, su indice de masa corporal es {bmi:.2f} y se encuentra en estado de obesidad media.")
    elif bmi >= 40.00:
           print(f"{name} {firstlastname} {secondlastname}, su indice de masa corporal es {bmi:.2f} y se encuentra en estado de obesidad morbida.")

    repeat = input("\nDesea calcular su indice de masa corporal nuevamente? (si/no): ").lower ()
    if repeat != "si":
     print("Gracias por usar el calculador de indice de masa corporal. ¡Hasta luego!")
     break


 
    
