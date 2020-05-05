from random import shuffle

MAT = [
    'Ronaldinho G.',
    'K. De Bruyne',
    'Salva Sevilla',
    'S. Khaoui',
    'K. Havertz',
    'T. Kubo',
    'Ronaldinho G. (Fim de Carreira)',
    'M. Ozil',
    'G. Sigurdsson',
    'M. Reus',
    'N. Fekir',
    'Talisca',
    'D. Alli',
    'G. Til',
]

shuffle(MAT)
MAT_sorteado = MAT[0]

MAT2 = [
    'Ronaldinho G.',
    'K. De Bruyne',
    'Salva Sevilla',
    'S. Khaoui',
    'K. Havertz',
    'T. Kubo',
    'Ronaldinho G. (Fim de Carreira)',
    'M. Ozil',
    'G. Sigurdsson',
    'M. Reus',
    'N. Fekir',
    'Talisca',
    'D. Alli',
    'G. Til',
]

shuffle(MAT2)
MAT2_sorteado = MAT2[0]

while MAT_sorteado in MAT2_sorteado or MAT2_sorteado in MAT_sorteado:

    if MAT_sorteado in MAT2_sorteado:
        shuffle(MAT)
        MAT_sorteado = MAT[0]
    
    elif MAT_sorteado not in MAT2_sorteado:
        MAT_sorteado = MAT[0]
        break

    if MAT2_sorteado in MAT_sorteado:
        shuffle(MAT2)
        MAT2_sorteado = MAT2[0]

    elif MAT2_sorteado not in MAT_sorteado:
        MAT2_sorteado = MAT2[0]
        break
