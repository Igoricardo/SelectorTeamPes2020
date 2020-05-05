from random import shuffle

LD = [
    'A. Florenzi',
    'R. Aguilar',
    'Dani Morer',
    'Azpilicueta',
    'Sergi Roberto',
    'João Cancelo',
    'Zeca',
    'J. Kimmich',
    'T. Alexander-Arnold',
    'Víctor Díaz',
]

shuffle(LD)
LD_sorteado = LD[0]

LD2 = [
    'A. Florenzi',
    'R. Aguilar',
    'Dani Morer',
    'Azpilicueta',
    'Sergi Roberto',
    'João Cancelo',
    'Zeca',
    'J. Kimmich',
    'T. Alexander-Arnold',
    'Víctor Díaz',
]

shuffle(LD2)
LD2_sorteado = LD2[0]

while LD_sorteado in LD2_sorteado or LD2_sorteado in LD_sorteado:

    if LD_sorteado in LD2_sorteado:
        shuffle(LD)
        LD_sorteado = LD[0]

    elif LD_sorteado not in LD2_sorteado:
        LD_sorteado = LD[0]
        break

    if LD2_sorteado in LD_sorteado:
        shuffle(LD2)
        LD2_sorteado = LD2[0]

    elif LD2_sorteado not in LD_sorteado:
        LD2_sorteado = LD2[0]
        break
