# quick_sort.py
# Created: 5 11 2019

"""
    这是一个系列,此为快速排序
"""


# 交换数组中的两个元素
def exchange(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# 快速排序(原地排序)
def quick_sort(arr):
    if arr == None or len(arr) == 1:
        return arr
    low = 0
    high = len(arr) - 1
    sort(arr, low, high)
    
def sort(arr, low, high):
    if low >= high:
        return;
    mid = partition(arr, low, high)
    sort(arr, low, mid-1)
    sort(arr, mid+1, high)
    
def partition(arr, low, high):
    left = low+1
    right = high
    flag = arr[low]
    while 1:
        while arr[left] <= flag and left < high: # 从左向右扫描
            left += 1
        while arr[right] >= flag and right > low: # 从右向左扫描
            right -= 1
        if left >= right:
            break
        exchange(arr, left, right)
    exchange(arr, right, low)
    return right

if __name__ == "__main__":
    ll = [1 ,3, 2, 4,4,4,4, 67, 23 , 12]
    quick_sort(ll)
    print(ll)