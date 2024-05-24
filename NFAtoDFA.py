def fromListToNumber(list):
    number = 0
    for i in list:
        number = number * (10**len(str(i))) + i
    return number

def fromNumberToList(number):
    list=[]
    while number!=0:
        list.append(number%10)
        number = number//10
    return list
def creatingNewState(listOfStates, letter):
    newState=[]
    for state in listOfStates:
        if state in transitions and  letter in transitions[state]:
            for tempState in transitions[state][letter]:
                if tempState not in newState:
                    newState.append(tempState)
            dfaTransitions[dfaState1][letter]=fromListToNumber(newState)
    return newState
def printAll():
    print(len(dfaStates))
    for state in dfaStates:
        print(fromListToNumber(state), end=' ')

    print()
    print(numberOfLetters)
    for letter in alphabet:
        print(letter, end=' ')

    print()
    print(startState)

    print(len(dfaFinalStates))
    for state in dfaFinalStates:
        print(fromListToNumber(state), end=' ')
    print()
    print(dfaNumberOfTransitions)
    for state1 in dfaTransitions:
        for letter in alphabet:
            if letter in dfaTransitions[state1]:
                print(state1, letter, dfaTransitions[state1][letter])
def ifFinalState(state):
    for st in state:
        if st in finalStates:
            return True
    return False


f = open('NFAtoDFA.in')
NFA_out = open('NFA.out', 'w')
numberOfStates = int(f.readline())
print("Number of states: ", numberOfStates)

listOfStates = f.readline().split()
states={}
i=1
for x in listOfStates:
    states[int(x)]=i
    i+=1
print("States: ", states)

numberOfLetters = int(f.readline())
print("Number of letters: ", numberOfLetters)

alphabet = f.readline().split()
print("Alphabet: ", alphabet)

startState = states[int(f.readline())]
print("Start state: ", startState)

numberOfFinalStates = int(f.readline())
print("Number of final states: ", numberOfFinalStates)

listOfFinalStates = f.readline().split()
finalStates=[]
for x in listOfFinalStates:
    finalStates.append(states[int(x)])
print("Final states: ", finalStates)

numberOfTransitions = int(f.readline())
print("Number of transitions: ", numberOfTransitions)
transitions = {}
for _ in range(numberOfTransitions):
    trans = f.readline().split()
    if states[int(trans[0])] not in transitions:
        transitions[states[int(trans[0])]] = {}
        if trans[1] not in transitions[states[int(trans[0])]]:
            transitions[states[int(trans[0])]][trans[1]] = []
            transitions[states[int(trans[0])]][trans[1]].append(states[int(trans[2])])
        else:
            transitions[states[int(trans[0])]][trans[1]].append(states[int(trans[2])])
    else:
        if trans[1] not in transitions[states[int(trans[0])]]:
            transitions[states[int(trans[0])]][trans[1]] = []
            transitions[states[int(trans[0])]][trans[1]].append(states[int(trans[2])])
        else:
            transitions[states[int(trans[0])]][trans[1]].append(states[int(trans[2])])


print("Transitions: ", transitions)

print("\nDFA:")


dfaNumberOfTransitions=0

dfaStates=[[startState]]

dfaFinalStates=[]

dfaTransitions={}

for listOfStates in dfaStates:
    dfaState1=fromListToNumber(listOfStates)
    dfaTransitions[dfaState1]={}
    for letter in alphabet:
        newState=creatingNewState(listOfStates, letter)
        if len(newState)>0 and newState not in dfaStates:
            dfaStates.append(newState)
        if ifFinalState(newState) is True and newState not in dfaFinalStates:
            dfaFinalStates.append(newState)

    dfaNumberOfTransitions+=len(dfaTransitions[dfaState1])

printAll()
