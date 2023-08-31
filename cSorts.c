// Programmer: Jon Atkinson
// Purpose: A collection of sorting algorithms, written in C and designed to be compiled into
// a shared library to be called from pySorts (a sorting algorithm comparison program in python)

// FUNCTION INTERFACE:
// takes: arr, an array of n integers of size n
// returns: a c_int pointer to the sorted array
// postcondition: arrays may sort in place or return a sorted copy of the input array but if a
// copy is returned, the original must be freed

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int *selectionSort(int *arr, int n);
int *bubbleSort(int *arr, int n);
int *insertionSort(int *arr, int n);
int *heapSort(int *arr, int n);

void swap (int *first, int *second);
void printArray(int *arr, int n);
int *newRandArray(int n);
bool isSorted(int *arr, int n);

int main(void) {
    int n = 10000;
    int *arr = newRandArray(n);

    printf("before sorting, arr is ");
    if (isSorted(arr, n)) printf("SORTED\n");
    else printf("NOT SORTED\n");

    arr = bubbleSort(arr, n);

    printf("after sorting, arr is ");
    if (isSorted(arr, n)) printf("SORTED\n");
    else printf("NOT SORTED\n");

    free(arr);
}

int *selectionSort(int *arr, int n) {
    
}


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

void swap(int *first, int *second) {
    int temp = *first;
    *first = *second;
    *second = temp;
}



// Helper Functions
void printArray(int *arr, int n) {
    for (int i = 0; i < n; i++) printf("%d, ", arr[i]);
}

int *newRandArray(int n) {
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