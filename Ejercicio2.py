def convertir_coordenadas(coordenada):
    letras = 'ABCDEFGH'
    columna = letras.index(coordenada[0])
    fila = int(coordenada[1]) - 1
    return fila, columna

def es_movimiento_valido(posicion_inicio, posicion_final):
    fila_inicio, columna_inicio = posicion_inicio
    fila_final, columna_final = posicion_final

    # Verificar si la diferencia entre las filas y las columnas es la misma para diagonales
    if abs(fila_final - fila_inicio) == abs(columna_final - columna_inicio):
        return True
    else:
        return False

# Ejemplo de uso
if __name__ == "__main__":
    # Ingresa la posición de partida y posición final del alfil en formato (fila, columna)
    
    inicio = input("Ingrese la posicion inicial: ")
    final = input("Ingrese la posicion final: ")
    posicion_inicio = convertir_coordenadas(inicio) #'A1')  # Coordenada inicial
    posicion_final = convertir_coordenadas(final) #'H8')  # Coordenada final

    if es_movimiento_valido(posicion_inicio, posicion_final):
        print("El movimiento es válido para el alfil en el tablero de ajedrez.")
    else:
        print("El movimiento no es válido para el alfil en el tablero de ajedrez.")
