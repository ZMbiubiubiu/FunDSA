#include <iostream>
using namespace std;

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

void select_sort(int arr[], int length) {
    if (arr == NULL or length < 0 ) {
        cout << "Invlid inputs!" << endl;
        return ;
    }
    for (int i=0; i<length; i++) { // 每次循环找到一个最小值,为了找到所有最小值所以需要遍历n次
        int min = i;
        for (int j=i; j<length; j++) { // 每次循环找到一个局部最小值
            if (arr[j] < arr[min]) {
                min = j;
            }
        }
        swap(arr, i, min);
    }
}

int main()
{
    int arr[10] = {1, 4, 2, 6, 3, 5, 2, 9, 7, 5};
    print(arr, 10);
    select_sort(arr, 10);
    print(arr, 10);
    return 0;
}