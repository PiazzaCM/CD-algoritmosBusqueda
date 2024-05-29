import time

def buscar_elemento(arr, n, elemento):
    # Iterando a través del array
    for i in range(n):
        # Comparando cada elemento del array con el elemento a buscar
        if arr[i] == elemento:
            # Si el elemento se encuentra, devolver su posición
            return i
    # Si el elemento no se encuentra, devolver -1
    return -1

# Función principal para probar el código
if __name__ == '__main__':
    # Definir un array
    arr = [1, 8, 3, 11, 5, 6, 7, 2, 9, 10]
    # Definir el tamaño del array
    n = 10
    # Elemento a buscar
    buscar = 2
    
    # Capturar el tiempo inicial
    inicio = time.time()
    
    # Llamando a la función de búsqueda
    posicion = buscar_elemento(arr, n, buscar)
    
    # Capturar el tiempo final
    fin = time.time()
    
    if posicion != -1:
        print("Se ha encontrado el número", buscar, "en la posición", posicion)
    else:
        print("No se ha encontrado el número", buscar)
    
    # Calcular el tiempo transcurrido
    tiempo_transcurrido = fin - inicio
    print("Tiempo transcurrido:", tiempo_transcurrido, "segundos")
