int init = 0;

void init1d(int n, int arr[]) {
  int i = 0;
  while (i < n) {
    arr[i] = init;
    init = init + 1;
    i = i + 1;
  }
}

void init2d(int n, int arr[][10]) {
  int i = 0;
  while (i < n) {
    init1d(10, arr[i]);
    i = i + 1;
  }
}

void init3d(int n, int arr[][10][10]) {
  int i = 0;
  while (i < n) {
    init2d(10, arr[i]);
    i = i + 1;
  }
}

int sum1d(int n, int arr[]) {
  int i = 0, sum = 0;
  while (i < n) {
    sum = sum + arr[i];
    i = i + 1;
  }
  return sum;
}

int sum2d(int n, int arr[][10]) {
  int i = 0, sum = 0;
  while (i < n) {
    sum = sum + sum1d(10, arr[i]);
    i = i + 1;
  }
  return sum;
}

int sum3d(int n, int arr[][10][10]) {
  int i = 0, sum = 0;
  while (i < n) {
    sum = sum + sum2d(10, arr[i]);
    i = i + 1;
  }
  return sum;
}

int main() {
  int arr[10][10][10];
  init3d(10, arr);
  int sum = sum3d(10, arr);
  sum = sum + sum2d(10, arr[1]);
  sum = sum + sum1d(10, arr[2][3]);
  putint(sum);
  putch(10);
  return sum;
}
