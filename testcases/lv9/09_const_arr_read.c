int main() {
  const int arr[10] = {1, 2, 3, 4, 5};
  int i = 0, sum = 0;
  while (i < 10) {
    sum += arr[i];
    i = i + 1;
  }
  return sum;
}
