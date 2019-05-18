#include <iostream>
using namespace std;

/*归并排序需要一个辅助数组*/

// 打印数组的函数
void print(int arr[], int length) {
    for (int i=0; i<length; i++) {
        if ( i%10 == 0) cout << endl;
        cout << arr[i] << "\t";
    }
    cout << endl;
}

void merge(int arr[], int* tmp, int low, int mid, int high) {
    // 将arr复制到tmp中
    for (int i=low; i<=high; i++) {
        tmp[i] = arr[i];
    }
    int left = low;
    int right = mid + 1;
    for (int k=low; k<=high; k++) {
        if (left > mid) { // 左边数组用完
            arr[k] = tmp[right++]; 
        } else if (right > high) {
            arr[k] = tmp[left++]; // 右边数组用完
        } else if (tmp[left] <= tmp[right]) {
            arr[k] = tmp[left++];
        } else {
            arr[k] = tmp[right++];
        }
    }
}

void sort(int arr[], int* tmp, int low, int high) {
    if (low >= high) return;

    int mid = low + (high-low) / 2;
    sort(arr, tmp, low, mid);
    sort(arr, tmp, mid+1, high);
    merge(arr, tmp, low, mid, high);
}
void merge_sort(int arr[], int n) {
    // 边界检查
    if (arr == NULL || n < 0) return;
    // 构造辅助数组
    int *tmp = new int[n];
    sort(arr, tmp, 0, n-1);
}

int main()
{
    int arr[10] = {1, 4, 2, 6, 3, 5, 2, 9, 7, 5};
    print(arr, 10);
    merge_sort(arr, 10);
    print(arr, 10);
    return 0;
}
