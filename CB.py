from random import shuffle

CB = [
    'P. Maldini',
    'W. Samuel',
    'O. Deschacht',
    'D. Lugano',
    'R. Vlaar',
    'E. Garay',
    'R. Rocha',
    'T. Alderweireld',
    'E. Mangala',
    'K. Manolas',
    'J. Boateng',
    'N. Otamendi',
    'K. Zouma',
    'A. Romagnoli',
    'J. Simunovic',
    'N. Pallois',
    'J. Denayer',
    'Andrei Girotto',
    'F.Tomori',
    'T. Kehrer',
    'K. Ajer',
    'A. Martynovich',
    'M. Demiral',
    'L. Bonucci',
    'M. Benatia',
    'David Luiz',
    'S. De Vrij',
    'V. Van Dijk',
    'W. Hoedt',
    'M. Ginter',
    'Bruno',
    'K. Koulibaly',
    'P. Kimpembe',
    'C. Lenglet',
    'E. Bailly',
    'A. Rudiger',
    'N. Elvedi',
    'Ç. Soyuncu',
    'M. Sarr',
    'N. Sule',
    'K. Manolas',
    'R. Varane',

]

shuffle(CB)
CB_sorteado = CB[0]

CB2 = [
    'P. Maldini',
    'W. Samuel',
    'O. Deschacht',
    'D. Lugano',
    'R. Vlaar',
    'E. Garay',
    'R. Rocha',
    'T. Alderweireld',
    'E. Mangala',
    'K. Manolas',
    'J. Boateng',
    'N. Otamendi',
    'K. Zouma',
    'A. Romagnoli',
    'J. Simunovic',
    'N. Pallois',
    'J. Denayer',
    'Andrei Girotto',
    'F.Tomori',
    'T. Kehrer',
    'K. Ajer',
    'A. Martynovich',
    'M. Demiral',
    'L. Bonucci',
    'M. Benatia',
    'David Luiz',
    'S. De Vrij',
    'V. Van Dijk',
    'W. Hoedt',
    'M. Ginter',
    'Bruno',
    'K. Koulibaly',
    'P. Kimpembe',
    'C. Lenglet',
    'E. Bailly',
    'A. Rudiger',
    'N. Elvedi',
    'Ç. Soyuncu',
    'M. Sarr',
    'N. Sule',
    'K. Manolas',
    'R. Varane',
]

shuffle(CB2)
CB2_sorteado = CB2[0]

CB3 = [
    'P. Maldini',
    'W. Samuel',
    'O. Deschacht',
    'D. Lugano',
    'R. Vlaar',
    'E. Garay',
    'R. Rocha',
    'T. Alderweireld',
    'E. Mangala',
    'K. Manolas',
    'J. Boateng',
    'N. Otamendi',
    'K. Zouma',
    'A. Romagnoli',
    'J. Simunovic',
    'N. Pallois',
    'J. Denayer',
    'Andrei Girotto',
    'F.Tomori',
    'T. Kehrer',
    'K. Ajer',
    'A. Martynovich',
    'M. Demiral',
    'L. Bonucci',
    'M. Benatia',
    'David Luiz',
    'S. De Vrij',
    'V. Van Dijk',
    'W. Hoedt',
    'M. Ginter',
    'Bruno',
    'K. Koulibaly',
    'P. Kimpembe',
    'C. Lenglet',
    'E. Bailly',
    'A. Rudiger',
    'N. Elvedi',
    'Ç. Soyuncu',
    'M. Sarr',
    'N. Sule',
    'K. Manolas',
    'R. Varane',
]

shuffle(CB3)
CB3_sorteado = CB3[0]

while CB_sorteado in CB2_sorteado or CB_sorteado in CB3_sorteado or CB3_sorteado in CB2_sorteado or CB3_sorteado in CB_sorteado:

    if CB_sorteado in CB2_sorteado or CB_sorteado in CB3_sorteado:
        shuffle(CB)
        CB_sorteado = CB[0]

    elif CB_sorteado not in CB2_sorteado or CB_sorteado not in CB3_sorteado:
        CB_sorteado = CB[0]
        break

    if CB2_sorteado in CB_sorteado or CB2_sorteado in CB3_sorteado:
        shuffle(CB2)
        CB2_sorteado = CB[0]

    elif CB2_sorteado not in CB_sorteado or CB2_sorteado not in CB3_sorteado:
        CB2_sorteado = CB2[0]
        break

    if CB3_sorteado in CB_sorteado or CB3_sorteado in CB2_sorteado:
        shuffle(CB3)
        CB3_sorteado = CB3[0]

    elif CB3_sorteado not in CB_sorteado or CB3_sorteado not in CB2_sorteado:
        CB3_sorteado = CB3[0]
        break
