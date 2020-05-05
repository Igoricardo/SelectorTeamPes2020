from random import shuffle

CA = [
    'Romário',
    'Llorente',
    'E. Cavani',
    'J. Hernández',
    'S. Jovetic',
    'D. Mertens',
    'E. Choupo-Moting',
    'J. Guidetti',
    'L. Muriel',
    'M. Icardi',
    'D. Zapata',
    'Adriano',
    'G. Burgstaller',
    'D. Okereke',
    'T. Abraham',
    'P. Pellegri',
    'U. Bozok',
    'J. Hernández',
    'D. Massaro',
    'A. Kutucu',
    'J. Arp',
    'G. Higuaín',
    'M. Arnautovic',
    'L. Suárez',
    'P. Aubameyang',
    'A. Griezmann',
    'Iago Aspas',
    'M. Depay',
    'A. Milik',
    'J. King',
    'André Silva',
    'A. Diakhaby',
    'T. Werner',
    'T. Pukki',
    'J. Vardy',
    'A. Lacazette',
    'Mata'
]

shuffle(CA)
CA_sorteado = CA[0]

CA2 = [
    'Romário',
    'Llorente',
    'E. Cavani',
    'J. Hernández',
    'S. Jovetic',
    'D. Mertens',
    'E. Choupo-Moting',
    'J. Guidetti',
    'L. Muriel',
    'M. Icardi',
    'D. Zapata',
    'Adriano',
    'G. Burgstaller',
    'D. Okereke',
    'T. Abraham',
    'P. Pellegri',
    'U. Bozok',
    'J. Hernández',
    'D. Massaro',
    'A. Kutucu',
    'J. Arp',
    'G. Higuaín',
    'M. Arnautovic',
    'L. Suárez',
    'P. Aubameyang',
    'A. Griezmann',
    'Iago Aspas',
    'M. Depay',
    'A. Milik',
    'J. King',
    'André Silva',
    'A. Diakhaby',
    'T. Werner',
    'T. Pukki',
    'J. Vardy',
    'A. Lacazette',
    'Mata'
]

shuffle(CA2)
CA2_sorteado = CA2[0]

CA3 = [
    'Romário',
    'Llorente',
    'E. Cavani',
    'J. Hernández',
    'S. Jovetic',
    'D. Mertens',
    'E. Choupo-Moting',
    'J. Guidetti',
    'L. Muriel',
    'M. Icardi',
    'D. Zapata',
    'Adriano',
    'G. Burgstaller',
    'D. Okereke',
    'T. Abraham',
    'P. Pellegri',
    'U. Bozok',
    'J. Hernández',
    'D. Massaro',
    'A. Kutucu',
    'J. Arp',
    'G. Higuaín',
    'M. Arnautovic',
    'L. Suárez',
    'P. Aubameyang',
    'A. Griezmann',
    'Iago Aspas',
    'M. Depay',
    'A. Milik',
    'J. King',
    'André Silva',
    'A. Diakhaby',
    'T. Werner',
    'T. Pukki',
    'J. Vardy',
    'A. Lacazette',
    'Mata'
]

shuffle(CA3)
CA3_sorteado = CA3[0]

while CA_sorteado in CA2_sorteado or CA2_sorteado in CA_sorteado or CA_sorteado in CA3_sorteado or CA2_sorteado in CA3_sorteado:

    if CA_sorteado in CA2_sorteado:
        shuffle(CA)
        CA_sorteado = CA[0]

    elif CA_sorteado not in CA2_sorteado:
        CA_sorteado = CA[0]
        break

    if CA2_sorteado in CA_sorteado:
        shuffle(CA2)
        CA2_sorteado = CA2[0]

    elif CA2_sorteado not in CA_sorteado:
        CA2_sorteado = CA2[0]
        break

    if CA3_sorteado in CA_sorteado:
        shuffle(CA2)
        CA3_sorteado = CA3[0]

    elif CA3_sorteado not in CA_sorteado:
        CA3_sorteado = CA3[0]
        break