# Simulación de la Máquina de Galton

Este repositorio contiene el código fuente para el Proyecto del Módulo 3: Fundamentos de Python. El objetivo de este proyecto es simular el comportamiento de una Máquina de Galton utilizando la generación de números aleatorios y graficar los resultados obtenidos mediante un histograma.

#  Cómo funciona el programa

El código fue desarrollado estrictamente en Python, dividiendo la lógica en dos funciones principales para mantener el código modular, legible y escalable:

* **`simular_canicas(cantidad_canicas, niveles)`**: Esta función es el motor matematico del proyecto. Utiliza un ciclo anidado para iterar sobre 3,000 canicas y 12 niveles de obstáculos. En lugar de utilizar funciones estadísticas predefinidas (como `normal()`), el recorrido de cada canica se decide evaluando una probabilidad discreta equitativa (50/50) en cada nivel mediante `random.randint(0, 1)`. Los resultados individuales se van acumulando para determinar el contenedor final de cada canica.
* **`graficar_histograma(resultados)`**: Toma la lista generada por la función anterior y utiliza la librería `matplotlib.pyplot` para renderizar el histograma. Se configuraron 13 rangos (bins) para centrar correctamente los datos en los contenedores correspondientes (del 0 al 12), añadiendo los títulos y etiquetas de ejes correspondientes para una fácil lectura de la distribución binomial resultante.

# Requisitos para ejecutar
* Python 3.x
* Librería Matplotlib (`pip install matplotlib`)

#  Reflexiones del Bootcamp

Hasta este punto, el bootcamp ha sido una experiencia de aprendizaje bastante interesante, en este proyecto me sentia mas confiado al punto en que hice la mayor parte del codigo rapidamente, pero mi fallo fue la cuestion del modulo matplotlib, al momento de correrlo me di cuenta que no estaba instalado, intente instalarlo pero lo confundi con extensiones y me puse a verificar diferentes tipos de extensiones con el mismo nombre sin exito, hasta que recorde que era un MODULO no una extension, ingrese a la lista piplist y vi que en efecto este no estaba instalado.

Despues de haberlo instalado sentia que ya estaba completo el proyecto pero justo por mi sobre confianza y por distraerme en poner los comentarios me faltaron poner algunas partes funcionales en el codigo a pesar de si haber puesto los comentarios sobre estas partes, mi cerebro estaba tan enfocado en un aspecto, que paso de alto otros.

Al final se pudo resolver y el proyecto fue satisfactorio de completar, me hizo darme cuenta de que no me puedo confiar tanto porque esa sobre confianza puede costarme bastante tiempo.