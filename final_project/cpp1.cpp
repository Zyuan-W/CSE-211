

#include <iostream>
using namespace std;

// Function definition
int addNumbers(int a, int b) {
    return a + b;
  

}

int main() {
    // Variable declarations and assignments
    int x = 10;
    int y = 20;
    int j = x + y;
    j = x + y;
    int sum;

    int *a;
    a = (int *) malloc(sizeof(int) * 10);
    a[1] = 1;

    int *b;
    b = (int *) malloc(sizeof(int) * 10);


    // Calling a function
    sum = addNumbers(x, y);

    // If-else statement
    if (sum > 20) {
        cout << "Sum is greater than 20. sum = " << sum << endl;
    } else {
        cout << "Sum is less than or equal to 20.  sum = " << sum << endl;
    }



    // For loop
    cout << "For loop: ";
    for (int i = 0; i < 5; i++) {
        cout << i << " ";
    }
    cout << endl;

    // While loop
    cout << "While loop: ";
    int j = 5;
    while (j >= 0) {
        cout << j << " ";
        j--; 
    }
    cout << endl;

}




