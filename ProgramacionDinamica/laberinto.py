"""
Dado un laberinto representado por una grilla, queremos calcular la ganancia máxima que existe desde la posición (0,0) hasta la posición NxM. 
Los movimientos permitidos son, desde la esquina superior izquierda (el (0,0)), nos podemos mover hacia abajo o hacia la derecha. 
Pasar por un casillero determinado (i, j) nos da una ganancia de V_{i,j}. 
Implementar un algoritmo que, por programación dinámica, obtenga la máxima ganancia a través del laberinto. 
Hacer una reconstrucción del camino que se debe transitar. 
Indicar y justificar la complejidad del algoritmo implementado. 
Si hay algunos lugares por los que no podemos pasar (obstáculos), ¿cómo se debe modificar para resolver el mismo problema?

dp[i][j] = max(laberinto[i][j] + dp[i-1][j],laberinto[i][j] + dp[i][j])
"""

def laberinto(matriz):
    n = len(matriz)
    if n == 0:
        return 0
    m = len(matriz[0])
    
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = matriz[0][0]

    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + matriz[i][0]

    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + matriz[0][j]

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matriz[i][j]

    return dp[n-1][m-1]