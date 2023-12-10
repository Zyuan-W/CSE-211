// Test with else
#include <iostream>
using namespace std;

int main() {
    int x = 5;
    int y = 10;
    int z = 15;
    int condition = 1;

    if (condition > 0) {
        x = 100;
        y = 200;
    } else {
        x = -1;
        y = -2;
    }

    int result = x + y + z;
    cout << "result = " << result << endl;
}
