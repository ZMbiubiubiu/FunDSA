# binary_search.py
# Created: 5 9 2019

"""
这是一个系列, 此为二分查找
"""

def binary_search(array, target):
    if array == None:
        print('No valid input')
        return -1
    low = 0
    high = len(array) - 1
    while (low <= high):
        mid = low + (high-low) // 2 # 不写(low+high)/2 防止加法溢出
        if array[mid] > target:
            high = mid - 1
        elif array[mid] < target:
            low = mid + 1
        else:
            return mid
    return -1

if __name__ == "__main__":
    ll = [1, 3, 4, 5, 6, 12, 14 ,18 ,20 ,34, 45, 56, 67]
    print(binary_search(ll, 6))