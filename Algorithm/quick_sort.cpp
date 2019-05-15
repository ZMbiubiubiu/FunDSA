#include <iostream>
using namespace std;


int partition(int arr[], int low, int high);
void sort(int arr[], int low, int high);
// 打印数组的函数
void print(int arr[], int length) {
    for (int i=0; i<length; i++) {
        if ( i%10 == 0) cout << endl;
        cout << arr[i] << "\t";
    }
    cout << endl;
}

void swap(int arr[], int i, int j) {
    int tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
}

void quick_sort(int arr[], int n) {
    if (arr == NULL or n < 0 ) {
        cout << "Invlid inputs!" << endl;
        return ;
    }
    int low = 0;
    int high = n-1;
    sort(arr, low, high);
}

void sort(int arr[], int low, int high) {
    if (low >= high) {
        return ;
    }
    int mid = partition(arr, low, high);
    sort(arr, low, mid-1);
    sort(arr, mid+1, high);
}


int partition(int arr[], int low, int high) {
    int flag = arr[low];
    int left = low+1;
    int right = high;
    while (1) {
        while (arr[left] <= flag && left < high) {
            left++;
        }
        while (arr[right] >= flag && right > low) {
            right--;
        }
        if (left >= right) {
            break;
        }
        swap(arr, left, right);
    }
    swap(arr, low, right);
    return right;
}




int main()
{
    int arr[10] = {1, 4, 2, 6, 3, 5, 2, 9, 7, 5};
    print(arr, 10);
    quick_sort(arr, 10);
    print(arr, 10);
    return 0;
}