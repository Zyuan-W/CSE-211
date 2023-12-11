// scope_test

#include <iostream>
using namespace std;

int main (){
    int a = 10;
    int b = 20;
    int c = 30;
    int check = 0;

    if (check > 0){check += 1;if (check > 1){check += 2;} else {check += 3;}}


    int result = a + b + c;
    cout << "result = " << result << endl;


}
