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

if __name__ == "__main__":

    
    