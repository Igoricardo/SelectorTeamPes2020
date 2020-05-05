from random import shuffle

PTD = [
    'L. Giuly',
    'L. Messi',
    'B. Raman',
    'J. Lago',
    'V. Cerny',
    'S. Villa',
    'F. Chiesa',
    'Z. Bakaev',
    'Carles Pérez',
    'M. Suleymanov',
    'G. Bale',
    'Douglas Costa',
    'Lucas Moura',
    'Suso',
    'M. Politano',
    'Williams',
    'Marlos',
    'Bernado Silva',
    'V. Tsygankov',
    'David Neres',
    'M. Salah',
]

shuffle(PTD)
PTD_sorteado = PTD[0]

PTD2 = [
    'L. Giuly',
    'L. Messi',
    'B. Raman',
    'J. Lago',
    'V. Cerny',
    'S. Villa',
    'F. Chiesa',
    'Z. Bakaev',
    'Carles Pérez',
    'M. Suleymanov',
    'G. Bale',
    'Douglas Costa',
    'Lucas Moura',
    'Suso',
    'M. Politano',
    'Williams',
    'Marlos',
    'Bernado Silva',
    'V. Tsygankov',
    'David Neres',
    'M. Salah',
]

shuffle(PTD2)
PTD2_sorteado = PTD2[0]

while PTD_sorteado in PTD2_sorteado or PTD2_sorteado in PTD_sorteado:

    if PTD_sorteado in PTD2_sorteado:
        shuffle(PTD)
        PTD_sorteado = PTD[0]

    elif PTD_sorteado not in PTD2_sorteado:
        PTD_sorteado = PTD[0]
        break

    if PTD2_sorteado in PTD_sorteado:
        shuffle(PTD2)
        PTD2_sorteado = PTD2[0]

    elif PTD2_sorteado not in PTD_sorteado:
        PTD2_sorteado = PTD2[0]
        break
