# merge_sort.py
# Created: 5 10 2019

"""
这是一个系列, 此为冒泡排序
"""

def sort(array):
    length = len(array)
    if length < 2:
        return array
    mid = (length) // 2
    left = array[:mid]
    right = array[mid:]
    # 递归分解然后向上合并
    print(f'left:\t{left}')
    print(f'right:\t{right}')
    return merge(sort(left), sort(right))
    
    
def merge(left, right):
    result = [0 for i in left + right]
    index = 0
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result[index] = left[0]
            left = left[1:]
        else:
            result[index] = right[0]
            right = right[1:]
        index += 1
    if len(left) > 0:
        for num in left:
            result[index] = num
            index += 1
    if len(right) > 0:
        for num in right:
            result[index] = num
            index += 1
    print(f'result:\t{result}')
    return result

if __name__ == "__main__":
    ll = [6, 3, 2, 7, 5, 9, 10]
    sort(ll)