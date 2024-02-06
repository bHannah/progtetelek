def elso_otjegyu_prim():
    prim = False
    n = 9999
    while prim == False:
        n += 1
        i = 2
        while i <= n ** 0.5 and n % i != 0:
            i += 1
        prim = i > n**0.5
    return n