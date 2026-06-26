#Geovanni_Mendez_proyectoM2.py

#--- Reto 1: Longitud de una frase ---
# Programa para identificar la longitud de una frase ingresada.

def veriificar_longitud():
    palabra = input("Ingrese una palabra: ")
    longitud = len(palabra)
    
    #validamos si la longitud esta en el rando de 4 a 8 caracteres
    if 4 <= longitud <= 8:
        print("La palabra es correcta.")
    #si la longitud es menor a 4 caracteres
    elif longitud < 4:
        print(f"Hacen falta letras. solotienes {longitud} letras.")
    #si la longitud es mayor a 8 caracteres
    else:
        print(f"Te pasaste de letras. Tienes {longitud} letras.")

# --- Reto 2: Encuentra el cuadrante ---
# Programa para identificar el cuadrante basado en coordenadas X e Y

def encontrar_cuadrante():
    print("\n--- encuentra el cuadrante ---")

    # Ahora solicitamos coordenadas y convertimos a float para permitir decimales
    x = float(input("Ingrese la coordenada X: "))
    y = float(input("Ingrese la coordenada Y: "))

    # verificamos que ninguna coordenada sea cero
    if x == 0 or y == 0:
        print("Error: Las coordenadas no pueden ser cero.")

    # Logica de cuadrantes
    elif x > 0 and y > 0:
        print("El punto se encuentra en el primer cuadrante.")
    elif x < 0 and y > 0:
        print("El punto se encuentra en el segundo cuadrante.")
    elif x < 0 and y < 0:
        print("El punto se encuentra en el tercer cuadrante.")
    elif x > 0 and y < 0:
        print("El punto se encuentra en el cuarto cuadrante.")

# Ejecucion de las funciones
if __name__ == "__main__":
    veriificar_longitud()
    encontrar_cuadrante()
