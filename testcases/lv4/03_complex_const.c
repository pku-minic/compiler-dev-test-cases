int main() {
  const int x = 1 * 2 || 2 * 3 && 3 * 4;
  const int y = x * 3 > 10;
  return y + 4 - x;
}
