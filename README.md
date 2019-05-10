`Python` `Algorithm` `CLI` `Computer fundamentals`

在接下来的日子里，我每天会至少用 python 编写一个程序，记录学习的重点:blush:。  
内容包括
* 数据结构
* 基础算法
* python的语法特性
* 一些实用小工具

# Part1. 数据结构
  在python新建类， 实现基础的数据结构。每一种数据结构可能有多种不同的实现，一部分可以当做学习邓俊辉老师课程的笔记， 一部分来自 Dan Bader 的系列博客，一部分来自自己所感所悟进行编写。
### 链表
  * 单链表  
      * [初始版](/DataStructure/SinglyLinkedList.py)：实现链表的多个接口，增删改消➕反转  
      * [加强版](/DataStructure/SinglyLinkedList_strengthen.py)：增加头哨兵，减少麻烦的·头·判断
  * 双链表  
      * [初始版](/DataStructure/DoublyLinkedList.py):  实现双链表的多个接口
      * [加强版](/DataStructure/DoublyLinkedList_strength.py): 增加头尾哨兵, 并在节点类的基础上添加插入方法
### 队列  
  [用双链表实现队列](/DataStructure/queue_use_by_doubly_list.py)
### 栈  
  [用双链表实现栈](/DataStructure/stack_use_by_doubly_list.py)

# Part2. 基础算法  
  这一部分的学习资料来自邓俊辉老师课程、著名的《Algorithm》、简书、掘金等  

### 理解递归  
  关于递归这个概念,需要掌握三点:  
  * 明确递归函数的作用,并且相信它能够达成目的
  * 寻找到递归基,也就是结束的条件,不然会无限递归
  * 找到递归函数的等价关系式.比如f(n) = n*f(n-1)
  示例:[单链表的翻转](/Algorithm/reverse_list.py)  
### 冒泡排序  
  [实现特点](/Algorithm/bubble_sort.py) ：若中途已经有序，则不必继续‘冒泡’
### 归并排序  
  [代码](/Algorithm/merge_sort.py) : 先递归划分数组,然后向上合并
### 二分查找
  [代码](/Algorithm/binary_search.py) : 将加法改成减法,防止溢出

# Part3. python 知识点
  python 的进阶之路，学习资料来自《Fluent Python》、python 标准库等
### 特殊方法（Dunder method）
  体现 python 的一致性  
  [特殊方法__missing__](/Python-Knowledge/)  
    所有的映射类型在处理找不到键时,都会调用__missing__方法.
    * 基类dict并没有定义这个方法,但是dict是知道有这么个东西
    * 继承自dict的类,如果提供了__missing__方法,那么在__getitem__找不到键时,会调用它;如果没有提供__misssing__,则会直接抛出KeyError异常
    * 提供__missing__方法对get或者__contains__(in运算符会用到这个)没有影响
  [一个较小的例子](/Python-Knowledge/class_method_full_learn.py):使用多个特殊方法构建向量类  
  [序列实现的特殊方法](/Python-Knowledge/sequence_dunder_method.py)
### 迭代器&生成器
  [概述](/Python-Knowledge/iterable_iterator.py)  
  [标准库中的迭代器](/Python-Knowledge/iterator.py)  
  [链式求导](/Python-Knowledge/Iterator_chain.py)  
### 字符编码问题
  所谓字符串即为字符序列.在 python3 中,字符指的是 Unicode 字符,即人类可以'读取的文本'.  
  #### Unicode 字符有三个概念需要了解  
  * 所见的字符, 比如 s= 'café'
  * 字符的标识, 即码位. 比如字母 A 的码位是 U+0041
  * 字符的字节表示, 具体表述与编码有关. 编码是在码位与字节序列之间转换时使用的算法.  
  比如在 UTF-8 编码中,A(U+0041)的码位编码成单个字节 \x41,而在 UTF-16LE 编码中编码成两个字节\x41\x00  
  #### 编码和解码问题  
   从人类可读的 Unicode 字符转换到字节序列为编码, 从字节序列转换到人类可读 Unicode　字符是解码．显然解码与编码都涉及到编码方法，对应的 str.encode() 与 bytes.decode() 都需要有一个编码方法的参数  
  #### 编码之后的字节序列(bytes/bytearray)  
   将 Unicode 字符通过某种编码方式转换成字节序列.字节序列的每个元素是一个字节, 且值是 [0,255] 区间上的一个整数, 但是展示出来的并不是整数  
  比如, bytes('café', encoding='utf_8') -> b'caf\xc3\xa9'  
  各个字节的值可能有以下三种方式表示
  * 可打印的 ASCII 范围内的字节(从空格到 ~),使用 ASCII 字符本身 
  * 制表符、换行符、回车符和 \ 对应的字节,使用转义序列\t、\n、\r 和 \\
  * 其他字节的值,使用十六进制转义序列(例如,\x00 是空字节)  
  
  [文件处理的三明治原则](/Python-Knowledge/encoding_text_file.py)
### 参数
  [函数参数](/Python-Knowledge/function_argument.py)

# Part4. 实用小工具  
  包括一些文本批处理程序、自定义的 CLI ，比如模仿 Unix 命令等  
  * 之前写的一些[文件批处理程序](https://github.com/ZMbiubiubiu/python_files_prosessing_scripts)
  * 模仿 [ls](/Tool/ls.py) 命令  

  * 模仿 [more](/Tool/more.py) 命令  

  * 模仿 [head](/Tool/head.py) 命令,可选择打印出前n行,n值由你确定

  * 统计文本内容信息。[初始版](/Tool/stat_word_information.py) [加强版](/Tool/stat_word_enhanced.py)  

  * 输入一个路径,打印出路径下所有的文件,且递归搜索子目录[代码](/Tool/print_directory_content.py)  

  * 解析iTunes播放列表.[命令行版](/Tool/playlist/playlist.py) 代码重构,层次更加清晰,且使用click命令行库


  * 制造一个查看天气的命令行工具。[初始版](/Tool/weather.py) [加强版](/Tool/weather_strength.py)

  

