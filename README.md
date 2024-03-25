# Description
The language I chose was a set of words from the Chalkobsa language.
Here´s the set of words:
- mahdi
- maqbara
- matar
- maula
- midri

The *modeling technique* I used is a Deterministic Finite Automata (DFA) to represent my solution since it is a set of words so we know the next state based on the current state because DFAs eliminate ambiguity and for this example the DFA can accept or reject the input string in one pass, so it is more efficient.

# Model of the Solution
This is the automata generated for this language: 
![image](https://github.com/AntonioLanderos/tc2037/assets/150750842/b4ca0602-2461-4623-a81f-c2c16cc714b2)

The presented automata is equivalent to the following regular expression:
^m(a(hdi|qbara|tar|ula)|idri)$
