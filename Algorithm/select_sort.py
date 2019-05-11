# select_sort.py
# Created: 5 11 2019

"""
这是一个系列, 此为选择排序
"""

def select_sort(array:'list[int]'):
    """
        原地修改
    """
    if array == None or len(array) == 1:
        return array
    print(f'排序前:\t{array}')
    length = len(array)
    swap_count = 0
    for i in range(length):
        index_of_min = i
        # 找到此轮循环中的最小元素的索引
        for j in range(i+1, length):
            if array[index_of_min] > array[j]:
                index_of_min = j 
        # 交换
        array[i], array[index_of_min] = array[index_of_min], array[i]
        swap_count += 1
    # 输出
    print(f'排序后:\t{array}')
    print(f'交换次数:{swap_count} = 元素个数:{length}') # 不证自明的

if __name__ == "__main__":
    ll = [1, 4, 5, 6, 7, 7, 4, 8, 3, 3, 0]
    select_sort(ll)