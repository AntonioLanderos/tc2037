# Description
The language I chose was a set of words from the Chakobsa language.
Chakobsa, the secret language of the Fremen in Frank Herbert's "Dune" series, is likely inspired by the real-life Chakobsa used by medieval Circassian knights and princes. Derived from Bzhedukh words meaning 'the language of hunters,' it aligns with Herbert's portrayal of Chakobsa as a hunting language. The Fremen language in "Dune" appears to be a composite of various real-world languages, including French, Romani, Arabic, Slavic, Greek, Sanskrit, and Hebrew. In the 2021 film adaptation of "Dune," linguist David J. Peterson created an expanded version of Chakobsa, known as Neo-Chakobsa, based on existing samples and newly devised grammar. Peterson's work contributes to the linguistic richness of the "Dune" universe. (Wiki, s. f.)

Here's the set of words:
- mahdi
- maqbara
- matar
- maula
- midri

The *modeling technique* I used is a Deterministic Finite Automata (DFA) to represent my solution.
DFA is a suitable choice for this task due to its ability to eliminate ambiguity and efficiently process input strings in a single pass. In DFA, the next state is determined solely by the current state and the input symbol, making it ideal for tokenization tasks.

# Model of the Solution
### Automaton
I designed a Deterministic Finite Automaton (DFA) to recognize the chosen language. The DFA is an effective model for this task due to its ability to process input strings efficiently in a single pass without ambiguity.

#### DFA Explanation
A DFA is a theoretical model of computation that defines a machine with a finite number of states. It processes strings of symbols, transitioning from one state to another according to a set of rules defined by the input symbols. The DFA accepts a string if it ends in an accepting state after reading the entire string. 

In the DFA:
- There are multiple transitions from the start state to intermediate states, depending on the input symbol.
- Each word from the language has a unique path through the states that leads to an accepting state.
This is the automata generated for this language:

![image](https://github.com/AntonioLanderos/tc2037/assets/150750842/b4ca0602-2461-4623-a81f-c2c16cc714b2)

The presented automata is equivalent to the following regular expression:
^m(a(hdi|qbara|tar|ula)|idri)$

The regular expression breaks down as follows:
- `^m` asserts the position at the start of the string and matches the character 'm'.
- The subsequent part matches one of the specified words in the language:
  - `a(hdi|qbara|tar|ula)` matches 'ahdi', 'aqbara', 'atar', or 'aula'.
  - `idri` matches 'idri'.
- `$` asserts the position at the end of the string.

# Implementation
For the implementation of lexical analysis, I used the regular expression I described above. The lexical analyzer, implemented in the file regexv2.py, tokenizes input strings according to the rules defined by the DFA.

Example inputs and outputs include:
- Inputs: the inputs are stored in an array of strings
- Outputs:
  'The string *mahdi* is accepted? Yes'
  'The string *maaula* is accepted? No'
  etc.

  'Test *1* passed'
  'Test *2* passed'
  etc.
  (The text marked in *italics* represents an iterator that goes through the array of inputs and a counter that checks if they pass the tests)

  ## Test cases
  The Python script tests a set of input strings against the regular expression pattern. <br>
  To run the tests, execute the Python script. The script will parse each input string and print whether it is accepted by the regex pattern. It will also count the number of tests that passed.

# Analysis
The implementation utilizes Python's regular expression library (re) to parse input strings according to the defined rules of the Chakobsa language. Here's an analysis of the implementation:

parse(input_string): This function attempts to match the input string with the regular expression representing the Chalkobsa language. If a match is found, the input string is returned; otherwise, None is returned.  O(n)

accept(parsed_string): This function checks if the parsed string is not None. If the parsed string is not None, it returns 'Yes', indicating that the string is accepted; otherwise, it returns 'No'.   O(1)

inputs: This list contains predefined input strings for testing the lexical analyzer.

Testing: The lexical analyzer is tested with both predefined input strings and additional verification. For each input string, the parse() function is called to parse the input, and the accept() function is then called to determine if the string is accepted. The results are printed to the console.  O(n*m)

The time complexity of my model is primarily determined by the time complexity of the regular expression matching operation, which is O(n)

### Comparison with DFA Approach
Using a DFA for lexical analysis also offers a time complexity of O(n). However, the DFA is advantageous in scenarios where constant time processing per character is critical, such as in embedded systems or real-time applications. The regular expression approach is more flexible and easier to implement for complex patterns. (Time Complexity Trade Offs Of Nfa Vs Dfa, s. f.)

### Other Possible Solutions
Non-Deterministic Finite Automaton (NFA):
An NFA can be used to recognize the language, but it may require multiple passes over the input string and backtracking, making it less efficient than a DFA.
NFAs are more expressive than DFAs, but they can be converted to equivalent DFAs for efficient processing.

Context-Free Grammar (CFG):
A CFG can generate the language, but parsing with CFGs typically requires more computational resources and is more complex than using a DFA or regular expression.
CFGs are useful for more complex languages that cannot be described by regular expressions or DFAs. So, for this simple language it would be unefficient to implement it.

# References
Wiki, C. T. D. (s. f.). Chakobsa. Dune Wiki. https://dune.fandom.com/wiki/Chakobsa 
time complexity trade offs of nfa vs dfa. (s. f.). Stack Overflow. https://stackoverflow.com/questions/4580654/time-complexity-trade-offs-of-nfa-vs-dfa#:~:text=The%20construction%20time%20for%20a,DFA%20for%20a%20given%20string. 
re — Regular expression operations. (s. f.). Python Documentation. https://docs.python.org/3/library/re.html
