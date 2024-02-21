#include <klee/klee.h>

// A simple binary search function
int binary_search(int arr[], int l, int r, int x) {
  while (l <= r) {
    int m = l + (r - l) / 2;

    // Check if x is present at mid
    if (arr[m] == x)
      return m;

    // If x greater, ignore left half
    if (arr[m] < x)
      l = m + 1;

    // If x is smaller, ignore right half
    else
      r = m - 1;
  }

  // if we reach here, then element was not present
  return -1;
}

int main() {
  int arr[5];
  int x;
  int n = sizeof(arr) / sizeof(arr[0]);

  // Make the array and the search key symbolic
  klee_make_symbolic(arr, sizeof(arr), "arr");
  klee_make_symbolic(&x, sizeof(x), "x");

  // Assume the array is sorted for binary search to work
  for (int i = 1; i < 5; ++i) {
    klee_assume(arr[i-1] <= arr[i]);
  }

  int result = binary_search(arr, 0, n - 1, x);

  // Check for correctness or any specific property you are interested in
  if (result != -1) {
        if (!(arr[result] == x)) {
            klee_report_error("binary_search.cpp", __LINE__, "Assertion failed", "assert");
        }
  }

  return 0;
}

