def fibonacci(n):
    if n == 0:
        return 1
    
    M_FIB = [None] * (n+1)
    M_FIB[0] = 1
    M_FIB[1] = 1

    for i in range(2, n+1):
        M_FIB[i] = M_FIB[i-1] + M_FIB[i-2] 
    return M_FIB[n]