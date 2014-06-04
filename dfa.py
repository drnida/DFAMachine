import sys

encode_file = open('encode.dat', 'r')
for x in range(4):
    encode_file.readline()

for x in range((int(sys.argv[1]) - 1) * 2 + 1):
	  encode_file.readline()
encoding = encode_file.readline()
encoding = encoding[3:]
print "Encoding:  " + encoding
sigma = encoding.split('|')[0]
states = encoding.split('|')[1]
start = encoding.split('|')[2]
delta = encoding.split('|')[3]
final = encoding.split('|')[4]
string = encoding.split('|')[5]


print "--------------lines----------"
print sigma
print states
print start
print delta
print final
print string
print"----------------------------"


states = states.split(",")
sigma = sigma.split(",")
final = final.split(",")



DFA = dict.fromkeys(states, None)
for x in DFA:
    DFA[x] = dict.fromkeys(sigma, None)



print "\nthe dict-------------------------"
print DFA
print "the dict-------------------------"



#m = "state0:0-state2,1-state1/state1:0-state0,1-state2/state2:0-state1,1-state2/state2:4-state1,5-state2"
#print m
#print "\n"
Q = delta.split("/")
print "Q is ----- " + str(Q)
print "\n"

print "input----------------------------"

    

for x in range(len(Q)):

     state = Q[x].split(":")
     print "states is " + str(state)
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

string = list(string)
print string

for x in range(len(string)):
    print "Current state is " + currentState
    print "Input is " + string[x]

    currentState = DFA[currentState][string[x]]

    print "Transitioned to " + currentState

print "Final state is " + currentState

if currentState in final:
    print "ACCEPT"
else:
    print "REJECT"




