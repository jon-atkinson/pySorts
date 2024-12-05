// Programmer: Jon Atkinson
// Purpose: A collection of sorting algorithms, written in C and designed to be compiled into
// a shared library to be called from pySorts (a sorting algorithm comparison program in python)

// FUNCTION INTERFACE:
// takes: arr, an array of n integers of size n
// returns: a pointer to the sorted array
// postcondition: arrays may sort in place or return a sorted copy of the input array but if a
// copy is returned, the original must be freed

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>

#define Parent(i) ((i-1)/2)
#define LeftChild(i) (i*2)
#define RightChild(i) (i*2+1)

int *selectionSort(int *arr, int n);
int *bubbleSort(int *arr, int n);
int *insertionSort(int *arr, int n);
int *heapSort(int *arr, int n);

void swap (int *first, int *second);
void printArray(int *arr, int n);
int *newRandArray(int n);
bool isSorted(int *arr, int n);

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

// Sorting Functions
int *bubbleSort(int *arr, int n) {
    for (int i = 0; i < n; i++) {
        bool swapped = false;
        for (int j = 0; j < n - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(&arr[j], &arr[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) break;
    }
    return arr;
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

int *insertionSort(int *arr, int n) {
    for (int i = 1; i < n; i++) {
        int val = arr[i];
        int j = i - 1;
        while (j >= 0 && val < arr[j]) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = val;
    }
    return arr;
}

int *selectionSort(int *arr, int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++) if (arr[j] < arr[minIdx]) minIdx = j;
        if (minIdx != i) swap(&arr[minIdx], &arr[i]);
    }
    return arr;
}

void swap(int *first, int *second) {
    int temp = *first;
    *first = *second;
    *second = temp;
}



// Testing Helper Functions
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
