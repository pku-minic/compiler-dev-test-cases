int main() {
  int a = 0;
  const int b = 1 - 1 * 2 + 1;
  int c = 1, d = 2;
  if (a || b) {
    c = 3;
  } else {
    d = 3;
    int a = 1;
    if (a || b) {
      c = 4;
    } else {
      d = 4;
    }
    if (a == 0) return 1;
    else if (a == 0 && a == -1) return 2;
  }
  return a + b + c + d;
}
