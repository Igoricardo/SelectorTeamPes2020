from random import shuffle

LE = [
    'R. Carlos',
    'Jordi Alba',
    'Hélder Lopes',
    'S. Kolasinac',
    'L. Spinazzola',
    'A. Robertson',
    'A. Oyongo',
    'K. Tierney',
    'F. Ballo-Touré',
    'Marcelo',
    'D. Alaba',
    'N. Tagliafico',
    'P. Van Aanholt',
    'Jonny Castro',
    'B. Mendy',
    'Angeliño',
]

shuffle(LE)
LE_sorteado = LE[0]

LE2 = [
    'R. Carlos',
    'Jordi Alba',
    'Hélder Lopes',
    'S. Kolasinac',
    'L. Spinazzola',
    'A. Robertson',
    'A. Oyongo',
    'K. Tierney',
    'F. Ballo-Touré',
    'Marcelo',
    'D. Alaba',
    'N. Tagliafico',
    'P. Van Aanholt',
    'Jonny Castro',
    'B. Mendy',
    'Angeliño',    
]

shuffle(LE2)
LE2_sorteado = LE2[0]

while LE_sorteado in LE2_sorteado or LE2_sorteado in LE_sorteado:

    if LE_sorteado in LE2_sorteado:
        shuffle(LE)
        LE_sorteado = LE[0]

    elif LE_sorteado not in LE2_sorteado:
        LE_sorteado = LE[0]
        break

    if LE2_sorteado in LE_sorteado:
        shuffle(LE2)
        LE2_sorteado = LE2[0]

    elif LE2_sorteado not in LE_sorteado:
        LE2_sorteado = LE2[0]
        break
