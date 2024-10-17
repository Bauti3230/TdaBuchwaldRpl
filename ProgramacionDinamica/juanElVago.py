"""
Juan es ambicioso pero también algo vago. 
Dispone de varias ofertas de trabajo diarias, pero no quiere trabajar dos días seguidos. 
Dado un arreglo con el monto esperado a ganar cada día, determinar, por programación dinámica, 
el máximo monto a ganar, sabiendo que no aceptará trabajar dos días seguidos. 
Hacer una reconstrucción para verificar qué días debe trabajar. 
Indicar y justificar la complejidad del algoritmo implementado

Ejemplo:
Para: [100, 5, 50, 1, 1, 200]
Devolver: [0, 2, 5]

dp[i] = max(v[i] + dp[i-2],dp[i-1])
"""

def juan_el_vago(trabajos):
    n = len(trabajos)
    if n == 0:
        return []
    
    dp = [0] * n
    dp[0] = trabajos[0]
    if n == 1:
        elecciones = [0]*n
        elecciones[0] = 0
        return elecciones

    dp[1] = max(trabajos[0],trabajos[1])

    for i in range(2,n):
        dp[i] = max(trabajos[i] + dp[i-2],dp[i-1])

    elecciones = []
    d = len(dp) - 1
    while d >= 0:
        opt_ayer = dp[d-1] if d>0 else 0
        opt_anteayer = dp[d-2] if d>1 else 0
        valor_hoy = trabajos[d]
        if valor_hoy + opt_anteayer >= opt_ayer:
            elecciones.insert(0,d)
            d-=2
        else:
            d-=1

    return elecciones