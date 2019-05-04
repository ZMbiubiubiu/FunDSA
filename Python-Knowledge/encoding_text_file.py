# encoding_text_file.py
# Created: 4 30 2019

"""
处理文本文件的最佳实践是使用'三明治原则'
为了说明三明治原则, 我们需要一些基础知识
    1.前置知识, Unicode, utf-8, ANSCII, etc ...
    2.python3中, 字符串使用的是Unicode(就理解为人类可以明白的字符表示), 
      但是保存在文本文件中的内容使用的是字节序列.
    3.解码和编码. 编码 encode,就是将人类可见的Unicode字符转换成字节序列
                解码 decode,就是从人类不可见的字节序列转换成Unicode字符
                比如, b'Montr\xe9al'.decode('cp1252') = 'Montréal'
                      'café'.encode('utf-8') = b'caf\xc3\xa9'
    4. 关于默认值编码的最好建议, 就是不要依赖默认值编码
       默认编解码文件内容的设置, locale.getpreferredencoding()
       默认编解码文件名的设置,   sys.getfilesystemencoding()
       ps: 查看stdin/stdout/stderr的设置, sys.stdin/sys.stdout/sys.stderr
        
现在来说明'三明治原则'
    上片: 读入文件时, 将字节序列尽早的解码成字符串
    中间的'肉片': 业务的逻辑就是用来处理字符串
    下片: 写入文件时, 将字符串显示的编码成字节序列


"""

__author__ = 'ZzLee'
__email__ = 'zhangmeng.lee@foxmail.com'


# -------------- 一个错误的展示 --------------------------------
# 以utf-16的编码写入二进制序列到文件中
with open('en_de.code', 'w', encoding="utf-16") as f:
    f.write('café')

# 从文件中以utf-8解码出二进制序列
with open('en_de.code', 'r', encoding="utf-8") as f:
    data = f.read() # 抛出UnicodeDecodeError
    # 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte

# ----------------- 正确的使用 ----------------------------
# 显示的标注编码和解码方式, 为了跨平台, 请尽量选择不使用默认的编解码
with open('en_de.code', 'w', encoding="utf-8") as f:
    f.write('café')

with open('en_de.code', 'r', encoding="utf-8") as f:
    data = f.read()
# print(data) 
# >>> café

