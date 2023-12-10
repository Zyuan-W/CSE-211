// Test with for loop and multiple conditions
#include <iostream>
using namespace std;

int main() {
    int sum = 0;

    for (int i = 0; i <= 10; i++) {
        if (i % 2 == 0) {
            sum += i;
        } else {
            sum -= i;
        }
    }

    cout << "sum = " << sum << endl;
}
