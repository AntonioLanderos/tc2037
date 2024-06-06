# Description
### Context of the Problem
The problem "1114. Print in Order" from LeetCode requires ensuring that three methods (first, second, third) are executed in the correct order, despite being called from different threads. This problem is an example of a common concurrency issue where the order of execution needs to be controlled to maintain correct behavior. Solving this problem ensures that multithreaded applications behave deterministically and avoids issues that can arise from race conditions.

### Why is it Useful
Concurrency is a fundamental concept in modern programming, allowing multiple operations to be performed simultaneously. It is widely used in applications that require parallel processing, such as web servers, data processing, and real-time systems. Understanding how to control the order of execution in a concurrent environment is crucial for building reliable and efficient systems.

# Model of the solution
Let's model the problem using a diagram that represents the state transitions controlled by mutex.
![image](https://github.com/AntonioLanderos/tc2037/assets/150750842/77b1427a-1760-4155-a314-2c380a39867c)

# Implementation
[Link to the submission](https://leetcode.com/problems/print-in-order/submissions/1266078691/) <br>
For the implementation of the solution for this problem I used C++ with the help of its libraries: thread, mutex, and functional because leetcode's base template was already using it. 
Mutex and thread are are part of the standard C++ library and they are a powerful tool for working with multithreading. Mutex's method lock() is used to block the calling thread until the thread obtains ownership of the mutex and unlock() is used to release the ownership of the mutex.

I used this simple analogy for a better understanding of the problem: 
- lock(): When you want to use the bathroom, you take the key (lock the door). If someone else is already using the bathroom (the door is locked), you wait until they are done and the door is unlocked.
- unlock(): After you finish using the bathroom, you return the key (unlock the door), so the next person can use it.

### C++ Code
The C++ code provided defines 3 functions which print "first", "second", and "third". We use lock() and unlock() to ensure that the threads execute these functions in the correct order.
#### How It Ensures Correct Order:
Initialization: Both firstDone and secondDone are locked initially. This setup ensures that second and third cannot execute until first and second complete, respectively.
Execution of first: When first runs, it prints "first" and then unlocks firstDone, signaling that second can proceed.
Execution of second: When second runs, it waits for firstDone to be unlocked (ensuring first has completed), prints "second", and then unlocks secondDone, signaling that third can proceed.
Execution of third: When third runs, it waits for secondDone to be unlocked (ensuring second has completed) and then prints "third".
The solution, implemented in the file solution.h, which uses a `nums` array of 3 elements, The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). 

I couldn't run my code in VSCode and after investigating why, I found C++11 or C11 Multithreading features are only supported by POSIX threads, so if you are using win32, multithreading won't be supported.

### Threads in the Code
In the `test.cpp` file, we create multiple threads to execute the functions `first`, `second`, and `third` concurrently. Each thread is responsible for executing one of the functions:
- **Thread 1**: Executes the `first` function.
- **Thread 2**: Executes the `second` function.
- **Thread 3**: Executes the `third` function.

Here’s how the threads are created and managed:
- We define the tasks for each thread using lambda functions that capture the output stream.
- We initialize the threads in a vector and assign the appropriate function (`first`, `second`, or `third`) to each thread based on the input array.
- We start the threads, and each thread waits for the necessary mutex to be unlocked before proceeding.
- Finally, we join the threads to ensure that the main program waits for all threads to complete before continuing.

### Example Inputs and Outputs
- Input: `nums = [2, 1, 3]`
- Output: `firstsecondthird Test Passed`
- Explanation: we have to make sure the functions run in order, despite being called differently.

# Tests
The test.cpp file creates an instance of the Foo class and three threads, each executing one of the methods (first, second, third). The threads are joined to ensure the main thread waits for their completion. We also check if the output is "firstsecondthird" and print whether each test passed or failed. Below are the details of the tests:

### Test Examples
Test Case 1: <br> 
Input: nums = [1, 2, 3] <br> 
Explanation: Thread A calls first(), Thread B calls second(), and Thread C calls third(). <br> 
Output: "firstsecondthird" <br> 
Result: Should print "Output: firstsecondthird" and "Test Passed".

Test Case 2: <br> 
Input: nums = [1, 3, 2] <br> 
Explanation: Thread A calls first(), Thread B calls third(), and Thread C calls second(). <br> 
Output: "firstsecondthird" <br> 
Result: Should print "Output: firstsecondthird" and "Test Passed".

Test Case 3: <br> 
Input: nums = [2, 1, 3] <br> 
Explanation: Thread A calls second(), Thread B calls first(), and Thread C calls third(). <br> 
Output: "firstsecondthird" <br> 
Result: Should print "Output: firstsecondthird" and "Test Passed".

Test Case 4: <br> 
Input: nums = [2, 3, 1] <br> 
Explanation: Thread A calls second(), Thread B calls third(), and Thread C calls first(). <br> 
Output: "firstsecondthird" <br> 
Result: Should print "Output: firstsecondthird" and "Test Passed".

Test Case 5: <br> 
Input: nums = [3, 1, 2] <br> 
Explanation: Thread A calls third(), Thread B calls first(), and Thread C calls second(). <br> 
Output: "firstsecondthird" <br> 
Result: Should print "Output: firstsecondthird" and "Test Passed".

Test Case 6: <br> 
Input: nums = [3, 2, 1] <br> 
Explanation: Thread A calls third(), Thread B calls second(), and Thread C calls first(). <br> 
Output: "firstsecondthird" <br> 
Result: Should print "Output: firstsecondthird" and "Test Passed".

# Analysis
### Other Possible Paradigms
**Functional Programming**
In functional programming, the problem can be approached by using pure functions and avoiding shared state. Instead of using locks or semaphores, we can structure the program to pass results from one function to the next explicitly, ensuring the correct order of execution.

Tradeoff: Functional programming can simplify reasoning about concurrency by eliminating side effects, but it might require a significant shift in design and can be less intuitive for those unfamiliar with the paradigm.

**Parallel Programming**
Parallel programming involves dividing the problem into smaller tasks that can be executed concurrently. We could use parallel constructs to ensure that each method (first, second, third) runs in parallel but synchronize their completion using barriers or other synchronization mechanisms.

Tradeoff: While parallel programming can improve performance by leveraging multiple processors, it can also introduce complexity in managing task dependencies and synchronization.

**Procedural Programming**
Procedural programming focuses on a sequence of imperative commands. This paradigm can solve the problem by using straightforward control structures like loops and conditionals to ensure the methods execute in order.

Tradeoff: Procedural solutions can be simple and easy to understand, but they might not leverage concurrency effectively, potentially leading to suboptimal performance.

**Logic Programming**
Logic programming, such as using Prolog, involves declaring rules and relationships that define the order of execution. The logic engine ensures that the methods are called in the correct order based on the defined rules.

Tradeoff: Logic programming can be highly expressive and powerful for certain types of problems, but it might not be as efficient or straightforward to implement for problems that require fine-grained control over thread execution.

The **time complexity** of each method (first, second, third) is O(1) as they each perform a constant amount of work: printing a message and locking/unlocking a mutex. The overall complexity remains O(1) since the operations are independent of any input size.

# References
- TylerMSFT. (2023, 7 February). mutex Class (C++ Standard Library). Microsoft Learn. https://learn.microsoft.com/en-us/cpp/standard-library/mutex-class-stl?view=msvc-170
- namespace «std» has no member «mutex». (s. f.). Stack Overflow. https://stackoverflow.com/questions/76794453/namespace-std-has-no-member-mutex
- GeeksforGeeks. (2023, 18 November). Multithreading in C. GeeksforGeeks. https://www.geeksforgeeks.org/multithreading-in-cpp/
