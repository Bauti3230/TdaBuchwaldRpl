"""
Dada una escalera, y sabiendo que tenemos la capacidad de subir escalones de a 1 o 2 o 3 pasos, encontrar, 
utilizando programación dinámica, cuántas formas diferentes hay de subir la escalera hasta el paso n.

n = 0 --> Debe devolver 1 (no moverse)
n = 1 --> Debe devolver 1 (paso de 1)
n = 2 --> Debe devolver 2 (dos pasos de 1, o un paso de 2)
n = 3 --> Debe devolver 4 (un paso de 3, o tres pasos de 1, o un paso de 2 y uno de 1, o un paso de 1 y un paso de 2)
n = 4 --> Debe devolver 7
n = 5 --> Debe devolver 13

dp[n] = dp[n-1] + dp[n-2] + dp[n-3]
"""

def escalones(n):
    if n == 0 or n == 1:
        return 1
    
    if n == 2:
        return 2
    
    if n == 3:
        return 4
    
    dp = [None] * (n+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4,n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    return dp[n]