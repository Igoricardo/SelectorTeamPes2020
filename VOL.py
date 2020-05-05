from random import shuffle

VOL = [
    'A. Romao',
    'L. Paredes',
    'E. Dier',
    'L. Tousart',
    'O. Akichi',
    'D. De Rossi',
    'G. Xhaka',
    'V. Wanyama',
    'J. Hendrix',
    'Rúben Neves',
    'L. Torreira',
]

shuffle(VOL)
VOL_sorteado = VOL[0]

VOL2 = [
    'A. Romao',
    'L. Paredes',
    'E. Dier',
    'L. Tousart',
    'O. Akichi',
    'D. De Rossi',
    'G. Xhaka',
    'V. Wanyama',
    'J. Hendrix',
    'Rúben Neves',
    'L. Torreira',
]

shuffle(VOL2)
VOL2_sorteado = VOL2[0]

while VOL_sorteado in VOL2_sorteado or VOL2_sorteado in VOL_sorteado:

    if VOL_sorteado in VOL2_sorteado:
        shuffle(VOL)
        VOL_sorteado = VOL[0]

    elif VOL_sorteado not in VOL2_sorteado:
        VOL_sorteado = VOL[0]
        break

    if VOL2_sorteado in VOL_sorteado:
        shuffle(VOL2)[0]
        VOL2_sorteado = VOL2

    elif VOL2_sorteado not in VOL_sorteado:
        VOL2_sorteado = VOL2[0]
        break
