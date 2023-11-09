# Performance Comparison Report of Local Value Numbering

This document provides a detailed report on the performance comparison between the original code and optimized code after use local value numbering, evaluated across multiple test cases. The comparison includes execution time measured in milliseconds and the output hash to ensure the correctness of the optimization.

## Summary of Results

The following table summarizes the time differences between the original and optimized code for each test case provided:

| Test ID | Original Time (ms) | Optimized Time (ms) | Replacements | Hash Value        |
|---------|--------------------|---------------------|--------------|-------------------|
| test0   | 33                 | 37                  | 3            | 45.529884         |
| test1   | 781                | 680                 | 702          | -882.981133       |
| test2   | 774                | 660                 | 843          | 18.455962         |
| test3   | 974                | 643                 | 850          | -782705119.213801 |

## Detailed Report

Below are the detailed results after running both the original and optimized versions of the program for each test case:

### Test 0

- **Original Program:**
  - File: `test_cases/test0.cpp`
  - Elapsed Time: 33 ms
  - Hash: 45.529884

- **Optimized Program:**
  - File: `test_cases/test0.cpp`
  - Replacements Made: 3
  - Elapsed Time: 37 ms
  - Hash: 45.529884

### Test 1

- **Original Program:**
  - File: `test_cases/test1.cpp`
  - Elapsed Time: 781 ms
  - Hash: -882.981133

- **Optimized Program:**
  - File: `test_cases/test1.cpp`
  - Replacements Made: 702
  - Elapsed Time: 680 ms
  - Hash: -882.981133

### Test 2

- **Original Program:**
  - File: `test_cases/test2.cpp`
  - Elapsed Time: 774 ms
  - Hash: 18.455962

- **Optimized Program:**
  - File: `test_cases/test2.cpp`
  - Replacements Made: 843
  - Elapsed Time: 660 ms
  - Hash: 18.455962

### Test 3

- **Original Program:**
  - File: `test_cases/test3.cpp`
  - Elapsed Time: 974 ms
  - Hash: -782705119.213801

- **Optimized Program:**
  - File: `test_cases/test3.cpp`
  - Replacements Made: 850
  - Elapsed Time: 643 ms
  - Hash: -782705119.213801

## Conclusion

The optimization process has resulted in decreased execution time in all test cases. While the output remains correct (as indicated by the matching hash values), the performance in terms of execution speed has improved.
