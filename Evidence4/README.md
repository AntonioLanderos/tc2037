# Description
### Context of the Problem
The problem "1114. Print in Order" from LeetCode requires ensuring that three methods (first, second, third) are executed in the correct order, despite being called from different threads. This problem is an example of a common concurrency issue where the order of execution needs to be controlled to maintain correct behavior. Solving this problem ensures that multithreaded applications behave deterministically and avoids issues that can arise from race conditions.

### Why It Is Useful
Concurrency is a fundamental concept in modern programming, allowing multiple operations to be performed simultaneously. It is widely used in applications that require parallel processing, such as web servers, data processing, and real-time systems. Understanding how to control the order of execution in a concurrent environment is crucial for building reliable and efficient systems.

# Model of the solution
Let's model the problem using a diagram that represents the state transitions controlled by mutex.
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

For the implementation of the solution for this problem I used C++ with the help of its libraries: thread, mutex, and functional because leetcode's base template was already using it. 
Mutex and thread are are part of the standard C++ library and they are a powerful tool for working with multithreading. Mutex's method lock() is used to block the calling thread until the thread obtains ownership of the mutex and unlock() is used to release the ownership of the mutex.

I used this simple analogy for a better understanding of the problem: 
- lock(): When you want to use the bathroom, you take the key (lock the door). If someone else is already using the bathroom (the door is locked), you wait until they are done and the door is unlocked.
- unlock(): After you finish using the bathroom, you return the key (unlock the door), so the next person can use it.

### C++ Code
The C++ code provided defines 3 functions which print "first", "second", and "third". We use lock() and unlock() to ensure that the threads execute these functions in the correct order.
How It Ensures Correct Order:
Initialization: Both firstDone and secondDone are locked initially. This setup ensures that second and third cannot execute until first and second complete, respectively.
Execution of first: When first runs, it prints "first" and then unlocks firstDone, signaling that second can proceed.
Execution of second: When second runs, it waits for firstDone to be unlocked (ensuring first has completed), prints "second", and then unlocks secondDone, signaling that third can proceed.
Execution of third: When third runs, it waits for secondDone to be unlocked (ensuring second has completed) and then prints "third".
The solution, implemented in the file solution.h, which uses a `nums` array of 3 elements, The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). 

I couldn't run my code in VSCode and after investigating why, I found C++11 or C11 Multithreading features are only supported by POSIX threads, so if you are using win32, multithreading won't be supported.

### Example Inputs and Outputs
- Input: `nums = [2, 1, 3]`
- Output: `firstsecondthird Test Passed`
- Explanation: we have to make sure the functions run in order, despite being called differently.

# Tests
The test.cpp file creates an instance of the Foo class and three threads, each executing one of the methods (first, second, third). The threads are joined to ensure the main thread waits for their completion. We also check if the output is "firstsecondthird" and print whether each test passed or failed. Below are the details of the tests:

### Test Examples
Test Case 1:
Input: nums = [1, 2, 3]
Explanation: Thread A calls first(), Thread B calls second(), and Thread C calls third().
Output: "firstsecondthird"
Result: Should print "Output: firstsecondthird" and "Test Passed".

Test Case 2:
Input: nums = [1, 3, 2]
Explanation: Thread A calls first(), Thread B calls third(), and Thread C calls second().
Output: "firstsecondthird"
Result: Should print "Output: firstsecondthird" and "Test Passed".
Test Case 3:

Input: nums = [2, 1, 3]
Explanation: Thread A calls second(), Thread B calls first(), and Thread C calls third().
Output: "firstsecondthird"
Result: Should print "Output: firstsecondthird" and "Test Passed".

Test Case 4:
Input: nums = [2, 3, 1]
Explanation: Thread A calls second(), Thread B calls third(), and Thread C calls first().
Output: "firstsecondthird"
Result: Should print "Output: firstsecondthird" and "Test Passed".

Test Case 5:
Input: nums = [3, 1, 2]
Explanation: Thread A calls third(), Thread B calls first(), and Thread C calls second().
Output: "firstsecondthird"
Result: Should print "Output: firstsecondthird" and "Test Passed".

Test Case 6:
Input: nums = [3, 2, 1]
Explanation: Thread A calls third(), Thread B calls second(), and Thread C calls first().
Output: "firstsecondthird"
Result: Should print "Output: firstsecondthird" and "Test Passed".

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
