# Proyecto: Construye una Pokédex 

Este proyecto es una aplicación de terminal desarrollada en Python que funciona como una Pokédex digital. Su función principal es consultar la API pública [PokeAPI](https://pokeapi.co/) para obtener, mostrar y almacenar información detallada de cualquier Pokémon ingresado por el usuario.

# ¿Cómo se hizo?
El proyecto fue construido utilizando Python y hace uso de peticiones HTTP para extraer datos en tiempo real de la base de datos de PokeAPI. 

El flujo de la aplicación es el siguiente:
1. Se le solicita al usuario el nombre de un Pokémon.
2. El script valida la petición manejando los **status codes**. Si el Pokémon no existe (Error 404), informa al usuario sin romper el programa.
3. Si la búsqueda es exitosa (Status 200), extrae estadísticas como peso, tamaño, movimientos, habilidades, tipos y el link de la imagen frontal.
4. Despliega la información en la consola y automáticamente abre la imagen del Pokémon en el navegador web predeterminado.
5. Finalmente, crea de manera automática una carpeta llamada `pokedex` (si no existe) y guarda toda la información consumida en un archivo `.json` con el nombre del Pokémon.

# Bibliotecas necesarias
Para ejecutar este proyecto, necesitas tener instalado Python en tu sistema. Además, el programa requiere la siguiente biblioteca externa que no viene en la biblioteca estándar de Python:

* `requests`: Utilizada para realizar las peticiones HTTP a la API.

Puedes instalarla ejecutando el siguiente comando en tu terminal:
```bash
pip install requests

#  Reflexiones del Bootcamp
este proyecto personalmente fue mas interesante dado que me gusta pokemon, puedo ver la funcionalidad de esto para otros temas como calabozos y dragones, para ayudar a encontrar la informacion especifica de hechizos, habilidades, etc. al solo buscarlos, sera cuestion de buscar una API con la que pueda usar esto. Fuera de esto, fue complicado una vez mas por la cuestion de los modulos, esta ves si lo instale desde un inicio pero por alguna razon seguia marcando que no esta instalada, tuve que buscar en internet por soluciones hasta que encontre la siguiente: 

& C:\Users\URUSERNAMEdontSTEALmyDATA\AppData\Local\Python\pythoncore-3.14-64\python.exe -m pip install requests

que es el instalar la libreria con la ruta exacta, tarde un buen rato investigando esto y otros detalles de este proyecto en especifico porque el ejemplo en el documento de requerimientos por alguna razon nunca quizo cargar, de igual manera creo que fue bueno el poder investigar porque pude aprender bastante en el proceso, fue algo tardado pero valio la pena, esta clase de proyectos que estan mas cerca de mis gustos y a los cuales les puedo ver utilidad me animan mas a lo que esta por venir.