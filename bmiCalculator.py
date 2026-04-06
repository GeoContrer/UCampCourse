# Vamos a añadir un bucle para que el usuario pueda calcular su indice de masa corporal varias veces sin tener que reiniciar el programa

while True:
    name = input("\n¿Cuál es su nombre? ").strip()
    firstlastname = input("¿Cuál es su apellido paterno? ").strip()
    secondlastname = input("¿Cuál es su apellido materno? ").strip()

    # Verificamos que el usuario introduzca los valores adecuados para el nombre, apellido paterno y apellido materno, si no lo hace, se le pedira que vuelva a introducir los datos
    if not name or not firstlastname or not secondlastname:
        print("Por favor, verifique que haya ingresado todos los datos requeridos.")
        continue

    # Aqui solicitamos los datos de edad, peso y altura para calcular el indice de masa corporal
    try:
        age = int(input("Cual es su edad? "))
        weight = float(input("Cual es su peso en kg? "))
        height = float(input("Cual es su altura en metros? "))

        # Ahora validamos que los valores no sean negativos o cero
        if age <= 0 or weight <= 0 or height <= 0:
            print("Por favor, ingrese valores mayores a cero para edad, peso y altura.")
            continue

        # Establece el indice de masa corporal
        bmi = weight / (height ** 2)

        # Establecemos los valores if y else if para determinar el resultado del indice de masa corporal y dar el resultado al usuario con su nombre completo
        # y en que estado se encuentra su indice de masa corporal

        # utilizamos if y else if para determinar el resultado del indice de masa corporal haciendo basicamente una
        #  cadena de if y else if para determinar el resultado del indice de masa corporal y dar el resultado al usuario con su nombre completo
        if bmi <= 18.49:
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

        repeat = input("\nDesea calcular su indice de masa corporal nuevamente? (si/no): ").lower()
        if repeat != "si":
            print("Gracias por usar el calculador de indice de masa corporal. ¡Hasta luego!")
            break
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos para edad, peso y altura.")
        continue




