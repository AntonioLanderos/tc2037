#include "solution.h"

int main() {
  Foo foo;

  auto printFirst = []() { cout << "first"; };
  auto printSecond = []() { cout << "second"; };
  auto printThird = []() { cout << "third"; };

  thread t1(&Foo::first, &foo, printFirst);
  thread t2(&Foo::second, &foo, printSecond);
  thread t3(&Foo::third, &foo, printThird);

  t1.join();
  t2.join();
  t3.join();
  return 0;
}


