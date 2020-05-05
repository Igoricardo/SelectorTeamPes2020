from random import shuffle

SA = [
    'F. Totti',
    'Á. Recoba',
    'A. Rebic',
]

shuffle(SA)
SA_sorteado = SA[0]

SA2 = [
    'F. Totti',
    'Á. Recoba',
    'A. Rebic',
]

shuffle(SA2)
SA2_sorteado = SA2[0]

while SA_sorteado in SA2_sorteado or SA2_sorteado in SA_sorteado:

    if SA_sorteado in SA2_sorteado:
        shuffle(SA)
        SA_sorteado = SA[0]

    elif SA_sorteado not in SA2_sorteado:
        SA_sorteado = SA[0]
        break

    if SA2_sorteado in SA_sorteado:
        shuffle(SA2)
        SA2_sorteado = SA2[0]

    elif SA2_sorteado not in SA_sorteado:
        SA2_sorteado = SA2[0]
        break
