import requests
import os
import json
import webbrowser

def buscar_pokemon(nombre):
    """
    Consume la API de pokeapi.co para obetener información de un Pokémon por su nombre.
    Maneja adecuadamente los status codes del protocolo HTTP.
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"

    try:
        # Peticion HTTP a la API usando la libreria requests
        respuesta = requests.get(url)

        # Validacion correcta de status codes
        if respuesta.status_code == 200:
            # Si el status es 200 (ok), devolvemos los datos en formato JSON
            return respuesta.json()
        elif respuesta.status_code == 404:
            # Si el status es 404 (not found), mandamos mensaje de error
            print("\n[!] Error: El Pokémon introducido no existe. Verifica el nombre.")
            return None
        else:
            # Manejo de cualquier otro codigo de error HTTP
            print(f"\n[!] Error de conexión. Status code HTTP: {respuesta.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"\n[!] Ocurrió un problema crítico al intentar conectar con la API: {e}")
        return None
def mostrar_datos(datos):
    """
    Muestra la informacion del pokemons desde la API en la consola y abre la imagen del pokemon en el navegador.
    """
    print(f"\n--- POKÉDEX: {datos['name'].capitalize()} ---")

    # Mostramos informacion basica del pokemon (Peso y Tamaño)
    print(f"Peso: {datos['weight']} hectogramos")
    print(f"Tamaño: {datos['height']} decímetros")

    print("\nTipos:")
    for tipo in datos['types']:
        print(f"- {tipo['type']['name'].capitalize()}")

    print("\nHabilidades:")
    for habilidad in datos['abilities']:
        print(f"- {habilidad['ability']['name'].capitalize()}")

    print("\nMovimientos (Mostrando los primeros 5):")
    for movimiento in datos['moves'][:5]:
        print(f" - {movimiento['move']['name'].capitalize()}")

    # Extraemos la URL de la imagen del Pokémon
    url_imagen = datos['sprites']['front_default']

    if url_imagen:
        print(f"\nLink de imagen frontal: {url_imagen}")
        # Muestra una imagen desde el link del recurso abriéndola en el navegador
        webbrowser.open(url_imagen)
    else:
        print("\n[!] Este Pokémon no tiene una imagen frontal registrada en la API.")

def guardar_informacion(datos):
    """
    Crea un archivo dentro del sistema y guarda toda la informacion en un archivo JSON. dentro de la carpeta 'Pokedex'
    """
    nombre_carpeta = "Pokedex"

    # Verificamos si la carpeta 'Pokedex' existe, si no, la creamos
    if not os.path.exists(nombre_carpeta):
        os.makedirs(nombre_carpeta)
        print(f"\n[+] Carpeta '{nombre_carpeta}' creada exitosamente.")
    
    # Estructura del nombre del archivo JSON
    nombre_archivo = f"{datos['name']}.json"
    ruta_completa = os.path.join(nombre_carpeta, nombre_archivo)

    # Guardamos la informacion obtenida (incluyendo el link de la imagen) en un archivo JSON
    with open(ruta_completa, 'w', encoding= 'utf-8') as archivo:
        json.dump(datos, archivo, indent=4)

    print(f"[*] Los datos se han guardado exitosamente en el archivo: {ruta_completa}")

def main():
    """
    Función principal que ejecuta el flujo del programa.
    """
    print("=== Bienvenido a la Pokedex ===")
    nombre_pokemon = input("Introduce el nombre del Pokémon que deseas buscar: ")

    # Buscamos la información del Pokémon usando la API
    datos_pokemon = buscar_pokemon(nombre_pokemon)

    if datos_pokemon:
        # Mostramos la información obtenida en consola y abrimos la imagen en el navegador
        mostrar_datos(datos_pokemon)

        # Guardamos la información en un archivo JSON dentro de la carpeta 'Pokedex'
        guardar_informacion(datos_pokemon)

# Punto de entrada del programa
if __name__ == "__main__":
    main()

    
