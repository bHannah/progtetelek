def minimum_kivalasztas():
    db = 0
    vege = 0
    min = 0
    szam = 1
    while szam != vege:
        szam = int(input('Szám: '))
        if szam < min:
            min = szam
        db += 1
    print(f'{db} számból a legkisebb: {min}')

def minimum_kivalasztas_2():
    db = 0
    vege = 0
    min = 0
    szam = int
    while (szam := int(input('Szám: '))) != vege:
        if szam < min:
            min = szam
        db += 1
    print(f'{db} számból a legkisebb: {min}')