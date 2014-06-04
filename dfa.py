import sys

#needs error checking for invalid argv value 



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

#Listifying input
states = states.split(",")
sigma = sigma.split(",")
final = final.split(",")
currentState = start
string = list(string)
print string
try:
    string.remove("\n")
except:
    pass
print string

#Building empty DFA from states and sigma
DFA = dict.fromkeys(states, None)
for x in DFA:
    DFA[x] = dict.fromkeys(sigma, None)



print "\nthe dict-------------------------"
print DFA
print "the dict-------------------------"



#example transition string 
#"state0:0-state2,1-state1/state1:0-state0,1-state2/state2:0-state1,1-state2/state2:4-state1,5-state2"

#Parse transitions string and add transitions to the DFA
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



#Traverse DFA and accept or reject
for x in range(len(string)):
    print "Current state is " + currentState
    print "Input is " + string[x]

    currentState = DFA[currentState][string[x]]

    print "Transitioned to " + currentState

print "Current State is:  " + currentState + ", Final States are: " + str(final)



if currentState in final:
    print "ACCEPT"
else:
    print "REJECT"




