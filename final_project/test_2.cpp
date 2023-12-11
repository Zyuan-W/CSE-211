// Function Calls and Array coculation
#include <iostream>
using namespace std;

void incrementArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        arr[i]++;
    }
}

int main() {
    int myArray[5] = {1, 2, 3, 4, 5};
    incrementArray(myArray, 5);
    for (int i = 0; i < 5; i++) {
        cout << myArray[i] << " ";
    }
    cout << endl;
}

// def incrementArray(arr, size):
//     for i in range(size):
//         arr[i] += 1

// myArray = [1, 2, 3, 4, 5]
// incrementArray(myArray, 5)
// for i in myArray:
//     print(i, end=" ")
// print()
