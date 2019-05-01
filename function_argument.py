# function_argument.py
# Created: 5 01 2019

"""
定义一个tag函数, 用来生成HTML标签
涉及到的函数参数的知识
1.*和**用来打包输入参数
2.如何定义一个仅限关键字的参数
解答
1.content在函数内部是一个列表, attrs在函数内部是一个字典
2.此参数前要有*, 比如这个函数的cls, 如果不适用默认None, 自己定义的话,就得 cls = '..' 如此定义
"""

__author__ = 'ZzLee'
__email__ = 'zhangmeng.lee@foxmail.com'


def tag(name, *content, cls=None, **attrs):
    """
    name:      标签名称
    content:   标签内容.提示,自封闭标签没有标签内容
    cls:       定义一个标签的class
    attrs:     标签的属性
    """
    # 标签属性
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attrs_str = ''.join('{}={} '.format(attr, value) for attr, value in attrs.items())
    else:
        attrs_str = ""
    # 判断是否是自封闭标签
    if content:
        return '<{name} {attributions}>{text}</{name}>'.format(
            name = name,
            attributions = attrs_str,
            text = ' '.join(content),
        )
    else:
        return '<{name} {attributions}/>'.format(
            name = name,
            attributions = attrs_str,
        )

if __name__ == "__main__":
    print(tag('p'))
    print(tag('p', cls='hidebar', head ='top')) # head关键字参数不要写成'head'
    print(tag('p', 'hi', 'girl', cls = 'fam'))
    