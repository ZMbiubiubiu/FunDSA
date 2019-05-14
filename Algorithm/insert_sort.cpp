#include <iostream>
using namespace std;

void insert_sort(int arr[], int length) {
    // 这种算法明显交换次数是多余的,需要改进
    if (arr == NULL or length < 0) return;
    for (int i=1; i<length; i++) {
        for (int j=i; j>0; j--) {
            if (arr[j] < arr[j-1]) {
                int tmp = arr[j];
                arr[j] = arr[j-1];
                arr[j-1] = tmp;
            } else {
                break;
            }
        }
    }
}

void insert_sort2(int arr[], int length) {
    if (arr == NULL or length < 0) return;
    int i,j; // 在这里初始化.与python不同,c++的for语句有块作用域的作用
    for (i=1; i<length; i++) {
        int tmp = arr[i];
        for (j=i; j>0 && arr[j-1]>tmp; j--) {
            arr[j] = arr[j-1];
        }
        arr[j] = tmp;
    }
}

void print(int arr[], int length) {
    for (int i=0; i<length; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int arr[10] = {1, 3, 5, 5, 6, 2, 4, 9, 8, 7};
    print(arr, 10);
    insert_sort2(arr, 10);
    print(arr, 10);
}