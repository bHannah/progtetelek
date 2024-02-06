def tizzel_oszthato():
    also = 42
    felso= 67
    while also <= felso and not(also % 10 == 0):
        also += 1
    if also <= felso:
        print(f'van 0-ra végződő szám:  {also}')
    else:
        print(f'nincs 0-ra végződő')