# insert_sort.py
# Created: 5 11 2019

"""
这是一个系列, 此为插入排序
"""

def insert_sort(array):
    if array == None or len(array) == 1:
        return array
    print(f'排序前:\t{array}')
    compare_count = 0
    swap_count = 0
    length = len(array)
    for i in range(1, length):
        for j in range(i, 0, -1): # 这步是关键!
            compare_count += 1
            if array[j] < array[j-1]:
                swap_count += 1
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break;
    print(f'排序后:\t{array}')
    print(f'元素个数:\t{length}')
    print(f'比较次数:\t{compare_count}')
    print(f'交换次数:\t{swap_count}')

if __name__ == "__main__":
    ll = [1, 4, 5, 6, 7, 7, 4, 8, 3, 3, 0]
    insert_sort(ll)