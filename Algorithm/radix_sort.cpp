#include <iostream>
using namespace std;

int getMaxNumber(int arr[], int length) { // 取数组中的最大值
    int max = arr[0];
    for (int i=1; i<length; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

int getLengthOfNumber(int number) { // 一个整数的位
    int count = 1;
    while (number /= 10) {
        count++;
    }
    return count;
}

void radix_sort(int arr[], int length) {
    int max = getMaxNumber(arr, length);
    // 最大数的位数便是循环的次数, 所以取名 loops
    int loops = getLengthOfNumber(max);
    int radix = 1; // 基数,不断乘10
    int *tmp = new int[length]; // 辅助空间
    int *buck = new int[10]; // 计数的桶,0-9共10个数字
    int j,k;
    for (int i=1; i<=loops; i++) {
        // 清空桶
        for (j=0; j<10; j++) {
            buck[j] = 0;
        }
        // 记录每个桶中的个数
        for (j=0; j<length; j++) {
            // 数组中在当次循环位上的数字,即对应桶的位置
            k = (arr[j] / radix) % 10;
            buck[k]++;
        }
        // 将tmp中的位置依次分配给每个桶,具有累加效应.
        // 否则可能出现覆盖现象,或者顺序白排了.
        for(j = 1; j < 10; j++)
            buck[j] = buck[j - 1] + buck[j];
        // 将桶中暗示的元素顺序展示到辅助数组中
        for (j=length-1; j>=0; j--) {
            k = (arr[j] / radix) % 10;
            tmp[buck[k]-1] = arr[j];
            buck[k]--;
        }
        // 将辅助数组中的元素复制到原数组中
        for (j=0; j<length; j++) {
            arr[j] = tmp[j];
        }
        radix *= 10;
    }
    delete []tmp;
    delete []buck;
}

void print(int arr[], int length) {
    for (int i=0; i<length; i++) {
        cout << arr[i] << "\t";
    }
    cout << endl;
}

int main() 
{
    int arr[7] = {1, 10, 60, 743, 321, 577, 127};
    print(arr, 7);
    radix_sort(arr, 7);
    print(arr, 7);
    return 0;
}