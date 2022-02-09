int main() {
  int a = 1, b = 2;
  while (a < 10) {
    a = a + 1;
    while (a < 5 && b < 10) {
      b = b + 1;
    }
    while (b < 20) {
      while (b < 6 || b == 6) {
        b = b + 1;
      }
      b = b + 2;
    }
  }
  return a + b;
}
