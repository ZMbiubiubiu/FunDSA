#include <iostream>
#include <vector>
using namespace std;

void bubble_sort(vector<int>& arr) {
    if (arr.size() < 0) return;
    bool sorted = false;
    while (!sorted) {
        sorted = true;
        for (int i=0; i<arr.size()-1; i++) {
            if (arr[i] > arr[i+1]) {
                int tmp = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = tmp;
                sorted = false;
            } 
        }
    }
}

void print(vector<int> &arr) {
    for (auto &i:arr) {
        cout << i << "\t";
    }
    cout << endl;
}

int main()
{
    vector<int> arr{1, 4, 7, 2, 5, 99, 23, 45, 67};
    print(arr);
    bubble_sort(arr);
    print(arr);
    return 0;
}