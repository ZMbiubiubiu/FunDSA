def merge_sort(array):
    # array为空或None,不需要排序
    if array == None or len(array) == 1:
        return array
    low = 0
    high = len(array) - 1
    new = array[:]
    sort(array, low, high)
    

def sort(arr, low, high):
    # 递归基:只有一个元素
    if low >= high:
        return;
    mid = low + (high - low) // 2
    sort(arr, low, mid)        # 左半边排序
    sort(arr, mid+1, high)     # 右半边排序
    merge(arr, low, mid, high) # 归并

def merge(arr, low, mid, high):
    global new # 我们需要不断的修改new
    for i in range(low, high+1):
        new[i] = arr[i]
    left = low
    right = mid+1
    for k in range(low, high+1):
        if left > mid: # 左半边用尽
            arr[k] = new[right]
            right += 1
        elif right > high: # 右半边用尽
            arr[k] = new[left]
            left += 1
        elif new[left] > new[right]: # 右边的元素比左边的小
            arr[k] = new[right]
            right += 1
        else:  # 左边的元素比右边的小
            arr[k] = new[left]
            left += 1

if __name__ == "__main__":
    ll = [2, 4, 2, 5, 3, 67, 23, 78]
    # 务必要有一个同等大小的数组
    # 这也是个缺陷, 可以考虑写一个归并排序类
    new = [0 for index,_ in enumerate(ll)]
    merge_sort(ll)
    print(ll)