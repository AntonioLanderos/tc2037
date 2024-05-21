# Description
### Context of the Problem
The problem "1114. Print in Order" from LeetCode requires ensuring that three methods (first, second, third) are executed in the correct order, despite being called from different threads. This problem is an excellent example of a common concurrency issue where the order of execution needs to be controlled to maintain correct behavior. Solving this problem ensures that multithreaded applications behave deterministically and avoids issues that can arise from race conditions.

### Why It Is Useful
Concurrency is a fundamental concept in modern programming, allowing multiple operations to be performed simultaneously. It is widely used in applications that require parallel processing, such as web servers, data processing, and real-time systems. Understanding how to control the order of execution in a concurrent environment is crucial for building reliable and efficient systems.

# Model of the solution
Let's model the problem using a diagram that represents the state transitions controlled by the mutexes.
## Initial State:
firstDone is locked.
secondDone is locked.

### After first Executes:
firstDone is unlocked.

### After second Executes:
firstDone is locked.
secondDone is unlocked.

### After third Executes:
secondDone is locked.

# Implementation
For the implementation of a tester for my grammar I used Python and the Natural Language Toolkit (NLTK) library, which is a powerful tool for working with human language data. A CFG is defined in the NLTK format, and the `nltk.ChartParser` is used to parse sentences according to this grammar.
### Python Code
The Python code provided defines the CFG and utilizes NLTK's parser. The code tokenizes an input string and attempts to parse it according to the CFG, printing the parse tree if successful.
The grammar tester, implemented in the file grammar_test.py, which uses a CFG as an input an parses through it to generate its parse tree.
To use the Python file, we have to make sure that NLTK is installed and the CFG is correctly defined in the script. Run the script with a test sentence to see if it gets correctly parsed according to the CFG.
The program outputs a parse tree that represents the structure of the input according to the CFG. If the input does not conform to the CFG, the parser will not output a tree.
* explain mutex, and what the code does *

### Example Inputs and Outputs
- Input: `if 3 < 5 then my_variable = "Ruby" end`
- Output: A parse tree representing the structure of the if-statement.

# Tests
The testFoo function creates an instance of the Foo class and three threads, each executing one of the methods (first, second, third). The threads are joined to ensure the main thread waits for their completion. We can also test our code by submitting the problem's solution into it's corresponding LeetCode problem in the following [link](https://leetcode.com/problems/print-in-order/).

### Test Example
- Input: `while 3 <= 9 do id = "Hello" end`
- Expected Outcome: A parse tree showing the structure of the while loop.
- Actual Outcome: A parse tree (if the CFG and parser are functioning correctly).

# Analysis
### Other Possible Paradigms
Semaphore:
Could be used to signal the order of execution.
Tradeoff: Semaphores can be less intuitive and harder to manage compared to mutexes.
Difference between Mutex and Semaphore
Mutex uses a locking mechanism i.e. if a process wants to use a resource then it locks the resource, uses it and then release it. But on the other hand, semaphore uses a signaling mechanism where wait() and signal() methods are used to show if a process is releasing a resource or taking a resource.
A mutex is an object but semaphore is an integer variable.
A mutex object allows multiple process threads to access a single shared resource but only one at a time. On the other hand, semaphore allows multiple process threads to access the finite instance of the resource until available.
In mutex, the lock can be acquired and released by the same process at a time. But the value of the semaphore variable can be modified by any process that needs some resource but only one process can change the value at a time.

Event-driven programming:
Using condition variables or events to signal method completions.
Tradeoff: This approach can be more complex to implement correctly but offers more fine-grained control.

The time complexity of each method (first, second, third) is O(1) as they each perform a constant amount of work: printing a message and locking/unlocking a mutex. The overall complexity remains O(1) since the operations are independent of any input size.
