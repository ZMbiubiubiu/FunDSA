#! /home/bingo/anaconda3/bin/python
# *- coding=utf-8 -*

__author__ = "ZzLee"
__date__ = "2019/04/27"
__mail__ = "zhangmeng.lee@foxmail.com"

"""
    If you want to know more about python's iterator chains
    You can see "https://dbader.org/blog/python-iterator-chains"
"""

"""
step 1 .Remove spaces
step 2. Capitalize the word
step 3. Add a '~' at the end

"""
strings = ['   hello   ', 'world  ', 'this  ', 'is']



# =================================================================
# method 1 normal method
new_strings1 = []
for word in strings:
    word = word.strip()
    word = word.capitalize()
    word = word + '~'
    new_strings1.append(word)
print(new_strings1)



"""
tips:
1.The 'travel' generator yields a single word, let’s say 'world  '.
2.This “activates” the Strip generator, which processes the value 
  and passes it on to the next stage as word.strip() to 'world'
3.The 'world' yielded by the Strip generator gets fed immediately 
  into the Capitalize generator, which modifies it to 'World' and yields it again.
4. Eventually activates the Add generator, which processes the value 
  and passes it on to the next stage as word+"~" to 'World~'
"""
# =================================================================
# method 2 Iterator chains
def travel(seq):
    for word in seq:
        yield word
def Strip(seq):
    for word in seq:
        yield word.strip()
def Capitalize(seq):
    for word in seq:
        yield word.capitalize()
def Add(seq):
    for word in seq:
        yield word+'~'
new_strings2 = list(Add(Capitalize(Strip(travel(strings)))))
print(new_strings2)



# =================================================================
# method 3 Generator expressions
travel = (word for word in strings)
strip = (word.strip() for word in travel)
capitalize = (word.capitalize() for word in strip)
add = (word+'~' for word in capitalize)
new_strings3 = list(add)
print(new_strings3)


"""
Compared to the first method, the remaining two methods
have no buffering between the processing steps in the chain
"""