int main() {
  int i = 0, sum = 0;
  while (i < 10) {
    if (i == 5) {
      sum = sum + 7;
      i = i + 1;
      continue;
    }
    sum = sum + i;
    i = i + 1;
  }
  return sum;
}
