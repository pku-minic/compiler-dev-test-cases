int main() {
  int a = 10;
  if (a > 1)
    if (a > 2)
      if (a < 3)
        return a;
      else
        if (a > 4)
          if (a < 5)
            return a + 1;
          else
            return a + 2;
  return -1;
}
