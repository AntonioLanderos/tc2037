#include "concurrency.h"
#include <vector>
#include <sstream>

bool testFoo(const std::vector<int>& nums) {
  Foo foo;

  std::stringstream output;

  auto printFirst = [&output]() { output << "first"; };
  auto printSecond = [&output]() { output << "second"; };
  auto printThird = [&output]() { output << "third"; };

  std::vector<std::thread> threads(3);

  for (int i = 0; i < 3; ++i) {
      if (nums[i] == 1) {
          threads[i] = std::thread(&Foo::first, &foo, printFirst);
      } else if (nums[i] == 2) {
          threads[i] = std::thread(&Foo::second, &foo, printSecond);
      } else if (nums[i] == 3) {
          threads[i] = std::thread(&Foo::third, &foo, printThird);
      }
  }

  for (int i = 0; i < 3; ++i) {
      threads[i].join();
  }

  std::string result = output.str();
  std::cout << "Output: " << result << std::endl;
  return result == "firstsecondthird";
}

int main() {
  std::vector<std::vector<int>> testCases = {
      {1, 2, 3}, // Example 1
      {1, 3, 2}, // Example 2
      {2, 1, 3}, // Additional test case
      {2, 3, 1}, // Additional test case
      {3, 1, 2}, // Additional test case
      {3, 2, 1}  // Additional test case
  };

  for (const auto& testCase : testCases) {
      bool passed = testFoo(testCase);
      std::cout << "Test " << (passed ? "Passed" : "Failed") << std::endl;
  }

  return 0;
}


