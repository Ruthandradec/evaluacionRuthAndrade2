def convertir_coordenadas(coordenada):
    letras = 'ABCDEFGH'
    columna = letras.index(coordenada[0])
    fila = int(coordenada[1]) - 1
    return fila, columna


if __name__ == "__main__":

    
    