int main() {
  int a[10], b[2][3] = {1, 2, 3, 4}, sum = 0;
  int i = 0;
  while (i < 2) {
    int j = 0;
    while (j < 3) {
      sum += b[i][j];
      j = j + 1;
    }
    i = i + 1;
  }
  i = 0;
  while (i < 10) {
    a[i] = sum + i;
    i = i + 1;
  }
  return sum;
}
