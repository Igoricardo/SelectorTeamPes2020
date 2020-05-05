from random import shuffle

PTE = [
    'L. Insigne',
    'Vitolo',
    'Y. Soteldo',
    'J. Brekalo',
    'N. Ampomah',
    'H. Bandé',
    'L. Sinisterra',
    'C. Ronaldo',
    'E. Hazard',
    'Taison',
    'Son Heung-Min',
    'S. Mané',
    'Q. Promes',
    'L. Sané',
    'Gonçalo Guedes',
    'Diogo Jota',
]

shuffle(PTE)
PTE_sorteado = PTE[0]

PTE2 = [
    'L. Insigne',
    'Vitolo',
    'Y. Soteldo',
    'J. Brekalo',
    'N. Ampomah',
    'H. Bandé',
    'L. Sinisterra',
    'C. Ronaldo',
    'E. Hazard',
    'Taison',
    'Son Heung-Min',
    'S. Mané',
    'Q. Promes',
    'L. Sané',
    'Gonçalo Guedes',
    'Diogo Jota',
]

shuffle(PTE2)
PTE2_sorteado = PTE2[0]

while PTE_sorteado in PTE2_sorteado or PTE2_sorteado in PTE_sorteado:

    if PTE_sorteado in PTE2_sorteado:
        shuffle(PTE)
        PTE_sorteado = PTE[0]

    elif PTE_sorteado not in PTE2_sorteado:
        PTE_sorteado = PTE[0]
        break

    if PTE2_sorteado in PTE_sorteado:
        shuffle(PTE2)
        PTE2_sorteado = PTE2[0]

    elif PTE2_sorteado not in PTE_sorteado:
        PTE2_sorteado = PTE2[0]
        break
    