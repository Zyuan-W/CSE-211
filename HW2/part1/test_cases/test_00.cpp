// expected to replace: 3

#include "stdio.h"
#include "time.h"
#include "stdlib.h"
#include <iostream>
#include <chrono>
using namespace std;

// From https://stackoverflow.com/questions/33058848/generate-a-random-double-between-1-and-1
/* generate a random floating point number from min to max */
double randfrom(double min, double max) 
{
    double range = (max - min); 
    double div = RAND_MAX / range;
    return min + (rand() / div);
}

double op_function(double a, double b, double c, double d, double e, double f, double g, double h, double i, double j, double k, double l) {
  // Start optimization range
    d = j - j;
    e = k - k;
    d = j + j;
    e = j + k;
    f = i + k;
    d = j - j;
    e = k + k;
    f = i - i;
    // End optimization range
    return d + e;
}

int main() {
    srand (0);
    double a,b,c,d,e,f,g,h,i,j,k,l;  
    a= randfrom(-100.0, 100.0);
    b= randfrom(-100.0, 100.0);
    c= randfrom(-100.0, 100.0);
    d= randfrom(-100.0, 100.0);
    e= randfrom(-100.0, 100.0);
    f= randfrom(-100.0, 100.0);
    g= randfrom(-100.0, 100.0);
    h= randfrom(-100.0, 100.0);
    i= randfrom(-100.0, 100.0);
    j= randfrom(-100.0, 100.0);
    k= randfrom(-100.0, 100.0);
    l= randfrom(-100.0, 100.0);
    // Timer code from https://www.techiedelight.com/measure-elapsed-time-program-chrono-library/
    auto start = chrono::steady_clock::now();
    double res;
    for (int i = 0; i < 2000000; i++) {
        res = op_function(a,b,c,d,e,f,g,h,i,j,k,l);
    }
    auto end = chrono::steady_clock::now();
    cout << "Elapsed time in milliseconds: "
        << chrono::duration_cast<chrono::milliseconds>(end - start).count()
        << " ms" << endl;
    printf("hash: %f\n", res);
    return 0;
}

