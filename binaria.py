import time

def buscar_elemento(ordenar_arr, n, elemento):
    inicio = 0
    fin = n - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if ordenar_arr[medio] == elemento:
            return medio
        elif ordenar_arr[medio] < elemento:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 10
    buscar = 2
    
    inicio = time.time()  # Capturando el tiempo inicial
    
    posicion = buscar_elemento(arr, n, buscar)
    
    fin = time.time()  # Capturando el tiempo final
    
    if posicion != -1:
        print("Se ha encontrado el número", buscar, "en la posición", posicion)
    else:
        print("No se ha encontrado el número", buscar)
    
    tiempo_transcurrido = fin - inicio  # Calculando el tiempo transcurrido
    print("Tiempo transcurrido:", tiempo_transcurrido, "segundos")
