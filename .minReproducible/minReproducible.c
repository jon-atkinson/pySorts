#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>

#define Parent(i) ((i-1)/2)
#define LeftChild(i) (i*2)
#define RightChild(i) (i*2+1)

void buildMaxHeap(int *arr, int n);
int *heapSort(int *arr, int n);
void printArray(int *arr, int n);
int *newRandArray(int n);
bool isSorted(int *arr, int n);
void swap(int *first, int *second);

int main(void) {
    int n = 30;
    int *arr = newRandArray(n);

    printf("before sorting, arr is ");
    if (isSorted(arr, n)) printf("SORTED\n");
    else printf("NOT SORTED\n");
    printArray(arr, n);

    arr = heapSort(arr, n);

    printf("after sorting, arr is ");
    if (isSorted(arr, n)) printf("SORTED\n");
    else printf("NOT SORTED\n");
    printArray(arr, n);

    free(arr);
}

void buildMaxHeap(int *arr, int n) {
    for (int i = 0; i < n; i++) {
        if (arr[i] > arr[Parent(i)]) {
            int j = i;
            while (arr[j] > arr[Parent(j)]) {
                swap(&arr[j], &arr[Parent(j)]);
                j = Parent(j);
            }
        }
    }
}

int *heapSort(int *arr, int n) {
    buildMaxHeap(arr, n);
    for (int i = n - 1; i > 0; i--) {
        swap(&arr[0], &arr[i]);
        int j = 0;
        int index = 0;
        while (true) {
            index = RightChild(index);
            if (index < i - 1 && arr[index] < arr[index + 1]) index++;
            if (index < i && arr[j] < arr[index]) swap(&arr[j], &arr[index]);
            j = index;
            if (index >= i) break;
        }
    }
    return arr;
}

void printArray(int *arr, int n) {
    for (int i = 0; i < n; i++) printf("%d, ", arr[i]);
    putchar('\n');
}

int *newRandArray(int n) {
    srand(time(NULL));
    int *ptr = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) ptr[i] = rand() % n;
    return ptr;
}

bool isSorted(int *arr, int n) {
    if (n == 0) return true;
    int curr = arr[0];
    for (int i = 0; i < n; i++) {
        if (arr[i] < curr) return false;
        curr = arr[i];
    }
    return true;
}

void swap(int *first, int *second) {
    int temp = *first;
    *first = *second;
    *second = temp;
}
