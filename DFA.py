def acceptare(stare, cuvant):
    if len(cuvant)==0:
        if stare in stari_finale:
            print("DA")
        else:
            print("NU")
    else:
        if stare in tranzitii:
            if cuvant[0] in tranzitii[stare]:
                acceptare(tranzitii[stare][cuvant[0]], cuvant[1:])
            else:
                print("NU")
        else:
            print("NU")

f=open('DFA_in')
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
        tranzitii[int(trans[0])]={trans[1]:int(trans[2])}
    else:
        tranzitii[int(trans[0])].update({ trans[1]:int(trans[2]) })

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
    acceptare(stare_initiala, cuv)
