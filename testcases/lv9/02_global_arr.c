int a[10];
const int len = 10;
int b[8 + 2], c, d[len];
int e[5][6];
int f[5][6], g, h[5][6];

int main() {
  // global value should zero init
  return a[len - 1] + b[len -1] + d[len - 1] + e[0][0];
}
