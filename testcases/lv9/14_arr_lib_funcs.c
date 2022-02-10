int main() {
  int arr[10], n = getarray(arr);
  int i = 0;
  while (i < 10) {
    if (i < n) {
      arr[i] = arr[i] + i;
    } else {
      arr[i] = arr[i - 1] + i;
    }
    i = i + 1;
  }
  putarray(n, arr);
  return 0;
}
