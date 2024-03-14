def acceptare(stare, cuvant):
    if len(cuvant)==0:
        verif=1 #nu este acceptat
        for i in stare:
            if i in stari_finale:
                verif=0# este acceptat
        if verif==0:
            print("DA")
        else:
            print("NU")
    else:
        lista_stari=[]
        for nr in stare:
            if nr in tranzitii and cuvant[0] in tranzitii[nr]:
                for st in tranzitii[nr][cuvant[0]]:
                    lista_stari.append(st)
        if len(lista_stari)==0:
            print("NU")
        else:
            acceptare(lista_stari, cuvant[1:])


f=open('NFA.in')
nr_stari=int(f.readline())
print("Nr stari: ", nr_stari)

stari=f.readline().split()
for x in range(nr_stari):
    stari[x]=int(stari[x])
print("Starile: ", stari)

nr_litere=int(f.readline())
print("Nr litere: ", nr_litere)

litere=f.readline().split()
print("Literele: ", litere)

stare_initiala=int(f.readline())
print("Stare initiala: ", stare_initiala)

nr_stari_finale=int(f.readline())
print("Nr stari finale: ", nr_stari_finale)

stari_finale=f.readline().split()
for x in range(nr_stari_finale):
    stari_finale[x]=int(stari_finale[x])
print("Stari finale: ", stari_finale)

nr_tranzitii=int(f.readline())
print("Nr tranzitii: ", nr_tranzitii)
tranzitii={}
for _ in range(nr_tranzitii):
    trans=f.readline().split()
    if int(trans[0]) not in tranzitii:
        tranzitii[int(trans[0])]={}
        if trans[1] not in tranzitii[int(trans[0])]:
            tranzitii[int(trans[0])][trans[1]]=[]
            tranzitii[int(trans[0])][trans[1]].append(int(trans[2]))
        else:
            tranzitii[int(trans[0])][trans[1]].append(int(trans[2]))
    else:
        if trans[1] not in tranzitii[int(trans[0])]:
            tranzitii[int(trans[0])][trans[1]] = []
            tranzitii[int(trans[0])][trans[1]].append(int(trans[2]))
        else:
            tranzitii[int(trans[0])][trans[1]].append(int(trans[2]))

print("Tranzitii ", tranzitii)

nr_cuvinte=int(f.readline())
print("Nr cuvinte: ", nr_cuvinte)

lista=[f.readline() for _ in range(nr_cuvinte)]
lista_cuvinte=[]
for cuv in lista:
    clean=cuv.strip()
    lista_cuvinte.append(clean)
print("Lista cuvinte: ", lista_cuvinte)


for cuv in lista_cuvinte:
    acceptare([stare_initiala], cuv)
