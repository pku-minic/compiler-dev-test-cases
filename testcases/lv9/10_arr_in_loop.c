int main() {
  int arr[10] = {1, 2, 3, 4, 5};
  int i = 0;
  while (i < 10) {
    int x[10] = {};
    arr[i] = arr[i] + i + x[i];
    x[i] = arr[i];
    i = i + 1;
  }
  return arr[9];
}
