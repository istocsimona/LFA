#merge daca starile sunt numere de la 1 la cate sunt si literele de la a la cate sunt
def acceptare(stare, cuvant):
    if len(cuvant)==0:
        if stare in stari_finale:
            print("DA")
        else:
            print("NU")
    else:
        urmatoarea_stare=tranzitii[stare-1][ord(cuvant[0])-ord('a')]
        if urmatoarea_stare!=0:
            acceptare(urmatoarea_stare, cuvant[1:])
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
tranzitii=[[0]*(nr_litere) for _ in range(nr_stari) ]

for i in range(nr_tranzitii):
    trans=f.readline().split()
    tranzitii[int(trans[0])-1][ord(trans[1])-ord('a')+1-1]=int(trans[2])

print(tranzitii)

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