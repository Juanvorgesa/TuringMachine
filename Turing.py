"""
Project: Design a Turing machine (free programming language).
The T.M must receive a JSON file with the format explained, the input
symbols are determinated as "{A,B}"
Student: Juan Pedro Reyes Ornelas.
Matricle: 2001336c
"""

import json # Import the json module for file managing.
"""
JSON Doc Format:
states: [A list with all the T.M states]
transitions: {
    "{state}" : {
        "Input" : ["Next state", "Write", "R/L/N"]
    }
}
initial_state: Initial state.
accept_states: [A list with the accepted states.]
reject_states: [A list with the rejected states (Trap states).]

The tacit values:
Input symbols: {A,B} (Defined before)
Alphabet: it includes the input symbols extended with "_" for blank symbol.
Blank symbol: Blank symbol (_)


"""

class TuringMachine: # We define the T.M as an object.
    def __init__(self, config):
        self.states = config["states"]
        self.blank_symbol = "_"
        self.input_symbols = config["input_symbols"]
        self.alphabet = self.input_symbols.append(self.blank_symbol)
        self.transitions = config["transitions"]
        self.initial_state = config["initial_state"]
        self.accept_states = config["accept_states"]
        self.reject_states = config["reject_states"]
        self.current_state = self.initial_state # We define the current state as initial.
        self.tape = [] # We initialize the tape as an empty one.
        self.head_position = 0 # The head position will be 0 (the start).

    def initialize_tape(self, input_string): # We define the method to initialize the tape with a input string.
        self.tape = list(input_string) # The tape will be the input string as a list.
        self.head_position = 0 # Initialize the head position as 0 (start).

    def step(self): # Define the method "Step" for each step we do.
        # We might verify if the header is at one of the edges of the tape.
        if self.head_position < 0: # If the position is negative, it means we must append a Blank symnol.
            self.tape.insert(0, self.blank_symbol)
            self.head_position = 0 # Once we add the blank symbol, we return the head to "0"
        elif self.head_position >= len(self.tape): # If the position is higher or equals to the tape length, we must append the Blank Symbol.
            self.tape.append(self.blank_symbol) # We append the blank symbol.
        
        # Once we verify our position, we should get the current symbol.
        current_symbol = self.tape[self.head_position]
        # If the symbol has a transition in that state
        if self.current_state in self.transitions and current_symbol in self.transitions[self.current_state].keys():
            print(self.transitions[self.current_state][current_symbol])
            next_state, write_symbol, move_direction = self.transitions[self.current_state][current_symbol]
            self.tape[self.head_position] = write_symbol
            self.current_state = next_state
            # We verify if the move direction is left or right to change the head position, if it is N, it stands as it.
            if move_direction == 'R':
                self.head_position += 1
            elif move_direction == 'L':
                self.head_position -= 1
            elif move_direction == "N":
                pass # We pass if the symbol is _ (Stand)
            else:
                raise ValueError(f"Invalid move direction: {move_direction}") # If the move direction is invalid.
            return True
        # If the symbol has not a transition in that state
        else:
            print(f'The state {self.current_state} doesn\'t contain the symbol: {current_symbol}')
            return False

    # Method to run the T.M with a input string.
    def run(self, input_string):
        self.current_state = self.initial_state
        self.initialize_tape(input_string) # We initialize the tape as the input string.
        steps = 0 # The steps starts at 0.

        # We do the steps while the transitions are right.
        while self.current_state not in self.accept_states and self.current_state not in self.reject_states:
            print(f"Step {steps}:")
            print(f"State: {self.current_state}")
            print(f"Tape: {''.join(self.tape)}")
            print(f"Head Position: {self.head_position}")
            if not self.step(): # If therwe are no more steps, we break the loop.
                break
            steps += 1

        # We print the final information.
        print(f"Final State: {self.current_state}")
        print(f"Final Tape: {''.join(self.tape)}")
        print(f"Steps: {steps}")
        if self.current_state in self.accept_states:
            print("Result: Accepted")
        elif self.current_state in self.reject_states:
            print("Result: Rejected")
        else:
            print("Result: Stopped (No more transitions)")
while True:
    file_name = input("Enter the JSON file name: ") # We ask the file name
    if not file_name: break # If there is no file name, we break the loop.
    try: # We try to open the file, if it doesn't exist, we raise an exception.
        with open(file_name, 'r') as f:
            config = json.load(f) # We load the json data.
        tm = TuringMachine(config) # We initialize the TM to work.
        while True: # We start the loop for asking strings.
            input_string = input("Enter the input string: ")
            if not input_string: break # If there is no input string, we break de loop.
            tm.run(input_string) # We run our TM.
    except Exception as ex:
        print(f"There is an exception: {ex}") # We print the exception.