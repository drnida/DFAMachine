import sys

encode_file = open('encode.dat', 'r')
for x in range(int(sys.argv[1]) - 1):
	  encode_file.readline()
	  encoding = encode_file.readline()
	  sigma = encoding.split('|')[0]
	  states = encoding.split('|')[1]
	  start = encoding.split('|')[2]
	  delta = encoding.split('|')[3]
	  final = encoding.split('|')[4]
	  string = encoding.split('|')[5]




	  temp = []
	  transitions = []
	  states = states.split(';')
	  state_list = []
	  for state in states:
		    state_list.append(state.split(','))
		    for state in state_list:
			      for transition in state:
				           temp.append(transition.split('->'))
					     transitions.append(temp)
					       temp = []
					       print transitions






STATES = ["state1","state2","state3","state4","state0"]
SIGMA = ["0","1","2","3","4","5","6"]

DFA = dict.fromkeys(STATES, None)
for x in DFA:
    DFA[x] = dict.fromkeys(SIGMA, None)



print DFA
print "the dict-------------------------"



m = "state0:0-state2,1-state1/state1:0-state0,1-state2/state2:0-state1,1-state2/state2:4-state1,5-state2"
print m
print "\n"
Q = m.split("/")
print Q
print "\n"

print "input----------------------------"

    

for x in range(len(Q)):

     state = Q[x].split(":")
     #print state
     deltas = state[1].split(",")
     print deltas

     for y in range(len(deltas)):
         sigma = deltas[y].split("-") 
         
	 #state[0] is the state index, 
	 #sigma[0] is the alphabet index, sigma[1] is the state to transition to. 
	 DFA[state[0]][sigma[0]] = sigma[1] 




print "DFA populated------------------"
print DFA
print "\n"


print "DFA by line------------------"
for x in DFA:
    print x + "|||" + str(DFA[x])


currentState = "state0"
inputString = "011001"

inputString = list(inputString)
print inputString

for x in range(len(inputString)):
    print "Current state is " + currentState
    print "Input is " + inputString[x]

    currentState = DFA[currentState][inputString[x]]

    print "Transitioned to " + currentState

print "Final state is " + currentState






