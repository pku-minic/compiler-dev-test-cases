int main() {
  int i = 0, sum = 0;
  while (i < 10) {
    if (i == 5) {
      sum = sum + 1;
    } else {
      sum = sum + i;
    }
    if (sum > 10) sum = sum - 1;
    i = i + 1;
  }
  return sum;
}
