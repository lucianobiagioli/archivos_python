# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv
from ipaddress import summarize_address_range


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    
    
    cantidad = 0
    csvfile = open(archivo)
    stock = list(csv.DictReader(csvfile))
    for fila in stock:
        cantidad += int(fila["tornillos"])

    print("La cantidad total de tornillos es: ", cantidad)
    csvfile.close()



def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion

    dpto_2 = 0
    dpto_3 = 0

    csvfile_2 = open(archivo)
    datos = list(csv.DictReader(csvfile_2))
    for i in range(len(datos)):
        try:
            dato = int(datos[i]["ambientes"])
        except:
            print("No se encontraron datos disponibles")
        if dato == 2:
            dpto_2 += 1
        elif dato == 3:
            dpto_3 += 1

    print("La cantidad de dptos de 2 ambientes es: ", dpto_2)
    print("La cantidad de dptos de 3 ambientes es: ", dpto_3)

    csvfile_2.close()


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
