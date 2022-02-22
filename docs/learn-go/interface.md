# 接口

## 什么是接口
接口也可以叫做协议
接口就是要求实现他的对象都遵循一个协议

python中是没有接口，但有类似的实现（抽象基类），都是在类里实现
例如Python中的Iterable类型，也可以算是一个接口
只要你自定义的类里实现了__iter__方法，遵循了这个协议，那么他就是一个Iterable类型


```go
// 定义协议
type Programmer interface {
	Coding (string) string
	Debugging (string) string
}

type GoProgrammer struct {

}


func (g GoProgrammer) Coding (string) string {
	return "go is good"
}

func (g GoProgrammer) Debugging (string) string {
	return "debug is good"
}
var pro Programmer = GoProgrammer{}
fmt.Printf("%T\n", pro)
```

打印pro的type你可以发现，pro是一个GoProgrammer类型，而不是Programmer类型，他只是实现了Programmer的协议
而且Programmer不能直接去实例化，接口类型不能实例化

而Python中的抽象基类不一样，是可以实例化的，他是class


## 接口的组合
