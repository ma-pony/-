# net/rpc
go自带的rpc包

service
```go
package main

import (
	"net/rpc"
	"net"
)

// 必须要是一个结构体
type HelloService struct {

}

func (s *HelloService) Hello(request string, reply *string) error {
    // reply是一个引用类型，就可以去修改他的值
	// 返回值是通过修改reply的值来实现的
	*reply = "hello:" + request
	return nil
}

func main() {
	_ = rpc.RegisterName("HelloService", new(HelloService))
	
	// rpc不是一个service，要依赖Listen去监听端口来获取调用
	listener, _ := net.Listen("tcp", ":1234")
	conn, _ := listener.Accept()
	
	// 接收连接之后，再将连接传递到rpc.ServeConn
	rpc.ServeConn(conn)
}
```


client
```go
package main

import (
	"fmt"
	"net/rpc"
)

func main() {
    // rpc也没有自己的client端
    // 需要借助net/rpc包的Dial函数去连接服务端
	client, _ := rpc.Dial("tcp", ":1234")
	var reply string
    // 将返回值传递到连接中
	_ = client.Call("HelloService.Hello", "world", &reply)
	// client接收到返回值后回去修改reply的值
	fmt.Println(reply)

}
```
