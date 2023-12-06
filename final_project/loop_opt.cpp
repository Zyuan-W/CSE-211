
int addNumbers(int a, int b) {
    return a + b;

}

void reference_reduction(int *b, int size) {
  for (int i = 1; i < size; i++) {
    b[0] += b[i];
  }
}

int subNumbers(int d, int c) {
    return d - c;

}

void reference_reduction(int *n, int size) {
  for (int i = size; i >= 1; i++) {
    n[1] += n[i];
  }
}
