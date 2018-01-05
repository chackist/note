## twisted 框架学习

### Transports
Transports抽象是通过Twisted中interfaces模块中ITransport接口定义的。一个Twisted的Transport代表一个可以收发字节的单条连接。对于我们的诗歌下载客户端而言，就是对一条TCP连接的抽象。但是Twisted也支持诸如Unix中管道和UDP。Transport抽象可以代表任何这样的连接并为其代表的连接处理具体的异步I/O操作细节。

如果你浏览一下ITransport中的方法，可能找不到任何接收数据的方法。这是因为Transports总是在低层完成从连接中异步读取数据的许多细节工作，然后通过回调将数据发给我们。相似的原理，Transport对象的写相关的方法为避免阻塞也不会选择立即写我们要发送的数据。告诉一个Transport要发送数据，只是意味着：尽快将这些数据发送出去，别产生阻塞就行。当然，数据会按照我们提交的顺序发送。

通常我们不会自己实现一个Transport。我们会去使用Twisted提供的实现类，即在传递给reactor时会为我们创建一个对象实例。

```
class ITransport(Interface):
    def write(data):
    def writeSequence(data):
    def loseConnection():
    def getPeer():
    def getHost():
```

### Protocols
Twisted的Protocols抽象由interfaces模块中的IProtocol定义。也许你已经想到，Protocol对象实现协议内容。也就是说，一个具体的Twisted的Protocol的实现应该对应一个具体网络协议的实现，像FTP、IMAP或其它我们自己制定的协议。我们的诗歌下载协议，正如它表现的那样，就是在连接建立后将所有的诗歌内容全部发送出去并且在发送完毕后关闭连接。

严格意义上讲，每一个Twisted的Protocols类实例都为一个具体的连接提供协议解析。因此我们的程序每建立一条连接（对于服务方就是每接受一条连接），都需要一个协议实例。这就意味着，Protocol实例是存储协议状态与间断性（由于我们是通过异步I/O方式以任意大小来接收数据的）接收并累积数据的地方。

因此，Protocol实例如何得知它为哪条连接服务呢？如果你阅读IProtocol定义会发现一个makeConnection函数。这是一个回调函数，Twisted会在调用它时传递给其一个也是仅有的一个参数，即Transport实例。这个Transport实例就代表Protocol将要使用的连接。

Twisted内置了很多实现了通用协议的Protocol。你可以在twisted.protocols.basic中找到一些稍微简单点的。在你尝试写新Protocol时，最好是看看Twisted源码是不是已经有现成的存在。如果没有，那实现一个自己的协议是非常好的，正如我们为诗歌下载客户端做的那样。
```
class IProtocol(Interface):
    def dataReceived(data):
    def connectionLost(reason):
    def makeConnection(transport):
    def connectionMade():
```

### Protocol Factories
因此每个连接需要一个自己的Protocol，而且这个Protocol是我们自己定义的类的实例。由于我们会将创建连接的工作交给Twisted来完成，Twisted需要一种方式来为一个新的连接创建一个合适的协议。创建协议就是Protocol Factories的工作了。

也许你已经猜到了，Protocol Factory的API由IProtocolFactory来定义，同样在interfaces模块中。Protocol Factory就是Factory模式的一个具体实现。buildProtocol方法在每次被调用时返回一个新Protocol实例，它就是Twisted用来为新连接创建新Protocol实例的方法。
```
class IProtocolFactory(Interface):
    def buildProtocol(addr):
    def doStart():
    def doStop():
```

### 常用api
* reactor.callLater
* 1.deferred = defer.Deferred() 2.deferred.addBoth() 3.deferred.callback deferred.errback
