from random import shuffle

MLD = [
    'D. Beckham',
    'Pablo Sarabia',
    'Reine-Adelaide',
    'A. Schopf',
    'F. Ljungberg',
    'H. Mkhitaryan',
    'F. Thauvin',
]

shuffle(MLD)
MLD_sorteado = MLD[0]

MLD2 = [
    'D. Beckham',
    'Pablo Sarabia',
    'Reine-Adelaide',
    'A. Schopf',
    'F. Ljungberg',
    'H. Mkhitaryan',
    'F. Thauvin',
]

shuffle(MLD2)
MLD2_sorteado = MLD2[0]

while MLD_sorteado in MLD2_sorteado or MLD2_sorteado in MLD_sorteado:

    if MLD_sorteado in MLD2_sorteado:
        shuffle(MLD)
        MLD_sorteado = MLD[0]

    elif MLD_sorteado not in MLD2_sorteado:
        MLD_sorteado = MLD[0]
        break

    if MLD2_sorteado in MLD_sorteado:
        shuffle(MLD2)
        MLD2_sorteado = MLD2[0]

    elif MLD2_sorteado not in MLD_sorteado:
        MLD2_sorteado = MLD2[0]
        break
