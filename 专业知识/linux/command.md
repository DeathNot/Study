# 一. 目录及文件的基本操作
1. pwd    显示当前工作的目录

   参数：
   >-p    显示链接的真实目录

2. cd    切换当前工作目录
    >cd -： 返回上一个目录

3. ls    显示目录与文件信息

    参数：
    >-a    显示所有，包括隐藏文件与目录

    >-d    显示目录本身的信息，而非目录下的文档信息

    >-h    人性化显示容量信息

    >-l    长格式显示文档的详细信息

    >-u    显示文件或目录最后被访问的时间

    >-t    以修改时间排序，ls命令默认是按文件名排序的。

4. touch    创建或修改文件时间，如果文件不存在，则创建，否则修改文件所有的时间为当前系统时间。
5. mkdir    创建目录

    参数：
    >-p    创建多级目录

6. cp    复制文件及目录

    用法：cp [选项] 源 目录

    参数：
    >-r    递归，复制子文件与子目录，一般复制目录时使用

    >-a    复制时保留源文档的所有属性（包括权限、时间等）

7. rm    删除文件或目录

    参数：
    >-f    不提示，强制删除

    >-i    删除前，提示是否删除

    >-r    递归删除，强制删除目录以及目录下的所有内容

8. mv    移动（重命名）文件或目录
9. find    搜索文件或目录

    用法：find [选项] [路径] [表达式选项]

    参数：

    >-empty    查找空白文件或目录

    >-group    按组查找

    >-name    按文档名称查找

    >-iname    按文档名称查找，且不区分大小写

    >-mtime    按修改时间查找

    >-size    按容量大小查找

    >-type    按文档类型查找，文件(f)、目录(d)、设备(b,c)
    、链接(l)等

    >-user    按用户查找

    >-exec    对找到的档案执行特定的命令

    >-a    并且

    >-o    或者

10. du    计算文件或目录的容量

    参数：

    >-h    人性化显示容量信息

    >-a    查看所有目录以及文件的容量信息

    >-s    仅显示总容量
    
