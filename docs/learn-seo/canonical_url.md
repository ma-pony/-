# 权威链接标签

实际上就是一段固定的HTML代码，主要是去重，在相似页面中写入，将其指向主要的版本，

搜索引擎抓取的是网址而不是网页，所有他们认为某些页面是不同的页面
例如 https://example.com/sample-page?hello=world和https://example.com/sample-page
他们几乎是一样的页面，只是URL略有差别

那我们就可以把权威链接指向 https://example.com/sample-page，来避免重复爬取

[google 文档](https://developers.google.com/search/docs/advanced/crawling/consolidate-duplicate-urls)

```
<link rel="canonical" href="https://example.com/sample-page/" />
```

过多的重复内容可能会影响你的爬取配额，一个网站的爬取配额其实是有限的，当然，少于几千个页面的就不用担心了

如果没有指明权威链接，那么爬虫会自己来决定最佳的版本，具体规则未知

某些特殊情况下，即使你指定了你的权威链接，谷歌也有可能出于各种原因（效果或内容元素等等）选择了另一个页面


## 小tips
1. 使用绝对的网址
2. 使用小写的网址（大小写会被视为两个不同的地址
3. 使用正确的域名版本（https
4. 使用自引用权威链接（即当前页面的权威链接指向自身）
5. 每页只使用一个权威链接标签（如果设置了多个，那么多个都会被忽略


## 常见的设置方法
1. 使用HTML标签设置权威内容页面
即将下面代码加到网页的<head>中
```
<link rel="canonical" href="https://example.com/canonical-page/" />
```

2. 在HTTP标头中设置权威页面（像一些PDF文件
```
HTTP/1.1 200 OK
Content-Type: application/pdf
Link: <http://ahrefs.com/blog/canonical-tags/>; rel="canonical"
```

3. 在sitemap中设置权威页面
谷歌默认会将站点地图中列出的界面当做你建议的权威界面，但并不保证一定会将其视为权威，这样做最简单有效

4. 用301重定向到权威页面


## 常见的错误
1. 权威网址被robots.txt拒绝（这种页面不会被爬取，设置也无效
2. 将权威网址设置为noindex（这种权威页面仍然有效，canonical优先级高于noindex，但两者设置是相关矛盾的，不建议这样设置
3. 权威网址返回4xx
4. 将所有分页页面的权威页面都执行第一页
5. 权威页面带有hreflang标签
