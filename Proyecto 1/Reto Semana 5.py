anio_actual = int(input("Ingrese el año actual: "))
anio_cualquiera = int(input("Ingrese cualquier otro año: "))
if anio_cualquiera == anio_actual:
    print("El año es el mismo.")
elif anio_actual > anio_cualquiera:
    diferencia = anio_actual - anio_cualquiera

    if diferencia == 1:
        print(f" desde el año {anio_cualquiera} ha pasado {diferencia} año.")
    else:
        print(f" desde el año {anio_cualquiera} han pasado {diferencia} años.")
else:
    diferencia = anio_cualquiera - anio_actual
    if diferencia == 1:
        print(f" para llegar al año {anio_cualquiera} falta {diferencia} año.")
    else:
        print(f" para llegar al año {anio_cualquiera} faltan {diferencia} años.")

