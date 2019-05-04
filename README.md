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
      [初始版](/DataStructure/SinglyLinkedList.py)：实现链表的多个接口，增删改消➕反转  
      [加强版](/DataStructure/SinglyLinkedList_strengthen.py)：增加头哨兵，减少麻烦的·头·判断
  * 双链表  
      [初始版](/DataStructure/DoublyLinkedList.py):  
      [加强版](/DataStructure/DoublyLinkedList_strength.py):
### 队列  
  [用双链表实现队列](/DataStructure/queue_use_by_doubly_list.py)
### 栈  
  [用双链表实现栈](/DataStructure/stack_use_by_doubly_list.py)

# Part2. 基础算法  
  这一部分的学习资料来自邓俊辉老师课程、著名的《Algorithm》、简书、掘金等
### 冒泡排序  
  [实现特点](/Algorithm/bubble_sort.py) ：若中途已经有序，则不必继续‘冒泡’
### 归并排序

# Part3. python 知识点
  python 的进阶之路，学习资料来自《Fluent Python》、python 标准库等
### 特殊方法（Dunder method）
  [一个较小的例子](/Python-Knowledge/class_method_full_learn.py)
  [序列实现的特殊方法](/Python-Knowledge/sequence_dunder_method.py)
### 迭代器&生成器
  [概述](/Python-Knowledge/iterable_iterator.py)  
  [标准库中的迭代器](/Python-Knowledge/iterator.py)  
  [链式求导](/Python-Knowledge/Iterator_chain.py)  
### 字符编码问题
  [文件处理的三明治原则](/Python-Knowledge/encoding_text_file.py)
### 参数
  [函数参数](/Python-Knowledge/function_argument.py)

# Part4. 实用小工具  
  包括一些文本批处理程序、自定义的 CLI ，比如模仿 Unix 命令等  
  * 之前写的一些[文件批处理程序](https://github.com/ZMbiubiubiu/python_files_prosessing_scripts)
  * 模仿 [ls](/Tool/ls.py) 命令

  * 统计文本内容信息。[初始版](/Tool/stat_word_information.py) [加强版](/Tool/stat_word_enhanced.py)


  * 制造一个查看天气的命令行工具。[初始版](/Tool/weather.py) [加强版](/Tool/weather_strength.py)

  

