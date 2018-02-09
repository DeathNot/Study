# 第2章 复杂HTML解析
## 2.2 再端一碗BeautifulSoup
调用`findAll(tagName, tagAttributes)`可以获取页面中所有指定的标签。

`.get_text()`会把你正在处理的HTML文档中所有的标签都清除，然后返回一个只包含文本的字符串。通常情况下，应该最后才使用`.get_text()`。
``` python
findAll(tag, attributes, recursive, text, limit, keywords)
find(tag, attributes, recursive, text, keywords)
```
+ 标签参数tag，你可以传一个标签的名称或多个标签名称组成的python列表做标签参数。
+ 属性参数atttibutes是一个python字典封装一个标签的若干属性和对应的属性值。
+ 递归参数recursive是一个布尔变量。如果设置recursive的值为True， findAll就会根据你的要求去查找标签参数的所有子标签，以及子标签的子标签。如果设置为False，findAll就只查找文档的一级标签。findAll默认是支持递归查找的（recursive默认值为True）。
+ 文本参数text是用标签的文本内容去匹配，而不是用标签的属性。
+ 范围限制参数limit，如果你只对网页中获取的前x项结果感兴趣，就可以设置它。这个参数设置后，获得的前几项结果是按照网页上的顺序排序的，未必是你想要的前几项。
+ 关键词参数keyword，可以让你选择那些具有指定属性的标签。使用keyword偶尔会出现问题，尤其是在用class属性查找标签的时候。此时可以在class下面加一个下划线：
` bsObj.findAll(class_='green')`

### 2.2.2 其他BeautifulSoup对象
BeautifulSoup库里的四种对象：
+ BeautifulSoup对象
+ 标签Tag对象
+ NavigableString对象：用来表示标签里的文字，不是标签。
+ Comment对象：用来查找HTML文档的注释标签。

### 2.2.3 导航树
子标签是一个父标签的下一级，后代标签是指一个父标签下面所有级别的标签。一般情况下，BeautifulSoup函数总是处理当前标签的后代标签。如果只想找出子标签，可以用`.children`标签。

BeautifulSoup的next_siblings()函数可以让收集表格数据成为简单的事情。这个函数只调用后面的兄弟标签。还有`previous_siblings`、`next_sibling`、`previous_sibling`。

BeautifulSoup的父标签查找函数：parent和parents。
## 2.3 正则表达式
12个Python正则表达式中最常见的符号：

| 符号 | 含义|
| :---- | :-----:|
|*| 匹配前面的字符、子表达式或括号里的字符0次或多次
|+| 匹配前面的字符、子表达式或括号里的字符至少一次
|[]|匹配中括号内任意一个字符
|()|表达死编组
|{m,n}|匹配前面的字符、子表达式或括号里的字符m到n次，包含m和n
|[^]|匹配任意一个不在中括号内的字符
| &#124; |匹配任意一个由竖线分割的字符、子表达式
|.|匹配任意单个字符
|^|指字符串开始位置的字符或子表达式
|\\|转义字符
|$|经常用在正则表达式的末尾，表示“从字符串的末端匹配”。
|?!|“不包含”。通常放在字符或正则表达死前面，表示字符不能出现在目标字符串里。如果要在整个字符串中全部排除某个字符，就加上^和$符号。
## 2.4 正则表达式和BeautifulSoup
正则表达式可以作为BeautifulSoup语句的任意一个参数，让你的目标元素查找工作极具灵活性。
## 2.5 获取属性
对于一个标签对象，可以使用`myTag.attrs`获取它的全部属性。这行代码返回的是一个python字典对象。
## 2.6 Lambda表达式
Lambda表达式本质上就是一个函数，可以作为其他函数的变量使用。

BeautifulSoup允许我们把特定函数类型当作findAll函数的参数。唯一的限制条件是这些函数必须把一个标签作为参数并且返回结果是布尔类型。BeautifulSoup用这个函数来评估它遇到的每一个标签对象，最后把评估结果为真的标签保留，把其他标签剔除。示例如下：
`soup.findAll(lambda tag: len(tag.attrs) == 2)`
