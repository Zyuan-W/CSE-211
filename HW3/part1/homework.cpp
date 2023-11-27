
#include <iostream>
#include <assert.h>
#include <chrono>
#include "checker_red_loop.h"
using namespace std;
using namespace std::chrono;

typedef double reduce_type;


void reference_reduction(reduce_type *b, int size) {
  for (int i = 1; i < size; i++) {
    b[0] += b[i];
  }
}
void homework_reduction(reduce_type *a, int size) {
  for (int i = 1; i < size/64; i++) {
    a[0] += a[i];
    a[1*size/64] += a[i+1*size/64];
    a[2*size/64] += a[i+2*size/64];
    a[3*size/64] += a[i+3*size/64];
    a[4*size/64] += a[i+4*size/64];
    a[5*size/64] += a[i+5*size/64];
    a[6*size/64] += a[i+6*size/64];
    a[7*size/64] += a[i+7*size/64];
    a[8*size/64] += a[i+8*size/64];
    a[9*size/64] += a[i+9*size/64];
    a[10*size/64] += a[i+10*size/64];
    a[11*size/64] += a[i+11*size/64];
    a[12*size/64] += a[i+12*size/64];
    a[13*size/64] += a[i+13*size/64];
    a[14*size/64] += a[i+14*size/64];
    a[15*size/64] += a[i+15*size/64];
    a[16*size/64] += a[i+16*size/64];
    a[17*size/64] += a[i+17*size/64];
    a[18*size/64] += a[i+18*size/64];
    a[19*size/64] += a[i+19*size/64];
    a[20*size/64] += a[i+20*size/64];
    a[21*size/64] += a[i+21*size/64];
    a[22*size/64] += a[i+22*size/64];
    a[23*size/64] += a[i+23*size/64];
    a[24*size/64] += a[i+24*size/64];
    a[25*size/64] += a[i+25*size/64];
    a[26*size/64] += a[i+26*size/64];
    a[27*size/64] += a[i+27*size/64];
    a[28*size/64] += a[i+28*size/64];
    a[29*size/64] += a[i+29*size/64];
    a[30*size/64] += a[i+30*size/64];
    a[31*size/64] += a[i+31*size/64];
    a[32*size/64] += a[i+32*size/64];
    a[33*size/64] += a[i+33*size/64];
    a[34*size/64] += a[i+34*size/64];
    a[35*size/64] += a[i+35*size/64];
    a[36*size/64] += a[i+36*size/64];
    a[37*size/64] += a[i+37*size/64];
    a[38*size/64] += a[i+38*size/64];
    a[39*size/64] += a[i+39*size/64];
    a[40*size/64] += a[i+40*size/64];
    a[41*size/64] += a[i+41*size/64];
    a[42*size/64] += a[i+42*size/64];
    a[43*size/64] += a[i+43*size/64];
    a[44*size/64] += a[i+44*size/64];
    a[45*size/64] += a[i+45*size/64];
    a[46*size/64] += a[i+46*size/64];
    a[47*size/64] += a[i+47*size/64];
    a[48*size/64] += a[i+48*size/64];
    a[49*size/64] += a[i+49*size/64];
    a[50*size/64] += a[i+50*size/64];
    a[51*size/64] += a[i+51*size/64];
    a[52*size/64] += a[i+52*size/64];
    a[53*size/64] += a[i+53*size/64];
    a[54*size/64] += a[i+54*size/64];
    a[55*size/64] += a[i+55*size/64];
    a[56*size/64] += a[i+56*size/64];
    a[57*size/64] += a[i+57*size/64];
    a[58*size/64] += a[i+58*size/64];
    a[59*size/64] += a[i+59*size/64];
    a[60*size/64] += a[i+60*size/64];
    a[61*size/64] += a[i+61*size/64];
    a[62*size/64] += a[i+62*size/64];
    a[63*size/64] += a[i+63*size/64];
  }
  a[0] += a[1*size/64];
  a[0] += a[2*size/64];
  a[0] += a[3*size/64];
  a[0] += a[4*size/64];
  a[0] += a[5*size/64];
  a[0] += a[6*size/64];
  a[0] += a[7*size/64];
  a[0] += a[8*size/64];
  a[0] += a[9*size/64];
  a[0] += a[10*size/64];
  a[0] += a[11*size/64];
  a[0] += a[12*size/64];
  a[0] += a[13*size/64];
  a[0] += a[14*size/64];
  a[0] += a[15*size/64];
  a[0] += a[16*size/64];
  a[0] += a[17*size/64];
  a[0] += a[18*size/64];
  a[0] += a[19*size/64];
  a[0] += a[20*size/64];
  a[0] += a[21*size/64];
  a[0] += a[22*size/64];
  a[0] += a[23*size/64];
  a[0] += a[24*size/64];
  a[0] += a[25*size/64];
  a[0] += a[26*size/64];
  a[0] += a[27*size/64];
  a[0] += a[28*size/64];
  a[0] += a[29*size/64];
  a[0] += a[30*size/64];
  a[0] += a[31*size/64];
  a[0] += a[32*size/64];
  a[0] += a[33*size/64];
  a[0] += a[34*size/64];
  a[0] += a[35*size/64];
  a[0] += a[36*size/64];
  a[0] += a[37*size/64];
  a[0] += a[38*size/64];
  a[0] += a[39*size/64];
  a[0] += a[40*size/64];
  a[0] += a[41*size/64];
  a[0] += a[42*size/64];
  a[0] += a[43*size/64];
  a[0] += a[44*size/64];
  a[0] += a[45*size/64];
  a[0] += a[46*size/64];
  a[0] += a[47*size/64];
  a[0] += a[48*size/64];
  a[0] += a[49*size/64];
  a[0] += a[50*size/64];
  a[0] += a[51*size/64];
  a[0] += a[52*size/64];
  a[0] += a[53*size/64];
  a[0] += a[54*size/64];
  a[0] += a[55*size/64];
  a[0] += a[56*size/64];
  a[0] += a[57*size/64];
  a[0] += a[58*size/64];
  a[0] += a[59*size/64];
  a[0] += a[60*size/64];
  a[0] += a[61*size/64];
  a[0] += a[62*size/64];
  a[0] += a[63*size/64];

}
#define UNROLL_FACTOR 64

#define SIZE (1024*1024*32)


int main() {
  reduce_type *a;
  a = (reduce_type *) malloc(SIZE * sizeof(reduce_type));

  reduce_type *b;
  b = (reduce_type *) malloc(SIZE * sizeof(reduce_type));

  for (int i = 0; i < SIZE; i++) {
    a[i] = 1;
    b[i] = 1;
  }

  auto new_start = high_resolution_clock::now();
  homework_reduction(a,SIZE);
  auto new_stop = high_resolution_clock::now();
  auto new_duration = duration_cast<nanoseconds>(new_stop - new_start);
  double new_seconds = new_duration.count()/1000000000.0;

  auto ref_start = high_resolution_clock::now();
  reference_reduction(b,SIZE);
  auto ref_stop = high_resolution_clock::now();
  auto ref_duration = duration_cast<nanoseconds>(ref_stop - ref_start);
  double ref_seconds = ref_duration.count()/1000000000.0;

  // Do not remove
  check_values(b, a, SIZE);

  double speedup = ref_seconds / new_seconds;
  cout << "new loop time: " << new_seconds << endl;
  cout << "reference loop time: " << ref_seconds << endl;
  cout << "speedup: " << speedup << endl << endl;

  return 0;
}
