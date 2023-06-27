
with open('automata.in', 'r') as f:
    lines = f.readlines()

# Initialize empty lists and dict to store the lines after "Sigma :", "States : " and "Transitions :"
sigma = []
transitions = []
states = {}

# variable to keep track of the current section
current_section = None


for line in lines:

    # remove whitespace from the beginning and end of the line
    line = line.strip()

    if line.startswith("#") or line.startswith("End"):
        continue

    # Check if the line starts with "Sigma :"
    if line.startswith("Sigma:"):
        current_section = "sigma"

    # Check if the line starts with "States :"
    elif line.startswith("States:"):
        current_section = "states"

    # Check if the line starts with "Transitions :"
    elif line.startswith("Transitions:"):
        current_section = "transitions"

    # If the current section is "sigma", append the next line to the sigma list
    elif current_section == "sigma" :
        sigma.append(line)

    # If the current section is "states" add the key-value pair to the states dictionary
    elif current_section == "states" and not line.startswith("Transitions:"):
        if "," in line:
            key, value = line.split(", ")
        else:
            key = line.strip()
            value = ""
        states[key] = value

    # If the current section is "transitions" append the next lines to the transitions list
    elif current_section == "transitions" :
        source, letter, destination = line.split(", ")
        transitions.append((source.strip(), letter.strip(), destination.strip()))


final_states = []
initial_states = []

# creating lists with the final and initial states
for key, value in states.items():
    if value == "F":
        final_states.append(key)
    elif value == "S":
        initial_states.append(key)


"""
print(states)
print(sigma)
print(final_states)
print(initial_states)
print(transitions)
"""


Flag_initial_state = True
def initial_state_validation(transitions):
    global Flag_initial_state
    Flag_initial_state = True
    # checking if the initial state is valid
    if len(initial_states) >1:
        Flag_initial_state = False

    if initial_states is not None:
        if transitions[0][0] not in initial_states:
            Flag_initial_state = False
    else:
        if transitions[0][0] not in states:
            Flag_initial_state = False

    if Flag_initial_state== True:
        return("inital state is valid", True)
    else:
        return("initial state is not valid", False)

#print(initial_state_validation(transitions))
state_flag = True
def state_validation(transitions):
    global state_flag
    state_flag = True
    # checking if the other states are valid
    for tup in transitions[1:-1]:
        if tup[0] not in states:
            state_flag=False
            
    for tup in transitions[1:-1]:
        if tup[2] not in states:
            state_flag = False

    if state_flag == True:
        return("states are valid", True)
    else:
        return("some states are not valid", False)


#print(state_validation(transitions))
letter_flag = True
def letter_validation(transitions):
    global letter_flag
    letter_flag = True
 # checking if the letter is valid
    for tup in transitions:
        if tup[1] not in sigma:
            letter_flag = False

    if letter_flag ==  True:
        return("letters are valid", True)
    else:
        return("some letters are not valid", False)


#print(letter_validation(transitions))

Flag_final_state = True
def final_state_validation(transitions):
    global Flag_final_state
    Flag_final_state = True
    # checking if the final state is valid
    if final_states is not None:
        if transitions[-1][2] not in final_states:
            Flag_final_state = False
    else:
        if transitions[-1][2] not in states:
            Flag_final_state = False

    if Flag_final_state==True:
        return("final state is valid", True)
    else:
        return("final state is not valid", False)


#print(final_state_validation(transitions))
def validation_automata():
    result = []
    result.append(initial_state_validation(transitions))
    result.append(state_validation(transitions))
    result.append(letter_validation(transitions))
    result.append(final_state_validation(transitions))
    is_valid = all([x[1] for x in result])
    if is_valid:
        return "automata is valid"
    else:
        for res in result:
            if res[1] == False:
                print(res[0])
        return "automata is not valid"


print(validation_automata())
