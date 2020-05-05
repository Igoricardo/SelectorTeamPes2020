from random import shuffle

MLE = [
    'P. Nedved',
    'S. Sinclair',
    'T. Castagne',
    'I. Perisic',
    'R. Pereyra',
    'Y. Carrasco',
]

shuffle(MLE)
MLE_sorteado = MLE[0]

MLE2 = [
    'P. Nedved',
    'S. Sinclair',
    'T. Castagne',
    'I. Perisic',
    'R. Pereyra',
    'Y. Carrasco',]

shuffle(MLE2)
MLE2_sorteado = MLE2[0]

while MLE_sorteado in MLE2_sorteado or MLE2_sorteado in MLE_sorteado:

    if MLE_sorteado in MLE2_sorteado:
        shuffle(MLE)
        MLE_sorteado = MLE[0]

    elif MLE_sorteado not in MLE2_sorteado:
        MLE_sorteado = MLE[0]
        break

    if MLE2_sorteado in MLE_sorteado:
        shuffle(MLE2)
        MLE2_sorteado = MLE2[0]

    elif MLE2_sorteado not in MLE_sorteado:
        MLE2_sorteado = MLE2[0]
        break
    