def no_la_comen(tablero, fil, col, n):
    for i in range(col):
        if tablero[fil][i] == 1:  
            return False

    
    for i, j in zip(range(fil, -1, -1), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False

    for i, j in zip(range(fil, n), range(col, -1, -1)):
        if j >= 0 and tablero[i][j] == 1:  
            return False

    return True

def _nreinas(tablero, n, col, cant_reinas):
    if cant_reinas == n:  
        return True
    
    for i in range(n):  
        if no_la_comen(tablero, i, col, n):  
            tablero[i][col] = 1  

            if _nreinas(tablero, n, col + 1, cant_reinas + 1):  
                return True
            
            tablero[i][col] = 0  
    return False

def nreinas(n):    
    tablero = [[0 for _ in range(n)] for _ in range(n)]  
    if not _nreinas(tablero, n, 0, 0):  
        return []  
    
    posiciones = []
    for col in range(n):
        for fila in range(n):
            if tablero[fila][col] == 1:
                posiciones.append((fila, col))
    return posiciones  