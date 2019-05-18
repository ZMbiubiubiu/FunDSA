#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 每个桶使用快速排序算法
void swap(vector<int>&arr, int i, int j) {
    int tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
}

int partition(vector<int>& arr, int low, int high) {
    int left = low+1;
    int right = high;
    int flag = arr[low];
    while (1) {
        while (arr[left] <= flag && left < high) left++;
        while (arr[right] >= flag && right > low) right--;
        if (left < right) {
            swap(arr, left, right);
        } else {
            break;
        }
    }
    swap(arr, low, right);
    return right;
}
void sort(vector<int>& arr, int low, int high) {
    if (low >= high) return;
    int mid = partition(arr, low, high);
    sort(arr, low, mid-1);
    sort(arr, mid+1, high);
}

void quick_sort(vector<int>& arr) {
    if (arr.size() < 0) return;
    int low = 0;
    int high = arr.size() - 1;
    sort(arr, low, high);
}




void buck_sort(int arr[], int n) {
    vector<int> b[10]; // 建造10个桶
    for (int i=0; i<n; i++) {
        int bi = arr[i] / 10; // 桶的索引,比如 10-19 放到第2个桶里,因为10/10=1,会放到索引为1的桶里
        b[bi].push_back(arr[i]);
    }
    // 对每个桶排序
    for (int i=0; i<10; i++) {
        // sort(b[i].begin(), b[i].end());
        quick_sort(b[i]);
    }
    // 排序
    int index=0;
    for (int i=0; i<10; i++) {
        for (int j=0; j<b[i].size(); j++) {
            // cout << b[i][j] << endl;
            arr[index] = b[i][j];
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

int main() {
    int arr[100] = {25,33,53,34,61,43,6,92,54,36,60,99,97,30,28,45,67,10,18,10,71,2,65,43,80,78,77,2,86,
                    97,45,91,36,73,28,71,36,37,25,80,63,7,48,43,72,21,11,23,50,68,59,98,83,9,41,95,66,95,98,32,64,90,
                    79,64,12,62,8,47,8,66,77,84,42,20,35,13,88,37,82,62,11,66,71,50,98,23,97,74,2,26,72,55,65,16,10,
                    31,50,64,10,52
                    };
    print(arr, 100);
    buck_sort(arr, 100);
    print(arr, 100);
    return 0;
}