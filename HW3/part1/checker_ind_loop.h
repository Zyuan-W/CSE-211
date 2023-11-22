#include <assert.h>
#include <iostream>

void check_values(float *ref, float *actual, int size) {
    // compare the two arrays, if they are the same, the program will continue,
    // if not the program will terminate 
    
    for (int i = 0; i < size; i++) {
        assert(ref[i] == actual[i]);
    }

    std::cout << "Match!" << std::endl;

} 
