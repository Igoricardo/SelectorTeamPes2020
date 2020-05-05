from random import shuffle
import GO, CB, LE, LD, VOL, MLG, MLE, MLD, MAT, PTD, PTE, SA, CA

c1 = 'L. Roman'
c2 = 'S. Doron'
c3 = 'P. Boer'
c4 = 'B. Vivanco'
c5 = 'A. Gouvea'

go = GO.GO_sorteado
go2 = GO.GO2_sorteado
cb = CB.CB_sorteado
cb2 = CB.CB2_sorteado
cb3 = CB.CB3_sorteado
le = LE.LE_sorteado
le2 = LE.LE2_sorteado
ld = LD.LD_sorteado
ld2 = LD.LD2_sorteado
vol = VOL.VOL_sorteado
vol2 = VOL.VOL2_sorteado
mlg = MLG.MLG_sorteado
mlg2 = MLG.MLG2_sorteado
mle = MLE.MLE_sorteado
mle2 = MLE.MLE2_sorteado
mld = MLD.MLD_sorteado
mld2 = MLD.MLD2_sorteado
mat = MAT.MAT_sorteado
mat2 = MAT.MAT2_sorteado
ptd = PTD.PTD_sorteado
ptd2 = PTD.PTD2_sorteado
pte = PTE.PTE_sorteado
sa = SA.SA_sorteado
ca = CA.CA_sorteado
ca2 = CA.CA2_sorteado
ca3 = CA.CA3_sorteado

coach = [c1, c2, c3, c4, c5]
shuffle(coach)
coach_sorteado = coach[0]

if coach_sorteado == c1:
    print(f'''
        Técnico: {c1}
        Formação: 4-1-2-3''')

    print(f'''
    Jogadores Sorteados para compor o elenco
    
    Time Principal:
    
    {go}
    {cb}
    {cb2}
    {le}
    {ld}
    {vol}
    {mat}
    {mat2}
    {pte}
    {ptd}
    {ca}
    
    Banco de reservas:

    {go2}
    {cb3}
    {le2}
    {vol2}
    {mlg}
    {ptd2}
    {ca2}
    
    ''')

elif coach_sorteado == c2:
    print(f'''
    Técnico: {c2}
    Formação: 4-2-3-1''')

    print(f'''
    Jogadores Sorteados para compor o elenco

    Time Principal:
    
    {go}
    {cb}
    {cb2}
    {le}
    {ld}
    {vol}
    {mlg}
    {mle}
    {mld}
    {mat}
    {ca}
    
    Banco de reservas:

    {go2}
    {cb3}
    {ld2}
    {mlg2}
    {mle2}
    {mld2}
    {ca2}

    ''')

elif coach_sorteado == c3:
    print(f'''
    Técnico: {c3}
    Formação: 4-2-1-3''')

    print(f'''
    Jogadores Sorteados para compor o elenco

    Time Principal:
    
    {go}
    {cb}
    {cb2}
    {le}
    {ld}
    {vol}
    {mlg}
    {mat}
    {pte}
    {ptd}
    {ca}
    
    Banco de reservas:

    {go2}
    {cb3}
    {le2}
    {vol2}
    {mlg2}
    {sa}
    {ca2}

    ''')

elif coach_sorteado == c4:
    print(f'''
    Técnico: {c4}
    Formação: 4-2-2-2''')

    print(f'''
    Jogadores Sorteados para compor o elenco
    
    Time Principal:

    {go}
    {cb}
    {cb2}
    {le}
    {ld}
    {mlg}
    {mlg2}
    {mle}
    {mld}
    {ca2}
    {ca}

    Banco de reservas:

    {go2}
    {cb3}
    {ld2}
    {vol2}
    {mle2}
    {sa}
    {ca3}

    ''')

elif coach_sorteado == c5:
    print(f'''
    Técnico: {c5}
    Formação: 4-1-3-2''')

    print(f'''
    Jogadores Sorteados para compor o elenco

    Time Principal:

    {go}
    {cb}
    {cb2}
    {le}
    {ld}
    {vol}
    {mle}
    {mld}
    {mat}
    {ca2}
    {ca}

    Banco de reservas:

    {go2}
    {cb3}
    {le2}
    {vol2}
    {mld2}
    {sa}
    {ca3}
    
    ''')
