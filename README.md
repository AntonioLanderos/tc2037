# Description
The language I chose was a set of words from the Chalkobsa language.
Here´s the set of words:
- mahdi
- maqbara
- matar
- maula
- midri

The *modeling technique* I used is a Deterministic Finite Automata (DFA) to represent my solution.
DFA is a suitable choice for this task due to its ability to eliminate ambiguity and efficiently process input strings in a single pass. In DFA, the next state is determined solely by the current state and the input symbol, making it ideal for tokenization tasks.

# Model of the Solution
This is the automata generated for this language: 
![image](https://github.com/AntonioLanderos/tc2037/assets/150750842/b4ca0602-2461-4623-a81f-c2c16cc714b2)

The presented automata is equivalent to the following regular expression:
^m(a(hdi|qbara|tar|ula)|idri)$

# Implementation
For the implementation of lexical analysis, I used the regular expression I described above. The lexical analyzer, implemented in the file regexv2.py, tokenizes input strings according to the rules defined by the DFA.

Example inputs and outputs include:

# Analysis
The implementation utilizes Python's regular expression library (re) to parse input strings according to the defined rules of the Chalkobsa language. Here's an analysis of the implementation:

parse(input_string): This function attempts to match the input string with the regular expression representing the Chalkobsa language. If a match is found, the input string is returned; otherwise, None is returned.  O(n)

accept(parsed_string): This function checks if the parsed string is not None. If the parsed string is not None, it returns 'Yes', indicating that the string is accepted; otherwise, it returns 'No'.   O(1)

inputs: This list contains predefined input strings for testing the lexical analyzer.

Testing: The lexical analyzer is tested with both predefined input strings and additional verification. For each input string, the parse() function is called to parse the input, and the accept() function is then called to determine if the string is accepted. The results are printed to the console.  O(n*m)
