`Python` `Algorithm` `CLI` `Computer fundamentals`

在接下来的日子里，我每天会至少用 python/C++ 编写一个程序，记录学习的重点:blush:。  
内容包括
* 数据结构
* 基础算法
* python的语法特性

# Part1. 数据结构
  在python新建类， 实现基础的数据结构。每一种数据结构可能有多种不同的实现，一部分可以当做学习邓俊辉老师课程的笔记， 一部分来自 Dan Bader 的系列博客，一部分来自自己所感所悟进行编写。
### 链表
  * 单链表  
      * [初始版](/DataStructure/SinglyLinkedList.py)：实现链表的多个接口，增删改消➕反转  
      * [加强版](/DataStructure/SinglyLinkedList_strengthen.py)：增加头哨兵，减少麻烦的·头·判断
  * 双链表  
      * [初始版](/DataStructure/DoublyLinkedList.py):  实现双链表的多个接口
      * [加强版](/DataStructure/DoublyLinkedList_strength.py): 增加头尾哨兵, 并在节点类的基础上添加插入方法
### 队列  
  [用双链表实现队列](/DataStructure/queue_use_by_doubly_list.py)
### 栈  
  [用双链表实现栈](/DataStructure/stack_use_by_doubly_list.py)  

### 二叉树  
  Python: [二叉树节点类](/DataStructure/Tree/BinNode.py) [二叉树类](/DataStructure/Tree/BinTree.py)  
  C++:(目前未实现)[二叉树节点类]() [二叉树类]()

# Part2. 基础算法  
  这一部分的学习资料来自邓俊辉老师课程、著名的《Algorithm》、简书、掘金等  

### 理解递归  
  关于递归这个概念,需要掌握三点:  
  * 明确递归函数的作用,并且相信它能够达成目的
  * 寻找到递归基,也就是结束的条件,不然会无限递归
  * 找到递归函数的等价关系式.比如f(n) = n*f(n-1)  

  示例:  
  单链表的翻转 [Python实现](/Algorithm/reverse_list.py)[C++迭代+递归实现](/Algorithm/reverse_list.cpp)  
  反转二叉树 [C++递归](/Algorithm/)  
### 选择排序  
  #### 原理  

首先找到数组中最小的元素,其次将它与第一个元素交换.然后在剩下的元素中找到最小的元素,与第二个元素交换.循环往复  
  #### 特点  

* 元素的移动次数最少,而且固定.根据算法的描述,不难看出,会移动N次,即元素的个数  
* 运行时间与输入无关.为了找到最小元素扫描一遍数组并不能为下一次扫描提供什么信息.  

[Python实现](/Algorithm/select_sort.py) 
[C++实现](/Algorithm/select_sort.cpp)  
```c++
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
```


### 插入排序  
  #### 原理  

  就是你打牌时,整理牌用的算法.

  [Python实现](/Algorithm/select_sort.py)    
  [C++实现](/Algorithm/select_sort.cpp) 
  ```
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
            arr[j] = arr[j-1]; // 将元素向后移动一位
        }
        arr[j] = tmp;
    }
}

void insert_sort3(int arr[], int length) {
    if (arr == NULL or length < 0) return;
    int i,j;
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
    insert_sort3(arr, 10);
    print(arr, 10);
}
  ```

### 冒泡排序  
  [Python实现](/Algorithm/bubble_sort.py) ：若中途已经有序，则不必继续‘冒泡’  
  ```
  def swap(arr, i, j):
    """
    交换'集合'中的两个元素
    """
    arr[i], arr[j] = arr[j], arr[i]

def bubble_sort(arr):
    if arr == None or len(arr) == 1:
        return arr
    high = len(arr) - 1
    while not bubble(arr, high):
        high -= 1

def bubble(arr, high):
    """
    完成单趟扫描
    注意两点
        每次单趟扫描, 都会检查是否有逆序数, 如果没有, 说明已经有序了, 已经不需要再次扫面, 提前结束
        每次单趟扫描之后, 局部最大值都会被'bubble'到最后位置, 所以逐渐将 high - 1
    """
    sorted = True
    for low in range(1, high + 1):
        if arr[low-1] > arr[low]:
            sorted = False
            swap(arr, low-1, low)
    return sorted

if __name__ == "__main__":
    arr = [1, 3, 5, 2, 2, 7, 4, 2]
    bubble_sort(arr)
    print(arr)
  ```
  [C++实现](/Algorithm/bubble_sort.cpp)  
 

### 归并排序  
  [Python实现](/Algorithm/merge_sort.py) : 先递归划分数组,然后向上合并  
  [Python原地修改实现](/Algorithm/merge_sort_inplace.py) : 需要有一个同等大小的辅助数组 
  [C++实现](/Algorithm/merge_sort.cpp)  
  ```
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

  ```

### 快速排序
  [Python实现](/Algorithm/quick_sort.py) : 重点是切分函数的实现 
  [C++实现](/Algorithm/quick_sort.cpp)  
  ```
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
    // 入口函数
    if (arr == NULL or n < 0 ) {
        cout << "Invlid inputs!" << endl;
        return ;
    }
    int low = 0;
    int high = n-1;
    sort(arr, low, high);
}

void sort(int arr[], int low, int high) {
    // 排序
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
        while (arr[left] <= flag && left < high) { // left<high 保证left不出格
            left++;
        }
        while (arr[right] >= flag && right > low) {
            right--;
        }
        if (left >= right) { // 此时分割已经完毕，只需要交换 low 与 right 即可
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
  ```

### 堆排序
目前还没有学习到这种算法.写在这里,只是为了完整.提示自己需要学习一下此排序.  

