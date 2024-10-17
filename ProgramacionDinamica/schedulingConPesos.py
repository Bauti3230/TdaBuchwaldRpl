def posicion_no_conflictiva(charlas, posicion):
    inicio, fin = 0, posicion - 1

    while inicio <= fin:
        mid = (inicio + fin) // 2
        if charlas[mid][1] <= charlas[posicion][0]:
            if mid + 1 < len(charlas) and charlas[mid + 1][1] <= charlas[posicion][0]:
                inicio = mid + 1
            else:
                return mid
        else:
            fin = mid - 1
    return -1

def scheduling(charlas):
    charlas.sort(key=lambda x: x[1])

    n = len(charlas)
    if n == 0:
        return []
    
    dp = [0] * n
    dpi = [[] for _ in range(n)]

    dp[0] = charlas[0][2]  
    dpi[0] = [charlas[0]]  
    for i in range(1, n):
        # Charla a incluir
        incl = charlas[i]
        incl_profit = incl[2]

        j = posicion_no_conflictiva(charlas, i)
        if j != -1:
            incl_profit += dp[j]

        # Máximo de incluir o no incluir la charla
        if incl_profit > dp[i - 1]:
            dp[i] = incl_profit
            dpi[i] = dpi[j] + [incl] if j != -1 else [incl]
        else:
            dp[i] = dp[i - 1]
            dpi[i] = dpi[i - 1]

    return dpi[n - 1]