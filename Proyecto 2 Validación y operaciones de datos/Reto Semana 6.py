errores = 0
contraseña_valida = ""

while errores < 3:
    if contraseña_valida == "":
        contraseña = input("Ingrese una contraseña: ")

        if contraseña[0].isdigit():
            contraseña_valida = contraseña
        else:
            print("La contraseña debe comenzar con un número.")
            errores += 1
    else:
        confirmacion = input("Ingrese la contraseña nuevamente: ")
        if confirmacion == contraseña_valida:
            print("Contraseña confirmada correctamente.")
            break
        else:
            print("Las contraseñas no coinciden.")
            errores += 1

print("fin del programa")            

