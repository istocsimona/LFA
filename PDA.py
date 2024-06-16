def acceptare(stare, cuvant):
    if len(stack)>0:#daca mai exista ceva pe stiva continuam altfel nu mai avem la ce da pop
        prov=stack.pop()
        for trans in tranzitii: #luam fiecare tranzitie
            if (trans[0] == stare  and trans[2] == prov): #cautam tranzitiile care incep din starea nostra si care iau din stiva ce avem noi in prov(varful stivei)
                if trans[1] == cuvant[0]:#daca prima litera din cuvant este in tranzitie
                    if trans[3] != ".":#daca ce avem in stiva e diferit de lambda adaugam(reversed pentru ca daca e mai mare il punem invers)
                        for elem in reversed(trans[3]):
                            stack.append(elem)
                    if len(cuvant)==1:
                        acceptare(trans[4], '.')
                    else:
                        acceptare(trans[4], cuvant[1:])
                    break
                elif trans[1] == ".": #daca gasim o tranzitie care are starea corecta si ce e in stiva corecta dar litera nu corespunde, continuam cu acea tranzitie dar cuvantul nu se schimba
                    if trans[3] != ".":
                        for elem in reversed(trans[3]):
                            stack.append(elem)

                    acceptare(trans[4], cuvant)
                    break

        else:
            stack.append(prov)
            verif=0
            if cuvant[0]==".":
                for st in stari_finale:
                    if st == stare:
                        if stack[0]=="$":
                            verif=1
            if(verif==0):
                print("NU")
            else:
                print("DA")
    else:
        print("NU")


nr_stari=3
print("Nr stari: ", nr_stari)

stari=[1, 2, 3]

print("Starile: ", stari)

nr_litere=2
print("Nr litere: ", nr_litere)

litere=["a", "b"]
print("Literele: ", litere)

stare_initiala=1
print("Stare initiala: ", stare_initiala)

nr_stari_finale=1
print("Nr stari finale: ", nr_stari_finale)

stari_finale=[3]
print("Stari finale: ", stari_finale)

nr_tranzitii=5
print("Nr tranzitii: ", nr_tranzitii)
#[din ce stare ma pornesc, ce litera prelucrez, ce iau de pe stiva, ce pun pe stiva, in ce stare merg]
tranzitii=[[1, "a", "A", "AA", 1],
           [1, "a", "$", "AA$", 1],
           [1, ".", "A", "A", 2],
           [2, "b", "A", ".", 2],
           [2, ".", "$", "$", 3]]


print("Tranzitii ", tranzitii)


f=open("tema3.txt")

nr_cuvinte=int(f.readline())
print("Nr cuvinte: ", nr_cuvinte)

lista=[f.readline() for _ in range(nr_cuvinte)]
lista_cuvinte=[]
for cuv in lista:
    clean=cuv.strip()
    lista_cuvinte.append(clean)
print("Lista cuvinte: ", lista_cuvinte)


for cuv in lista_cuvinte:
    print(cuv, end=" ")
    stack=["$"]
    acceptare(stare_initiala, cuv)

