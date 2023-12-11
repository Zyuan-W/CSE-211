//test

#include <iostream>
using namespace std;

// Function declaration
int addNumbers(int a, int b);

int main() {
    // Variable declarations and assignments
    int x = 10;
    int y = 20;
    int sum;

    // Calling a function
    sum = addNumbers(x, y);

    // If-else statement
    if (sum > 20) {
        cout << "Sum is greater than 20." << endl;
    } else {
        cout << "Sum is less than or equal to 20." << endl;
    }

    // For loop
    cout << "For loop: ";
    for (int i = 0; i < 5; i++) {
        cout << i << " ";
    }
    cout << endl;


    for (int i = 1; i < size; i++) {
        b[0] += b[i];
    }

    // While loop
    cout << "While loop: ";
    int j = 0;
    while (j < 5) {
        cout << j << " ";
        j++;
    }
    cout << endl;

    return 0;
}

// Function definition
int addNumbers(int a, int b) {
    return a + b;
}
