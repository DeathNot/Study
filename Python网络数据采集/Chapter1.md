# 第1章 初见网络爬虫
## 1.1 网络连接
urlopen用来打开并读取一个从网络获取的远程对象。
## 1.2 BeautifulSoup简介
`html = urlopen('http://pythonscraping.com/pages/page1.html') `
这行代码主要可能会发生两种异常：
+ 网页在服务器上不存在（或者获取网页的时候出现错误）
+ 服务器不存在

第一种异常发生时，程序会返回HTTP错误，urlopen函数会抛出“HTTPError”异常，可以采用下面的方式处理这种异常：
``` python
try:
  html = urlopen('http://pythonscraping.com/pages/page1.html')
except HTTPError as e:
  print(e)
  # 返回空值，中断程序，或者执行另一个方案
else:
  # 程序继续。注意：如果你已经在上面异常捕捉那一段代码里返回或中断(break),
  # 那么就不需要使用else语句了，这段代码也不会执行
```
如果程序返回HTTP错误代码，程序就会显示错误内容，不再执行else语句后面的代码。

如果服务器不存在，urlopen会返回一个None对象。我们可以增加一个判断语句检测返回的html是不是None：
``` python
if html is None:
  print("URL is not found")
else:
  # 程序继续
```
在使用BeautifulSoup的时候，每当调用BeautifulSoup对象里的一个标签时，如果想要调用的标签不存在，就会返回一个None对象。如果再调用这个None对象下面的子标签，就会发生`AttributeError`错误。

避免这种异常最简单的方式就是对两种情形进行检查：
``` python
try:
  badContent = bsObj.nonExistingTag.anotherTag
except AttributeError as e:
  print('Tag was not found')
else:
  if badContent == None:
    print('Tag was not found')
  else:
    print(badContent)
```
