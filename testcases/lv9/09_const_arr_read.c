const int garr[10] = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15};

int main() {
  const int arr[10] = {1, 2, 3, 4, 5};
  int i = 0, sum = 0;
  while (i < 10) {
    sum = sum + arr[i] + garr[i];
    i = i + 1;
  }
  return sum;
}
