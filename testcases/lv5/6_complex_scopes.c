int main() {
  int a = 1, k = 0;
  {
    a = a + 2;
    int b = a + 3;
    b = b + 4;
    k = k + a + b;
    {
      b = b + 5;
      int c = b + 6;
      a = a + c;
      k = k + a + b + c;
      {
        b = b + a;
        int a = c + 7;
        a = a + 8;
        k = k + a + b + c;
        {
          b = b + a;
          int b = c + 9;
          const int a = 100;
          b = b + 10;
          k = k + a + b + c;
          {
            c = c + b;
            int c = b + 11;
            c = c + a;
            k = k + a + b + c;
          }
          k = k - c;
        }
        k = k - b;
      }
      k = k - a;
    }
  }
  return k % 77;
}
