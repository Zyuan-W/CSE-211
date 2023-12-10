// Test with nested if
#include <iostream>
using namespace std;

int main() {
    int a = 3;
    int b = 4;
    int c = 5;
    int result;

    if (a < b) {
        if (b < c) {
            result = c;
        } else {
            result = b;
        }
    } else {
        result = a;
    }

    cout << "result = " << result << endl;
}
