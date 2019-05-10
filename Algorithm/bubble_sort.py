# bubble_sort.py
# Created: 4 30 2019

"""
这是一个系列, 此为冒泡排序
"""

__author__ = 'ZzLee'
__email__ = 'zhangmeng.lee@foxmail.com'
__version__ = '1.0'

def swap(arr, i, j):
    """
    交换'集合'中的两个元素
    """
    arr[i], arr[j] = arr[j], arr[i]

def bubble_sort(arr):
    if arr == None or len(arr) == 1:
        return arr
    high = len(arr) - 1
    while not bubble(arr, high):
        high -= 1

def bubble(arr, high):
    """
    完成单趟扫描
    注意两点
        每次单趟扫描, 都会检查是否有逆序数, 如果没有, 说明已经有序了, 已经不需要再次扫面, 提前结束
        每次单趟扫描之后, 局部最大值都会被'bubble'到最后位置, 所以逐渐将 high - 1
    """
    sorted = True
    for low in range(1, high + 1):
        if arr[low-1] > arr[low]:
            sorted = False
            swap(arr, low-1, low)
    return sorted

if __name__ == "__main__":
    arr = [1, 3, 5, 2, 2, 7, 4, 2]
    bubble_sort(arr)
    print(arr)