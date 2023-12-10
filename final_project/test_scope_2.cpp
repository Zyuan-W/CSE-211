// Test with while loop
#include <iostream>
using namespace std;

int main() {
    int i = 0;
    int sum = 0;

    while (i < 5) {
        sum += i;
        i++;
    }

    cout << "sum = " << sum << endl;
}
