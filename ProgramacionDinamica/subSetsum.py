"""
F(i,j) = max(F(i-1,j),F(i-1,j-vi)+vi)

Tenemos un conjunto de números v_1, v_2, …, v_n, 
y queremos obtener un subconjunto de todos esos números tal que su suma sea igual o menor a un valor V, 
tratando de aproximarse lo más posible a V. Implementar un algoritmo que, por programación dinámica, 
reciba un arreglo de valores, y la suma objetivo V, 
y devuelva qué elementos deben ser utilizados para aproximar la suma lo más posible a V, sin pasarse. 
Indicar y justificar la complejidad del algoritmo implementado.
"""

def subset_sum(elementos, V):
    n = len(elementos)
    if n == 0 or V == 0:
        return []
    
    dp = [[0] * (V + 1) for _ in range(n + 1)]
    resto = V

    for i in range(1,n+1):
        for j in range(1,V+1):
            valor_actual = elementos[i-1]
            if valor_actual > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-valor_actual]+valor_actual)

    elementos_seleccionados = []
    j = V
    for i in range(n, 0, -1): 
        if dp[i][j] != dp[i-1][j]:  
            elementos_seleccionados.append(elementos[i-1])  
            j -= elementos[i-1][1]  

    return elementos_seleccionados[::-1]