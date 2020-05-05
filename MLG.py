from random import shuffle

MLG = [
    'P. Scholes',
    'D. Stankovic',
    'G. Kondogbia',
    'R. Barkley',
    'A. Lallana',
    'M. Pasalic',
    'N. Keita',
    'B. Zungu',
    'L. Pellegrini',
    'Fabián Ruiz',
    'Febas',
    'I. Baba',
    'L. Modric',
    'R. Nainggolan',
    'Allan',
    'M. Verratti',
    'M. De Roon',
    'M. Brozovic',
    'Saúl',
    'N. Kanté',
    'L. Cook',
    'A. Ricaurte',
    'Arthur',
    'S. M. Savic',
    'I. Akhmetov',
    'R. Zobnin',
]

shuffle(MLG)
MLG_sorteado = MLG[0]

MLG2 = [
    'P. Scholes',
    'D. Stankovic',
    'G. Kondogbia',
    'R. Barkley',
    'A. Lallana',
    'M. Pasalic',
    'N. Keita',
    'B. Zungu',
    'L. Pellegrini',
    'Fabián Ruiz',
    'Febas',
    'I. Baba',
    'L. Modric',
    'R. Nainggolan',
    'Allan',
    'M. Verratti',
    'M. De Roon',
    'M. Brozovic',
    'Saúl',
    'N. Kanté',
    'L. Cook',
    'A. Ricaurte',
    'Arthur',
    'S. M. Savic',
    'I. Akhmetov',
    'R. Zobnin',
]

shuffle(MLG)
MLG2_sorteado = MLG2[0]

while MLG_sorteado in MLG2_sorteado or MLG2_sorteado in MLG_sorteado:

    if MLG_sorteado in MLG2_sorteado:
        shuffle(MLG)
        MLG_sorteado = MLG[0]

    elif MLG_sorteado not in MLG2_sorteado:
        MLG_sorteado = MLG[0]
        break

    if MLG2_sorteado in MLG_sorteado:
        shuffle(MLG2)
        MLG2_sorteado = MLG2[0]

    elif MLG2_sorteado not in MLG_sorteado:
        MLG2_sorteado = MLG2[0]
        break
