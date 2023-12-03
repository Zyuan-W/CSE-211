


void reference_reduction(int *b, int size) {
  for (int i = 1; i < size; i++) {
    b[0] += b[i];
  }
}