from random import shuffle

GO = [
    'O. Kahn',
    'D. Ospina',
    'F. Foster',
    'O. Karnezis',
    'Diego Alves',
    'David de Gea',
    'Ádrian',
    'Marcelo Lomba',
    'M. Ter Stegen',
    'E. Martínez',
    'Rui Patrício',
    'S. Ruffier',
    'D. Subasic',
    'Neto',
    'A. Cragno',
    'G. Donnarumma',
    'A. Meret',
      ]

shuffle(GO)
GO_sorteado = GO[0]

GO2 = [
    'O. Kahn',
    'D. Ospina',
    'F. Foster',
    'O. Karnezis',
    'Diego Alves',
    'David de Gea',
    'Ádrian',
    'Marcelo Lomba',
    'M. Ter Stegen',
    'E. Martínez',
    'Rui Patrício',
    'S. Ruffier',
    'D. Subasic',
    'Neto',
    'A. Cragno',
    'G. Donnarumma',
    'A. Meret',
      ]

shuffle(GO2)
GO2_sorteado = GO2[0]

while GO_sorteado in GO2_sorteado or GO2_sorteado in GO_sorteado:

    if GO_sorteado in GO2_sorteado:
        shuffle(GO)
        GO_sorteado = GO[0]

    elif GO_sorteado not in GO2_sorteado:
        GO_sorteado = GO[0]
        break

    if GO2_sorteado in GO_sorteado:
        shuffle(GO2)
        GO2_sorteado = GO2[0]

    elif GO2_sorteado not in GO_sorteado:
        GO2_sorteado = GO2[0]
        break
        