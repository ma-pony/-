# 包管理

Proxy 里要多配置一个源`https://goproxy.io`,来提供下载包的速度。

项目下边会有一个go.mod的文件,默认内容很简单
```go
module learn-go // 指定包名

go 1.14 // 指定版本

```

go的包管理相对Python要复杂很多

go 同一个文件夹下边的文体中不允许声明不同的package（新的文件夹中可以
每个文件夹都是一个单独的命名空间

go import包要是 `import "根包路径名/子包路径名"`
要注意是路径名，因为路径名和package名是允许不一样的，路径名才是准确找到

```
-- pag1
-- -- a.go package a
-- -- b.go package b
这样是会报错的
```
但使用的时候要用package名, package.func()

在Python中可以直接import包里的函数和变量，但go不行，因为go import的是路径，不是module，他找不到里边的函数和变量

go 里边只有同属一个包内，及时不在同一个文件中，也能相互调用，不用import
Python同属一个包其实也可以相互调用时，但Python的每个文件都被当做一个单独的包命名空间了，所以不能用，要import


go导包还有一种特殊的导入方式
`import . package` 他会将包的函数变量等直接合并到当前包，就可以直接调用func(),而不用package.func() 
类似于 Python的 `import *`

## 别名
go里的包别名是前置的，与Python的 as 正好相反
`import 别名 "包路径"` 
别名还可以设置为 _ ,即匿名引用，


