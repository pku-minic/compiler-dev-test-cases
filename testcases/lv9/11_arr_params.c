void f1d(int arr[]) {
  int i = 0;
  while (i < 10) {
    arr[i] = i;
    i = i + 1;
  }
}

void f2d(int arr[][8 + 2]) {
  arr[1][2] = 3;
  int i = 0;
  while (i < 10) {
    f1d(arr[i]);
    i = i + 1;
  }
}

int main() {
  return 33;
}
