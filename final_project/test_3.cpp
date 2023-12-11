// Complex Control Flow
#include <iostream>
using namespace std;

int main() {
    int x = 5;
    if (x > 0) {
        x += 10;
        if (x < 20) {
            x -= 4;
        }
    } else {
        x = 1;
    }
    cout << "x = " << x << endl;
}

x = 5
if x > 0:
    x += 10
    if x < 20:
        x -= 4
else:
    x = 1
print("x =", x)
