# compiler-dev-test-cases

为 SysY 编译器设计的本地测试用例, 已经包含于[编译器开发环境](https://github.com/pku-minic/compiler-dev).

`testcases` 目录内存放了测试用例的源文件, 并且已经按照[编译实践在线文档](https://pku-minic.github.io/online-doc/)的章节划分分类.

## 使用方法

由于 `compiler-dev` 已经包含了全部测试用例, 我们不建议你直接使用该仓库.

如果你需要另行构建测试用例, 可以执行:

```sh
LIB_DIR="SysY运行时库目录" INSTALL_DIR="测试用例安装目录" make install -j`nproc`
```

`make` 将使用 `clang` 编译并运行所有测试用例, 自动获取参考输出, 然后将测试用例及参考输入/输出复制至 `INSTALL_DIR`.

## 其他测试用例

本仓库只包含了一些结构较为简单的 SysY 测试用例, 如果你想进一步测试你的 SysY 编译器, 请参考之前版本的[开放测试用例仓库](https://github.com/pku-minic/open-test-cases).