### 桶排序  
一个实现:排序0-99之间的整数,建造10个桶,根据num/10作为进入哪个桶的依据.如此一来每只桶装的数分别为0~9,10~19,...,90~99.然后每个桶用自己实现的快速排序进行排序.  
[C++实现](/Algorithm/buck_sort.cpp)  
```
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
```

### 计数排序
  [C++实现](/Algorithm/count_sort.cpp) 
  ```
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
    int len_tmp = max - min + 1; // 辅助数组的大小是根据输入数组数值的范围决定的,而不是输入数组的最大值决定.
    int *tmp = new int[len_tmp]; // 辅助数组,用来统计输入数组
    // 初始化辅助数组,全部置为0
    for (int i=0; i<len_tmp; i++) {
        tmp[i] = 0;
    }
    // 进行统计
    for (int i=0; i<length; i++) {
        int k = arr[i];
        tmp[k-min]++; // 其实就是辅助数组的索引值对应着数字，辅助数组索引对应的值对应着这个数字有多少个
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

void count_sort2(int arr[], int length) {
    int min = minNumber(arr, length);
    int max = maxNumber(arr, length);
    int len_tmp = max - min + 1;
    int *tmp = new int[len_tmp];
    for (int i=0; i<len_tmp; i++) {
        tmp[i] = 0;
    }
    for (int i=0; i<length; i++) {
        int k = arr[i];
        tmp[k-min]++;
    }
    int index=0;
    for (int i=0; i<len_tmp; i++) {
        for (int j=tmp[i]; j>0; j--) {
            arr[index] = i + min;
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
    count_sort2(arr, 20);
    print(arr, 20);
    return 0;
}
  ```

### 基数排序  

[C++实现](/Algorithm/radix_sort.cpp) 
```
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
```

### 二分查找  

[代码](/Algorithm/binary_search.py) : 将加法改成减法,防止溢出  
```
# binary_search.py
# Created: 5 9 2019

"""
这是一个系列, 此为二分查找
"""

def binary_search(array, target):
    if array == None:
        print('No valid input')
        return -1
    low = 0
    high = len(array) - 1
    while (low <= high):
        mid = low + (high-low) // 2 # 不写(low+high)/2 防止加法溢出
        if array[mid] > target:
            high = mid - 1
        elif array[mid] < target:
            low = mid + 1
        else:
            return mid
    return -1

if __name__ == "__main__":
    ll = [1, 3, 4, 5, 6, 12, 14 ,18 ,20 ,34, 45, 56, 67]
    print(binary_search(ll, 6))
```

# Part3. python 知识点
  python 的进阶之路，学习资料来自《Fluent Python》、python 标准库等  
### 最新的笔记已经转到[知乎专栏](https://zhuanlan.zhihu.com/c_1111662131090558976)  

### 特殊方法（Dunder method）
  体现 python 的一致性  
  [特殊方法__missing__](/Python-Knowledge/)  
    所有的映射类型在处理找不到键时,都会调用__missing__方法.
    * 基类dict并没有定义这个方法,但是dict是知道有这么个东西
    * 继承自dict的类,如果提供了__missing__方法,那么在__getitem__找不到键时,会调用它;如果没有提供__misssing__,则会直接抛出KeyError异常
    * 提供__missing__方法对get或者__contains__(in运算符会用到这个)没有影响
  [一个较小的例子](/Python-Knowledge/class_method_full_learn.py):使用多个特殊方法构建向量类  
  [序列实现的特殊方法](/Python-Knowledge/sequence_dunder_method.py)
### 迭代器&生成器
  [概述](/Python-Knowledge/iterable_iterator.py)  
  [标准库中的迭代器](/Python-Knowledge/iterator.py)  
  [链式求导](/Python-Knowledge/Iterator_chain.py)  
### 字符编码问题
  所谓字符串即为字符序列.在 python3 中,字符指的是 Unicode 字符,即人类可以'读取的文本'.  
  #### Unicode 字符有三个概念需要了解  
  * 所见的字符, 比如 s= 'café'
  * 字符的标识, 即码位. 比如字母 A 的码位是 U+0041
  * 字符的字节表示, 具体表述与编码有关. 编码是在码位与字节序列之间转换时使用的算法.  
  比如在 UTF-8 编码中,A(U+0041)的码位编码成单个字节 \x41,而在 UTF-16LE 编码中编码成两个字节\x41\x00  
  #### 编码和解码问题  
   从人类可读的 Unicode 字符转换到字节序列为编码, 从字节序列转换到人类可读 Unicode　字符是解码．显然解码与编码都涉及到编码方法，对应的 str.encode() 与 bytes.decode() 都需要有一个编码方法的参数  
  #### 编码之后的字节序列(bytes/bytearray)  
   将 Unicode 字符通过某种编码方式转换成字节序列.字节序列的每个元素是一个字节, 且值是 [0,255] 区间上的一个整数, 但是展示出来的并不是整数  
  比如, bytes('café', encoding='utf_8') -> b'caf\xc3\xa9'  
  各个字节的值可能有以下三种方式表示
  * 可打印的 ASCII 范围内的字节(从空格到 ~),使用 ASCII 字符本身 
  * 制表符、换行符、回车符和 \ 对应的字节,使用转义序列\t、\n、\r 和 \\
  * 其他字节的值,使用十六进制转义序列(例如,\x00 是空字节)  
  
  [文件处理的三明治原则](/Python-Knowledge/encoding_text_file.py)
### 参数
  [函数参数](/Python-Knowledge/function_argument.py)



