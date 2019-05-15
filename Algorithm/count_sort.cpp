#include <iostream>
using namespace std;

int minNumber(int arr[], int length) {
    int min = arr[0];
    for (int i=1; i<length; i++) {
        if (arr[i] < min)
            min = arr[i];
    }
    return min;
}
int maxNumber(int arr[], int length) {
    int max = arr[0];
    for (int i=1; i<length; i++) {
        if (arr[i] > max)
            max = arr[i];
    }
    return max;
}

void count_sort(int arr[], int length) {
    if (arr == NULL or length < 0) {
        cout << "Invalid inputs!" << endl;
        return ;
    }
    int min = minNumber(arr, length);
    int max = maxNumber(arr, length);
    int len_tmp = max - min + 1;
    int *tmp = new int[len_tmp]; // 辅助数组,用来统计输入数组
    // 初始化辅助数组,全部置为0
    for (int i=0; i<len_tmp; i++) {
        tmp[i] = 0;
    }
    // 进行统计
    for (int i=0; i<length; i++) {
        int k = arr[i];
        tmp[k-min]++; // 辅助数组的大小是根据输入数组数值的范围决定的,而不是输入数组的最大值决定.
    }
    // 利用统计信息进行排序
    int index = 0;
    for (int i=0; i<len_tmp; i++) {
        for (int j=1; j<=tmp[i]; j++) {
            arr[index] = i+min;
            index++;
        }
    }
}

void print(int arr[], int length) {
    for (int i=0; i<length; i++) {
        if ( i%10 == 0) cout << endl;
        cout << arr[i] << "\t";
    }
    cout << endl;
}

int main()
{
    int arr[20] = {1, 4, 6, 3, 5, 3, 6, 4, 2, 4, 29, 34, 34, 45, 34, 23, 45, 34, 2, 4};
    print(arr, 20);
    count_sort(arr, 20);
    print(arr, 20);
    return 0;
}