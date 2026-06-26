import random
import matplotlib.pyplot as plt

def simular_canicas(cantidad_canicas, niveles):
    """
    Simula la caida de canidas a traves de una maquina de Galton
    y devuelve la distribucion de canicas en los niveles/contenedores finales.  
    """
    resultados = []

    # Replicamos la cantidad de canicas en la maquina
    for _ in range(cantidad_canicas):
        posicion_contenedor = 0  # Comenzamos en el contenedor central

        # en cada nivel, la canica puede ir a la izquierda (0) o a la derecha (1)
        for _ in range(niveles):
            # Generamos un movimiento aleatorio: izquierda o derecha
            decision = random.randint(0, 1)
            posicion_contenedor += decision
        # Guardamos la posicion final (contenedor) de la canica
        resultados.append(posicion_contenedor)
        
    return resultados

def graficar_histograma(resultados):
    """
    Recibe la lista de resultados de la simulacion y genera un histograma
    """
    # se cre el histograma a base de los resultados
    # Usamos 13 'bins' para representar los 13 contenedores posibles (0 a 12)
    # El parametro 'range' asegura que las barras queden centradas en numeros enteros
    plt.hist(resultados, bins=13, range=(-0.5, 12.5), edgecolor='black', color='#1f77b4')
    
    # Configuramos los encabezados y etiquetas de los ejes
    plt.title("Simulacion de la Maquina de Galton")
    plt.xlabel("Distribucion de Canicas (Contenedores)")
    plt.ylabel("Cantidad de Canicas")

    # Mostramos la grafica en pantalla
    plt.show()

# --- Ejecucion del programa ---

# 1. Definimos la cantidad de canicas y niveles
total_canicas = 3000
total_niveles = 12

# 2. llamamos a la funcion de simulacion para obtener los resultados
# No se utiliza la funcion normal(), cumpliendo con los requisitos del proyecto
contenedores_finales = simular_canicas(total_canicas, total_niveles)

# 3.llamamos a la funcion de graficar para mostrar el histograma de resultados
graficar_histograma(contenedores_finales)



