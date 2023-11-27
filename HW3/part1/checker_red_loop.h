#include <assert.h>
#include <iostream>

void check_values(double *ref, double *actual, int size) {
    
    assert(ref[0] == actual[0]);
    
    std::cout << "Match!\n";
} 
