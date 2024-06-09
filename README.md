# Welcome to my Turing Machine Project! 

Al the information about how it works it's contained in the comments, but in this readme I'll tell **how to use.**

## File format.

The file format used is the JavaScript Object Notation, it contains a dictionary with the following data.

{
	"input_symbols":  ["A",  "B"],
	"states":  ["q0",  "q1",  "q_accept",  "q_reject"],
	"transitions":  {
		"q0":  {
			"A":["q1",  "B",  "R"],
			"B":["q_reject",  "B",  "R"],
			"_":["q_reject", "\_", "N"]
	}
	"initial_state":  "q0",
	"accept_states":  ["q_accept"],
	"reject_states":  ["q_reject"]
}

As you can see, on the **input_symbols** we can define the input symbols we can use in the tape.
At the **states**   key we've a list of all the states <em>including accept and reject states.</em>
The hardest part is defining the transition functions, it will contain as a key every state we have, and the value will be the list of each input it can hold, followed by a list with the order of "<em><strong>next state, symbol to write, position to change </strong></em>".
We also have the initial state (<em>We can define it default as <strong>q0</strong> if we want in the code, just change on the \_\_init__ method the <strong>initial_state</strong> propriety. </em>)
Finally, we have the <strong>accept</strong> and <strong>reject</strong> states contained in a list.

## Using the program.

The program doesn't need external libraries, it just need the json module to work. To run the program we just use <strong>python Turing.py</strong> (Or <strong>Python3</strong> in case we're using it) and It'll display the filename question at the console, in case we press enter (sending <strong>empty string</strong>) the program will end. If the file doesn't exist, it'll raise an error and will continue asking for a file. Once it match an  existing file, It'll ask strings to verify in the T.M. untill we send an empty string, that will return us to the filename asking loop.
All the steps in the T.M. run will be shown on console, with the step number, current tape state, current state and the header position and the final result. If we want, we can set an max step number, adding on the <strong>run</strong>  method of the class the code <em>and steps<=(Our max steps number)</em> at the end of the while loop.
