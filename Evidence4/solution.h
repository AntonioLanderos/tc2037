#include <iostream>
#include <thread>
#include <mutex>
#include <functional>

using namespace std; 

class Foo {
     public:
        mutex firstDone;
        mutex secondDone;
    
      Foo() {
        firstDone.lock();
        secondDone.lock();
      }
    
      void first(function<void()> printFirst) {
        // printThird() outputs "third". Do not change or remove this line.
        printFirst();
        firstDone.unlock();
      }
    
      void second(function<void()> printSecond) {
        firstDone.lock();
        // printThird() outputs "third". Do not change or remove this line.
        printSecond();
        secondDone.unlock();
      }
    
      void third(function<void()> printThird) {
        secondDone.lock();
        // printThird() outputs "third". Do not change or remove this line.
        printThird();
      }
};