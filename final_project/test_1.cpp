// Nested Loops and Conditional Statements

#include <iostream>
using namespace std;

int main() {
    int sum = 0;
    for (int i = 1; i <= 5; i++) {
        for (int j = 1; j <= i; j++) {
            if (i == j) {
                sum += i;
            }
        }
    }
    cout << "Sum = " << sum << endl;
}

// sum = 0
// for i in range(1, 6):
//     for j in range(1, i + 1):
//         if i == j:
//             sum += i
// print("Sum =", sum)
